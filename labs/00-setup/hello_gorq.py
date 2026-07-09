import os
from groq import Groq
client = Groq(api_key=os.environ["GROQ_API_KEY"])
r = client.chat.completions.create(model="llama-3.3-70b-versatile", messages=[{"role":"user","content":"Say hello in exactly five words"}])
print(r.choices[0].message.content)