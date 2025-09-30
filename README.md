# Money Tracker Project

This project is a simple currency exchange rate tracker that uses Kafka for messaging and MongoDB for data storage. It fetches exchange rates for specific currencies from an external API, produces the data to a Kafka topic, and consumes the data to store it in a MongoDB collection.

## Components

- **Producer (`producer.py`)**: Fetches exchange rates from the [ExchangeRate API](https://api.exchangerate.host/latest) every 60 seconds and sends the data to a Kafka topic named `money-tracker`.
- **Consumer (`consumer.py`)**: Listens to the `money-tracker` Kafka topic, processes incoming messages, and stores the exchange rate data in a MongoDB collection with appropriate indexing.

## Requirements

- Python 3.x
- Kafka server running locally on `localhost:9092`
- MongoDB server running locally on `mongodb://localhost:27017`
- Python packages:
  - kafka-python
  - requests
  - pymongo

## Setup

1. Install Kafka and MongoDB and ensure both services are running locally.
2. Install the required Python packages:
   ```bash
   pip install kafka-python requests pymongo
   ```
3. Run the Kafka producer:
   ```bash
   python producer.py
   ```
4. Run the Kafka consumer:
   ```bash
   python consumer.py
   ```

## How It Works

- The producer fetches exchange rates for USD to YER and SAR currencies from the ExchangeRate API every 60 seconds.
- It sends the fetched data as JSON messages to the Kafka topic `money-tracker`.
- The consumer listens to the `money-tracker` topic, parses the messages, and inserts or updates the exchange rate data in the MongoDB collection `money.money-tracker`.
- The MongoDB collection has indexes on `currency` and `fetched_at` fields for efficient querying.

## Notes

- The API key in the producer script is included but may not be required or valid depending on the API usage policy.
- Adjust the Kafka and MongoDB connection strings if your services are running on different hosts or ports.
- The consumer commits offsets automatically and processes messages from the earliest offset.

## License

This project is provided as-is without any warranty.
