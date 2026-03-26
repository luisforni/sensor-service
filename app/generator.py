import random
import time
from typing import Dict


def generate_sensor_data(sensor_id: int) -> Dict:
    """Generate a simulated IoT sensor reading."""
    return {
        "sensor_id": sensor_id,
        "temperature": round(random.uniform(20.0, 30.0), 2),
        "humidity": round(random.uniform(40.0, 60.0), 2),
        "timestamp": time.time()
    }
