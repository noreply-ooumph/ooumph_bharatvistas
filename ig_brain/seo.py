"""
SEO + AEO Optimizer -- captions, hashtags, image prompts via Claude.
"""
import random
from .config import HASHTAG_POOLS, CONTENT_PILLARS, ACCOUNT_NICHE
from .memory import load_memory


def pick_hashtags(topic: str, count: int = 25) -> list:
    t = topic.lower()
    pool = []
    if any(x in t for x in ["coffee","espresso","latte","brew","pour","french","cappuccino","americano"]):
        pool += HASHTAG_POOLS.get("coffee", [])
    if any(x in t for x in ["aesthetic","cozy","hygge","minimal","photography","bokeh"]):
        pool += HASHTAG_POOLS.get("aesthetic", [])
    if any(x in t for x in ["mug","ceramic","cup","pottery","handmade","collection"]):
        pool += HASHTAG_POOLS.get("mugs", [])
    if any(x in t for x in ["cafe","barista","shop","coffeehouse","roaster"]):
        pool += HASHTAG_POOLS.get("cafe", [])
    if any(x in t for x in ["morning","lifestyle","routine","self","cozy","weekend","home"]):
        pool += HASHTAG_POOLS.get("lifestyle", [])
    pool += HASHTAG_POOLS.get("general", [])
    seen, out = set(), []
    for tag in pool:
        if tag not in seen:
            seen.add(tag); out.append(tag)
    random.shuffle(out)
    return out[:count]


def generate_seo_caption(client, topic: str, pillar: str) -> str:
    mem      = load_memory()
    strategy = mem.get("strategy_notes", "")
    resp = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=700,
        system=(
            "You are an expert Instagram SEO and AEO content writer for muggedmoments, "
            f"a coffee culture and aesthetic lifestyle account. Niche: {ACCOUNT_NICHE}

"
            "SEO Rules: First line = powerful hook. Include 2-3 natural keyword phrases. Short paragraphs.

"
            "AEO Rules: Include a direct factual/coffee statement early. "
            "Structure: Hook -> Coffee insight -> Cozy detail -> CTA.

"
            "Tone: cozy coffee enthusiast -- warm, aesthetic, inviting. "
            "Format: 150-250 words. Tasteful emojis. End with 1 engaging question. NO hashtags."
        ),
        messages=[{"role": "user", "content": (
            f"Topic: {topic}
Pillar: {pillar}
Strategy: {strategy}

Write the Instagram caption:"
        )}]
    )
    return resp.content[0].text.strip()


def generate_image_prompt(client, topic: str) -> str:
    resp = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=150,
        system="Write only a FLUX/Stable Diffusion image generation prompt. 2-3 sentences. No explanation.",
        messages=[{"role": "user", "content": (
            f"Topic: {topic}
"
            "Style: warm moody coffee photography aesthetic, steam rising from a mug, soft bokeh background, "
            "cozy tones of brown and cream, hyper-detailed, square 1:1 composition. No text in image."
        )}]
    )
    return resp.content[0].text.strip()
