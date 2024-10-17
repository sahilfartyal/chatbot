import nltk
from nltk.chat.util import Chat, reflections

# Define some patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"my name is (.*)",
        ["Hello %1, nice to meet you!"]
    ],
    [
        r"how are you ?",
        ["I'm doing good, how about you?"]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "No problem"]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that!", "Great! How can I assist you today?"]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created using NLTK.", "You can call me ChatBot!"]
    ],
    [
        r"quit",
        ["Bye! Have a nice day."]
    ],
]

# Reflections are a dictionary used to convert input pronouns to appropriate responses
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

# Create Chat object with pairs and reflections
chatbot = Chat(pairs, reflections)

# Start the chatbot
def chatbot_start():
    print("Hi! I'm your chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Bye! Have a great day.")
            break
        response = chatbot.respond(user_input)
        if response:
            print(f"Chatbot: {response}")
        else:
            print("Chatbot: I didn't understand that.")

# Run the chatbot
if __name__ == "__main__":
    chatbot_start()
