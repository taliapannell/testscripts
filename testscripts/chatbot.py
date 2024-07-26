import random

class Chatbot:
    def __init__(self):
        self.responses = {
            "hello": ["Hi there!", "Hi!", "What's Up!"],
            "how are you": ["I'm doing well, thanks for asking!", "I'm good! How are you?.", "I'm feeling chill."],
            "what's your name": ["My name is Talia."],
            "bye": ["Goodbye!", "See ya later!", "Peace!"],
            "default": ["I didn't quite understand that."]
        }

    def get_response(self, user_input):
        user_input = user_input.lower()

        for intent, response_list in self.responses.items():
            if intent in user_input:
                return random.choice(response_list)

        return self.responses["default"]

if __name__ == "__main__":
    chatbot = Chatbot()
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        response = chatbot.get_response(user_input)
        print("Chatbot:", response)
