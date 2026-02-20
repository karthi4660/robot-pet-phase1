class DecisionEngine:
    def decide(self, mood_state):
        if mood_state == "tired":
            return "sleep"
        elif mood_state == "sad":
            return "seek_attention"
        elif mood_state == "excited":
            return "play"
        else:
            return "idle"
