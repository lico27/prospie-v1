import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

URL = "https://charitybase.uk/api/graphql"
HEADERS = {
    "Authorization": f"Apikey {api_key}",
    "Content-Type": "application/json",
}
COUNT_QUERY = """
{
  CHC {
    getCharities(filters: {}) {
      count
    }
  }
}
"""

def count_charities():
    try:
        res = requests.post(
            URL,
            headers=HEADERS,
            json={ "query": COUNT_QUERY }
        )
        payload = res.json()
    except Exception as e:
        print("REQUEST ERROR (probably your network)")
        raise Exception(e)
    if "errors" in payload:
        print("QUERY ERRORS")
        raise Exception(payload["errors"])
    print(payload["data"])
    return payload["data"]["CHC"]["getCharities"]["count"]

count_charities()
