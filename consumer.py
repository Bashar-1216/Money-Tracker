# consumer_to_mongo.py
import json
from kafka import KafkaConsumer
from pymongo import MongoClient, ASCENDING, DESCENDING
from datetime import datetime

# Kafka Consumer
consumer = KafkaConsumer(
    "money-tracker",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

# MongoDB
mongo = MongoClient("mongodb://localhost:27017")
db = mongo["money"]
coll = db["money-tracker"]


coll.create_index([("currency", ASCENDING), ("fetched_at", DESCENDING)])

print("Consumer started... waiting for messages.")

for msg in consumer:
    try:
        doc = msg.value
        ts = datetime.fromisoformat(doc["fetched_at"])
        for cur, val in doc.get("rates", {}).items():
            if val is None:
                continue
            entry = {
                "base": doc.get("base", "N/A"),
                "currency": cur,
                "rate": float(val),
                "fetched_at": ts,
                "timestamp": int(ts.timestamp())
            }
            
            coll.update_one(
                {"currency": cur, "fetched_at": ts},
                {"$set": entry},
                upsert=True
            )
        print(f"[{ts}] Inserted/Updated rates for {list(doc['rates'].keys())}")
    except Exception as e:
        print("Error processing message:", e)
