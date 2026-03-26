# sensor-service

A microservice that simulates IoT sensors and sends real-time data to the Kafka broker.

## Features

- Generates temperature and humidity readings
- Supports multiple sensors
- Configurable frequency
- Sends data to Kafka topic `iot.sensors`
- REST API to start/stop simulation

## Endpoints

### Health check

```bash
GET /health
```

### Start simulation

```bash
POST /start
{
"sensors": 3,
"interval": 1.0
}
```

### Stop simulation

```bash
POST /stop
```

## Run locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 9100
```

## Docker

```bash
docker build -t sensor-service .
docker run -p 9100:9100 sensor-service
```
