secret_key = "18fd24bf6a2ad4dac04a33963db1c42f"


# For flaw 1 Cryptographic Failures
# Fix: secret key is read from .env file via environment variable
#import os 
#from dotenv import load_dotenv

#load_dotenv()
#secret_key = os.environ.get("SECRET_KEY")
#if not secret_key:
#    raise RuntimeError("SECRET_KEY missing .env-file") 
