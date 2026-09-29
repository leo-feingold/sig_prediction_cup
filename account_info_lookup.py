import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("api_key_1")
if not api_key:
    raise ValueError("Add api_key_1 to your .env file")

base_url = "https://sig.thesuper.market/api/v1"

response = requests.get(
    f"{base_url}/account",
    headers={"Authorization": f"Bearer {api_key}"},
    timeout=20,
)

print("Status:", response.status_code)

if not response.ok:
    print(response.text)
    response.raise_for_status()

data = response.json()
print(json.dumps(data, indent=2))