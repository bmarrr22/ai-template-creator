"""
AI Product Discovery Configuration v3.2
"""

# ======================
# Core Discovery Settings
# ======================
REDDIT_SUBREDDITS = [
    "IndieHackers", 
    "SideProject",
    "Entrepreneur",
    "DigitalNomad"
]  # Target low-competition communities
REDDIT_FETCH_LIMIT = 20  # Increased for better trend sampling from 75
REQUEST_DELAY = .1  # Seconds between API calls from 1.2

# ======================
# Google Trends Configuration
# ======================
GOOGLE_TRENDS_KEYWORDS = [
    "micro saas", 
    "nocode tools",
    "passive income",
    "solopreneur"
]  # Long-tail, low-competition keywords
GOOGLE_TRENDS_TIMEFRAME = "today 3-m"  # Optimal for emerging trends
GOOGLE_TRENDS_GEO = "US"  # ISO 3166-2 country code
GOOGLE_TRENDS_MAX_RETRIES = 3  # Retry failed requests

# ======================
# AI/ML Configuration
# ======================
OPENAI_MODEL = "gpt-4-turbo-preview"  # Current recommended model
OPENAI_TEMPERATURE = 0.65  # Balance creativity vs focus
OPENAI_TIMEOUT = 45  # Seconds per request
OPENAI_MAX_RETRIES = 5  # Retry transient errors
ANALYSIS_MAX_INPUT = 150  # Max items sent to AI model

# ======================
# Content Filtering
# ======================
PROBLEM_KEYWORDS = [
    "how to", "why can't", 
    "looking for", "best way to",
    "struggling with", "alternative to"
]  # Phrases indicating unmet needs
CONTENT_FILTERS = [
    "nsfw", "illegal", 
    "crypto", "gambling"
]  # Blocked content categories

# ======================
# Output Configuration
# ======================
THEMES_OUTPUT_DIR = "discoveries"  # Changed from 'themes'
OUTPUT_PREFIX = "niche_ideas_"
OUTPUT_FORMAT = "%Y-%m-%d_%H%M"  # File timestamp format
MAX_OUTPUT_FILES = 30  # Auto-rotate old files

# ======================
# System Behavior
# ======================
LOG_LEVEL = "INFO"  # DEBUG/INFO/WARNING/ERROR
ENABLE_ANALYTICS = False  # Set to True for performance metrics
FAILURE_THRESHOLD = 0.25  # Abort if >25% API calls fail

# ======================
# Security & Compliance
# ======================
USER_AGENT = "NicheFinderBot/3.0 (by /u/your_username)"  # Reddit requirement
DATA_RETENTION_DAYS = 7  # Auto-delete old data

# ======================
# Validation Rules
# ======================
MIN_TITLE_LENGTH = 15  # Characters
MAX_TITLE_LENGTH = 300  # Characters
