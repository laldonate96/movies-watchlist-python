import os
from flask import Flask
from dotenv import load_dotenv
from pymongo import MongoClient

from movie_library.routes import pages

load_dotenv()


app = Flask(__name__)
app.config["MONGODB_URI"] = os.environ.get("MONGODB_URI")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.db = MongoClient(app.config["MONGODB_URI"]).get_default_database()

app.register_blueprint(pages)
