from given import KNOWN
from llm import ask_llm


def get_response(user_input):

    user_input = user_input.lower().strip()

    response = KNOWN.get(user_input)

    if response:
        return response

    return ask_llm(user_input)


def main():

    print("=" * 50)
    print("Hybrid Chatbot Started")
    print("Type 'kill' to stop")
    print("=" * 50)

    while True:

        user_input = input("\nYou: ")

        if user_input.lower().strip() == "kill":

            print("Bot: Shutdown Successful")
            break

        response = get_response(user_input)

        print("Bot:", response)


if __name__ == "__main__":
    main()