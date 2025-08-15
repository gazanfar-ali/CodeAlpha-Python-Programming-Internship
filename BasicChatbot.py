def chatbot():
    print("🤖 Simple Chatbot — type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()

        if user_input in ["hello", "hi"]:
            print("Bot: Hi there!")
        elif user_input in ["how are you", "how are you doing"]:
            print("Bot: I'm doing great, thanks for asking! 😊")
        elif user_input in ["bye", "goodbye"]:
            print("Bot: Goodbye! Have a nice day!")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

# Run chatbot
chatbot()
