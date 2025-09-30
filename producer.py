# producer.py
import time, requests, json
from kafka import KafkaProducer
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

API_URL = "https://api.exchangerate.host/latest"

def fetch_rates():
    r = requests.get(
        API_URL,
        params={
            "base": "USD",
            "symbols": "YER,SAR",
            "access_key": "c17b41c7c6e7635f59c2bcd894134b0a"
        },
        timeout=10
    )
    r.raise_for_status()
    return r.json()

while True:
    data = fetch_rates()
    if "base" in data and "rates" in data:
        payload = {
            "fetched_at": datetime.utcnow().isoformat(),
            "base": data["base"],
            "rates": data["rates"]
        }
        producer.send("money-tracker", payload)
        producer.flush()
        print("Produced:", payload)
    else:
        print("Warning: Missing 'base' or 'rates' in API response:", data)
    time.sleep(60)
