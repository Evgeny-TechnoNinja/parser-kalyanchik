import os
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
BOT_ADMIN = os.getenv("BOT_ADMIN")
# The file for logging requests errors must have the extension .log
HTTP_ERROR_FILE = "requests_error.log"
PROXIES = os.getenv("PROXIES").replace(" ", "").split(",")
PROXY_LOGIN = os.getenv("PROXY_LOGIN")
PROXY_PASSWORD = os.getenv("PROXY_PASSWORD")
PROXIES_TEST_OPTIONS = {
    "timeout": 3,
    "multiplication_attempts": 2,
    "url": "http://icanhazip.com/"
}

USER_AGENT_DATA = {
    "default": "Mozilla/5.0 (Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0",
    "url": "https://seolik.ru/user-agents-list"
}
