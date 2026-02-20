
import random

class FakeSensors:
    def read_environment(self):
        return {
            "noise_level": random.randint(0, 100),
            "light_level": random.randint(0, 100),
            "touch_detected": random.choice([True, False])
        }