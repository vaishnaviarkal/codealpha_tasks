def get_chatbot_response(user_input):
    # Normalize input to lowercase so 'Hello' and 'hello' both work
    user_input = user_input.lower()

    # Rule-based logic using if-elif-else
    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I help you today?"
    
    elif "how are you" in user_input:
        return "I'm doing great, thanks for asking! How about you?"
    
    elif "your name" in user_input:
        return "I'm a simple Python chatbot. You can call me PyBot!"
    
    elif "weather" in user_input:
        return "I don't have a window, but I hope it's sunny where you are!"
    
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a wonderful day!"
    
    else:
        return "I'm sorry, I don't understand that yet. Could you try asking something else?"

def start_chat():
    print("--- Welcome to the Rule-Based Chatbot ---")
    print("(Type 'bye' to exit the conversation)")
    
    # Loop to keep the chat active
    while True:
        user_message = input("\nYou: ")
        
        # Get the response from our function
        response = get_chatbot_response(user_message)
        
        print(f"Chatbot: {response}")
        
        # Break the loop if the user says goodbye
        if "bye" in user_message.lower():
            break

if __name__ == "__main__":
    start_chat()