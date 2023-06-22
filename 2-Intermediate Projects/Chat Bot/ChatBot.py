from difflib import get_close_matches

def get_best_match(user_question: str, questions: dict) -> str|None:
    questions: list[str] = [q for q in questions]
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)

    if matches:
        return matches[0]

def chat_bot(knowledge: dict):
    while True:

        user_input: str = input('You: ').lower()
        best_match: str|None = get_best_match(user_input, knowledge  )

        if user_input == 'bye':
            print("Bot: Goodbye!")
            break

        if answer:= knowledge.get(best_match):
            print(f'Bot: {answer}')
        else:
            print("Bot: I don't understand...")

if __name__ == '__main__':
    brain: dict = {'Hello': 'Hi there!',
                   'How are you?': "I'm good thanks!",
                   'What time is it?': 'I\'m not sure',
                   'Bye':' Goodbye!'}

    chat_bot(brain)