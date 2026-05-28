import random
import time
from app.services.store import events

types = ["signup", "purchase", "payment", "error", "login"]

while True:
    event = {
        "type": random.choice(types),
        "user": random.randint(1000, 9999),
        "value": round(random.uniform(10, 500), 2),
        "region": random.choice(["US", "EU", "ASIA"]),
        "time": time.strftime("%H:%M:%S")
    }

    events.insert(0, event)
    if len(events) > 100:
        events.pop()

    print(event)