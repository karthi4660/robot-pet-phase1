from brain.mood import Mood
from brain.decision import DecisionEngine
from sensors.fake_sensors import FakeSensors
from actions.movement import Movement
from actions.sound import Sound
import time

mood = Mood()
decision_engine = DecisionEngine()
sensors = FakeSensors()
movement = Movement()
sound = Sound()

while True:
    print("\n--- Robot Status ---")

    env = sensors.read_environment()
    print("Sensor Data:", env)

    # Simulate energy drain
    mood.update_energy(-5)

    current_mood = mood.current_state()
    print("Mood:", current_mood)

    action = decision_engine.decide(current_mood)
    print("Action:", action)

    movement.execute(action)
    sound.make_sound(current_mood)

    time.sleep(3)
