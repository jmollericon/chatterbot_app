from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create the bot and setting the storage adapter and specify logic adapters
bot = ChatBot(
    "Jorge's bot",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    database_uri='sqlite:///database.sqlite3'
)

# Print an example of getting one math based response
response = bot.get_response('What is 4 + 9?')
print(response)

# Print an example of getting one time based response
response = bot.get_response('What time is it?')
print(response)

# Gettion a response from bot
while True:
    try:
        bot_input = bot.get_response(input('>>>'))
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break

