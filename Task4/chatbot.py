# Import JSON for reading FAQ data and re for pattern matching
import json, re

# Define the path to the FAQ JSON file
jsonfile = "Task4/sample_faq.json"

# Load FAQ data from the JSON file
def loadjson():
    with open(jsonfile, "r") as file:
        data = json.load(file)

    return data

# Run the Datheon AI Assistant chatbot
def main():
    data = loadjson()

    print()
    print("=" * 40)
    print("       DATHEON AI ASSISTANT")
    print("=" * 40)
    print("  Ask me anything about your internship!")
    print()

    # Keep the chatbot running until the user exits
    while True:
        user_input = input("You: ").lower().strip()
        
        # Check whether the user wants to exit the chatbot
        if re.search(r"\b(bye|exit|quit)\b", user_input):
            print("Bot: Goodbye! Have a great day!\n")
            break
        # Match greeting keywords from the JSON data
        elif re.search(r"\b("+"|".join(re.escape(g) for g in data["greetings"])+r"\b)", user_input):
            print("Bot: Hello! Welcome to Datheon Support. \n")

        # Answer questions about working hours
        elif re.search(r"\b(hour|hours|operation hours|timing|opening hours)", user_input):
            print(f"Bot: {data['faqs'][0]['answer']}\n")

        # Answer questions about internship projects and submissions
        elif re.search(r"\b(project|internship project|submit)\b", user_input):
            print(f"Bot: {data['faqs'][1]['answer']}\n")

        # Answer questions about internship certificates
        elif re.search(r"\b(certificate|certificates)\b", user_input):
            print(f"Bot: {data['faqs'][2]['answer']}\n")

        # Handle questions that do not match any predefined pattern
        else:
            print("Bot: Sorry, I couldn't understand your question. Please try asking differently.\n")


# Start the chatbot when the script is executed directly
if __name__ == "__main__":
    main()