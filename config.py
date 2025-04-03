# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "25531017"))
API_HASH = getenv("API_HASH", "c38eb0777ce9876e1b11729f8c35c7a7")
BOT_TOKEN = getenv("BOT_TOKEN", "7146629756:AAG2_qVX2SOvW35vUR9rAp371-qa7Rg7d_A")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7418520746").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://newshelpforeveryone:fIg1jWwn6BfyMT7R@cluster0.ailhjhy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002571422633")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002622788463"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "50000"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
