from google import genai
import os
from dotenv import load_dotenv

load_dotenv("api_key.env")
api_key = os.getenv("gemini_api_key")
client = genai.Client(api_key=api_key)

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Which gemini free model is best for fast and accurate results?"
)
print(interaction.output_text)