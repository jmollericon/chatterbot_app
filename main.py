from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot
chatbot = ChatBot("Jorge's bot")

# Training the chatbot
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)

# Get a response
response = chatbot.get_response("Good morning!")
print(response)
