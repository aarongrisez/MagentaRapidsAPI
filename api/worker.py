import schedule
import functools
import time
import requests
import random
import os
from models.event import SynthesizedEvent
from models.note import SynthesizedNote
import logging

CHANNELS = list(map(str, [0]))
PITCHES = list(map(str, [120, 220, 320, 420, 520, 620, 720, 820]))
DURATIONS = list(map(str, [3.5]))
TIMES = list(map(str, [0]))
VELOCITIES = list(map(str, [0.25, 0.33, 0.33, 0.25, 0.24, 0.44, 0.33]))

def job(*args, **kwargs):
    note = SynthesizedNote(
        note = random.choice(PITCHES),
        duration = random.choice(DURATIONS),
        time = random.choice(TIMES),
        velocity = random.choice(VELOCITIES),
    )
    event = SynthesizedEvent(
        channel = random.choice(CHANNELS),
        notes = [note]
    )
    r = requests.post(os.environ.get("API_URL") + "push/", json=event.dict())

schedule.every(1.5).seconds.do(lambda: job(3))

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(.0001)