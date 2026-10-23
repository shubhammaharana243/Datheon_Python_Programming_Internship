import json, re
jsonfile = "Task4/sample_faq.json"

def loadjson():
    with open(jsonfile, "r") as file:
        data = json.load(file)

    return data

def main():
    data = loadjson()

    print()
    print("=" * 40)
    print("       DATHEON AI ASSISTANT")
    print("=" * 40)
    print("  Ask me anything about your internship!")
    print()

    while True:
        user_input = input("You: ").lower().strip()

        if re.search(r"\b(bye|exit|quit)\b", user_input):
            print("Bot: Goodbye! Have a great day!\n")
            break
        elif re.search(r"\b("+"|".join(re.escape(g) for g in data["greetings"])+r"\b)", user_input):
            print("Bot: Hello! Welcome to Datheon Support. \n")

        elif re.search(r"\b(hour|hours|operation hours|timing|opening hours)", user_input):
            print(f"Bot: {data['faqs'][0]['answer']}\n")

        elif re.search(r"\b(project|internship project|submit)\b", user_input):
            print(f"Bot: {data['faqs'][1]['answer']}\n")

        elif re.search(r"\b(certificate|certificates)\b", user_input):
            print(f"Bot: {data['faqs'][2]['answer']}\n")

        else:
            print("Bot: Sorry, I couldn't understand your question. Please try asking differently.\n")


if __name__ == "__main__":
    main()