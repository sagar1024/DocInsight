# from app.utils.external_api import call_gemini_api
# import asyncio

# async def test_api():
#     response = await call_gemini_api("Summarize this text: Machine learning is important.")
#     print(response)

# asyncio.run(test_api())

import os
from dotenv import load_dotenv

load_dotenv()  # Ensure .env is loaded
print(f"GEMINI_API_KEY = {os.getenv('GEMINI_API_KEY')}")
