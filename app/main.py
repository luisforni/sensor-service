import asyncio
from fastapi import FastAPI
from pydantic import BaseModel

from .generator import generate_sensor_data
from .sender import send_to_broker

app = FastAPI(
    title="Sensor Service",
    description="Simulates IoT sensors and sends data to Kafka",
    version="0.1.0"
)

running = False


class SimulationConfig(BaseModel):
    sensors: int = 1
    interval: float = 1.0  # seconds


@app.get("/health")
def health():
    return {"status": "ok", "message": "Sensor service running"}


@app.post("/start")
async def start_simulation(config: SimulationConfig):
    global running
    running = True

    async def simulate():
        while running:
            for sensor_id in range(1, config.sensors + 1):
                data = generate_sensor_data(sensor_id)
                send_to_broker(data)
            await asyncio.sleep(config.interval)

    asyncio.create_task(simulate())
    return {"status": "started", "config": config}


@app.post("/stop")
def stop_simulation():
    global running
    running = False
    return {"status": "stopped"}
