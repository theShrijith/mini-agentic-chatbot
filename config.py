from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in .env file. Please create a .env file with GOOGLE_API_KEY=your_key_here.") 