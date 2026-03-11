# configuration file, separates application settings from the rest
# of the application, contains secret key, db URI etc..
from pathlib import Path
import os

basedir = Path(__file__).parent
# might be incorrect / or \  based on win/nix?
# print(f'sqlite:///{basedir / "app.db"}')

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'sqlite:///' / basedir / 'app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False