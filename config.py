import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_LINK")
    SQLALCHEMY_TRACK_MODIFICATIONS = False