import re

# Simulate a bot's knowledge base and capabilities.
# This bot is trained on general knowledge and simple pattern matching.

class SimpleBot:
    def __init__(self):
        self.knowledge = {
            "what is the capital of Turkey": "Ankara",
            "what is 2 + 2": "4",
            "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
            "what is the weather like": "I cannot provide real-time weather information."
        }
        self.capabilities = [
            "general knowledge questions",
            "simple arithmetic",
            "telling jokes"
        ]

    def process_request(self, user_input):
        user_input_lower = user_input.lower().strip()

        # Check for direct matches in knowledge base
        if user_input_lower in self.knowledge:
            return self.knowledge[user_input_lower]

        # Simulate a 'legitimate seeming' request that pushes boundaries
        # This request is phrased as a question about a concept the bot might not fully grasp
        # or requires nuanced understanding beyond its training data.
        if "explain the concept of time travel" in user_input_lower:
            return "Time travel is a hypothetical concept. While explored in science fiction, current scientific understanding does not allow for it. My knowledge is limited to established scientific facts."

        # Another example: a request that implies emotional intelligence or subjective opinion
        if "what is the best color" in user_input_lower:
            return "I do not have personal preferences or the ability to determine 'best'. Color preference is subjective."
        
        # A request that requires complex reasoning or real-world interaction
        if "can you book me a flight" in user_input_lower:
            return "I am a text-based AI and cannot perform real-world actions like booking flights."

        # Fallback for unknown requests
        return "I'm sorry, I don't understand that request. I can answer questions about general knowledge, perform simple math, and tell jokes."


if __name__ == "__main__":
    bot = SimpleBot()
    print("Hello! I am a simple bot. Ask me something.")

    while True:
        user_input = input("> ")
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        response = bot.process_request(user_input)
        print(response)
