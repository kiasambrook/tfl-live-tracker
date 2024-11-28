from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access environment variables
TFL_API_KEY = os.getenv("TFL_API_KEY")

if not TFL_API_KEY:
    raise Exception("TFL_API_KEY is missing. Please set it in your .env file.")
