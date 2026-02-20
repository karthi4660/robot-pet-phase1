class Sound:
    def make_sound(self, mood_state):
        if mood_state == "sad":
            print("🔊 Beep... (sad tone)")
        elif mood_state == "excited":
            print("🔊 Beep Beep! (excited tone)")
        else:
            print("🔊 Beep.")
