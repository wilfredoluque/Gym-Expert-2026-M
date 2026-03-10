import os
class Config:
    SECRET_KEY = "GYM-EXPERT-KEY"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///gym.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False