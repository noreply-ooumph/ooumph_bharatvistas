import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent / ".env", override=True)

ACCOUNT_USERNAME = "bharat.vistas"
ACCOUNT_USER_ID  = 59542557883
ACCOUNT_NICHE    = "Indian travel photography, landscapes, heritage sites, culture, traditions, and the beauty of Bharat"

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
    "Iconic Indian monuments and heritage sites -- Taj Mahal, temples, forts",
    "Himalayan landscapes -- mountains, valleys, snow peaks, trekking routes",
    "Cultural festivals and traditions -- Holi, Diwali, local fairs",
    "Hidden gems and offbeat destinations -- lesser-known India",
    "Street photography -- Indian markets, people, daily life",
    "Coastal beauty -- Goa, Kerala backwaters, beaches",
    "Wildlife and nature -- national parks, tigers, birds",
    "Indian cuisine and food culture -- street food, regional dishes",
    "Village India -- rural life, traditions, crafts",
    "Road trips and travel stories -- highways, chai stops, adventures",
]

HASHTAG_POOLS = {
    "travel":     ["#indiatravel", "#incredibleindia", "#travelindia", "#indiatourism", "#exploreindia"],
    "photo":      ["#travelphotography", "#landscapephotography", "#naturephotography", "#streetphotography"],
    "heritage":   ["#heritage", "#heritagesite", "#ancientindia", "#monument", "#incredibleindiaofficial"],
    "nature":     ["#himalaya", "#mountains", "#nature", "#wildlife", "#waterfalls", "#forests"],
    "culture":    ["#indianculture", "#tradition", "#festival", "#india", "#desi"],
    "general":    ["#reels", "#explore", "#viral", "#trending", "#instagram", "#fyp", "#instagood"],
}
