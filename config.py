import os
import secrets

class Config:
    # secret key used by Flask for security purposes 
    SECRET_KEY = os.getenv("SECRET_KEY") or secrets.token_hex(32)
    JSON_SORT_KEYS = False