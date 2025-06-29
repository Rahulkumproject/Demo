from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env file

secret = os.environ.get("SOME_SECRET", "Valueismissing")
print(secret)