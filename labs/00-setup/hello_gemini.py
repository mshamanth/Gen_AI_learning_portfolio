import os
from google import genai
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
r = client.models.generate_content(model="gemini-2.0-flash", contents="Say hello in exactly five words")
print(r.text)