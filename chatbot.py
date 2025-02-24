from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot
chatbot = ChatBot('MyChatBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English corpus
trainer.train("chatterbot.corpus.english")

# Function to interact with the chatbot
def chat():
    print("Hello! I am your chatbot. Type 'exit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.get_response(user_input)
        print(f"Chatbot: {response}")

# Start the chat
if __name__ == "__main__":
    chat()