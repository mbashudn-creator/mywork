import os
from dotenv import load_dotenv
import dotenv
from openai import OpenAI
load_dotenv(override=True)
client = OpenAI(base_url=os.getenv("OPENAI_API_BASE"), 
                api_key=os.getenv("OPENAI_API_KEY"))
MODEL = os.getenv("MODEL")
PRICE_IN, PRICE_OUT, INR = 0.075, 0.30, 95.0 # $/1M tokenks,