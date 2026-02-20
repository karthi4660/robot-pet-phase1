
class Movement:
    def execute(self, action):
        if action == "sleep":
            print("🤖 Robot is going to sleep...")
        elif action == "play":
            print("🤖 Robot is playing happily!")
        elif action == "seek_attention":
            print("🤖 Robot is seeking attention...")
        else:
            print("🤖 Robot is idling...")