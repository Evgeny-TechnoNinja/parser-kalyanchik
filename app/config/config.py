import os
from dotenv import load_dotenv
from typing import Dict, Any

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
BOT_ADMIN = os.getenv("BOT_ADMIN")
# The file for logging requests errors must have the extension .log
HTTP_ERROR_FILE = "requests_error.log"
PROXIES = os.getenv("PROXIES").replace(" ", "").split(",")  # type: ignore
PROXY_LOGIN = os.getenv("PROXY_LOGIN")
PROXY_PASSWORD = os.getenv("PROXY_PASSWORD")
PROXIES_TEST_OPTIONS: Dict[str, Any] = {
    "timeout": 3,
    "multiplication_attempts": 2,
    "url": "http://icanhazip.com/"
}
USER_AGENT_DATA:  Dict[str, Any] = {
    "default": "Mozilla/5.0 (Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0",
    "url": "https://seolik.ru/user-agents-list",
    "regex": {
        "user_agent": "Mozilla/5.0"
    }
}
MARKUP_ANALYZER = "lxml"
DONOR_URL = "https://opt.kalyanchik.ua/"
SLEEP_PARAMETERS = ((1, 3), (2, 5))
NAVIGATION_NAME = "page"
