import logging
from dotenv import load_dotenv
from google import genai
from google.genai.types import HttpOptions

# Suppress google_genai SDK warnings
logging.getLogger('google_genai').setLevel(logging.ERROR)

load_dotenv()

client = genai.Client(http_options=HttpOptions(api_version="v1"))

print("Sending request to Gemini...")
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='Tell me about Google Cloud Agent Development Kit.',
)
print("\nResponse:")
print(response.text)