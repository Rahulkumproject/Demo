from dotenv import load_dotenv
import os
from pymongo import MongoClient

# Load variables from .env file
load_dotenv()

# Get MongoDB connection string from environment variable
mongo_uri = os.environ.get("SOME_SECRET")

# Connect to MongoDB

try:
    client = MongoClient(mongo_uri)
    db = client.Socks  # Replace 'test' with your database name
    
    print("Connected to MongoDB successfully!")
    # print("Databases:", client.list_database_names())
    Jockey = db.Jockey
      # Replace 'test' with your collection name
    print("Collections in 'Socks' database:", list(Jockey.find()))
except Exception as e:
    print("Failed to connect to MongoDB:", e)