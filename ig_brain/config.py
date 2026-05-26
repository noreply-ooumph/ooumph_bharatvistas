import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent / ".env", override=True)

ACCOUNT_USERNAME = "muggedmoments"
ACCOUNT_USER_ID  = 65545472191
ACCOUNT_NICHE    = "Coffee culture, aesthetic mugs, cozy lifestyle, cafe vibes, morning rituals, and everyday beautiful moments"

POSTING_HOURS    = [9, 13, 18, 21]
POSTS_PER_DAY    = 1

REPLY_CHECK_INTERVAL = 300
REPLY_SLEEP_MIN      = 5
REPLY_SLEEP_MAX      = 15

EVOLUTION_AFTER_POSTS = 5

BASE_DIR      = Path(__file__).parent.parent
MEMORY_FILE   = BASE_DIR / "brain_memory.json"
POSTED_FILE   = BASE_DIR / "posted_content.json"
REPLIED_FILE  = BASE_DIR / "replied_comments.json"
IMAGES_DIR    = BASE_DIR / "generated_images"
IMAGES_DIR.mkdir(exist_ok=True)

ANTHROPIC_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
GROQ_KEY      = os.environ.get("GROQ_API_KEY", "")

CONTENT_PILLARS = [
    "Aesthetic coffee and mug photography -- latte art, steam, cozy setups",
    "Morning ritual content -- slow mornings, journals, and a perfect cup",
    "Cafe culture and coffee shop vibes -- ambiance and atmosphere",
    "Coffee recipes and brewing methods -- pour over, french press, espresso",
    "Cozy lifestyle -- books, blankets, rainy days and coffee",
    "Behind the mug -- stories of people and their coffee moments",
    "Seasonal coffee drinks -- winter warmers, summer cold brews",
    "Minimalist and aesthetic flat lay photography",
    "Coffee facts and trivia -- engaging educational content",
    "Community moments -- user stories and coffee connections",
]

HASHTAG_POOLS = {
    "coffee":     ["#coffee", "#coffeelover", "#coffeeaddict", "#coffeetime", "#coffeeoftheday", "#specialtycoffee", "#latteart", "#espresso"],
    "aesthetic":  ["#aesthetic", "#coffeesthetic", "#cozy", "#cozyliving", "#slowmorning", "#morningroutine", "#cozyhome", "#hygge"],
    "mugs":       ["#muglife", "#coffeemug", "#mugshot", "#ceramics", "#potterylove", "#handmade", "#mugcollection"],
    "cafe":       ["#cafevibes", "#cafelife", "#coffeeshop", "#cafestagram", "#coffeehouse", "#barista", "#brewedwithlove"],
    "lifestyle":  ["#lifestyle", "#morningvibes", "#selfcare", "#weekendvibes", "#homecafe", "#cottagecore", "#comfortzone"],
    "general":    ["#reels", "#explore", "#viral", "#trending", "#instagram", "#fyp", "#instagood"],
}
