#Take database files as well

import json
from difflib import get_close_matches

#loading knowledge from json file

def load_knowledge(file_path:str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_knowledge(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_math(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]

def chat_bot():
    knowledge_base: dict = load_knowledge('knowledge_base.json')

    while True:
        user_input: str = input('You: ')

        if user_input.lower() == 'quit':
            break

        best_match: str | None = find_best_math(user_input, [q["questions"] for q in knowledge_base["questions"]])

        if best_match:
            answer: str = get_answer(best_match, knowledge_base)
            print(f'Bot: {answer}')
        else:
            print('Bot: I don\'t know the answer can you teach me?')
            new_answer: str = input('Type the answer or "skip" to skip: ')

        if new_answer.lower() != 'skip':
               knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
               save_knowledge('knowledge_base.json', knowledge_base)
               print('Bot: Thank you! I learned a new reponse.')


if '_name_' == '_main_':
    chat_bot()
