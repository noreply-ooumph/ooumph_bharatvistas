import json, random
from .config import CONTENT_PILLARS, POSTS_PER_DAY
from .memory import load_memory

def extract_json(text: str):
    text = text.strip()
    if chr(96)*3 in text:
        parts = text.split(chr(96)*3)
        for part in parts:
            part = part.strip()
            if part.startswith("json"):
                part = part[4:].strip()
            try: return json.loads(part)
            except Exception: continue
    try: return json.loads(text)
    except Exception: pass
    for sc, ec in [("{"  , "}"), ("[", "]")]:
        s = text.find(sc); e = text.rfind(ec)
        if s != -1 and e != -1:
            try: return json.loads(text[s:e+1])
            except Exception: pass
    raise ValueError(f"No valid JSON found in: {text[:200]}")

def generate_content_plan(client, days: int = 7) -> list:
    mem = load_memory()
    strategy = mem.get("strategy_notes", "")
    pillars = "
".join(f"- {p}" for p in CONTENT_PILLARS)
    resp = client.messages.create(
        model="claude-sonnet-4-5", max_tokens=1500,
        system=(
            "You are a content strategist for muggedmoments, a coffee culture and aesthetic lifestyle Instagram account. "
            "Return ONLY a valid JSON array of post objects. No explanation, no markdown. "
            "Each object must have: topic (string), pillar (string), content_type (educational|inspirational|storytelling|viral)."
        ),
        messages=[{"role": "user", "content": (
            f"Create {days * POSTS_PER_DAY} diverse Instagram post ideas.

"
            f"Content pillars:
{pillars}

Strategy:
{strategy}

"
            f"Return a JSON array with {days * POSTS_PER_DAY} objects. Make each topic vivid and specific."
        )}]
    )
    text = resp.content[0].text.strip()
    posts = extract_json(text)
    if isinstance(posts, dict): posts = posts.get("posts", [posts])
    print(f"[PLANNER] {len(posts)} posts planned for {days} days.")
    return posts

def generate_single_topic(client) -> dict:
    mem = load_memory()
    strategy = mem.get("strategy_notes", "")
    pillar = random.choice(CONTENT_PILLARS)
    resp = client.messages.create(
        model="claude-haiku-4-5-20251001", max_tokens=200,
        system="Return ONLY a valid JSON object with keys: topic, pillar, content_type. No explanation.",
        messages=[{"role": "user", "content": (
            f"Generate ONE unique Instagram post idea for muggedmoments.
"
            f"Pillar: {pillar}
Strategy: {strategy}
Make it vivid and specific."
        )}]
    )
    return extract_json(resp.content[0].text.strip())
