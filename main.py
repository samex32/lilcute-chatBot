import json
from difflib import get_close_matches
from typing import Optional

def load_knowledge_base(file_path: str) -> dict:
    """Loads the knowledge base from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f'Error: The file "{file_path}" was not found.')
        return {"questions": []}
    except json.JSONDecodeError:
        print(f'Error: The file "{file_path}" is not a valid JSON file.')
        return {"questions": []}

def save_knowledge_base(file_path: str, data: dict):
    """Saves the updated knowledge base to a JSON file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)
    except Exception as e:
        print(f'Error saving the knowledge base: {e}')

def find_best_match(user_question: str, questions: list[str]) -> Optional[str]:
    """Finds the closest match to the user's question using fuzzy matching."""
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> Optional[str]:
    """Retrieves the answer to a question from the knowledge base."""
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
    return None

def chat_box():
    """Main function that runs the chatbot."""
    knowledge_base = load_knowledge_base('knowledge_base.json')

    # Check if 'questions' key exists and is a list
    if "questions" not in knowledge_base or not isinstance(knowledge_base["questions"], list):
        print('Error: Knowledge base is missing the "questions" key or it is not properly formatted.')
        return

    while True:
        user_input = input('You: ')

        if user_input.lower() == 'quit':
            break

        best_match = find_best_match(user_input, [q['question'] for q in knowledge_base["questions"]])

        if best_match:
            answer = get_answer_for_question(best_match, knowledge_base)
            print(f'Bot: {answer}')
        else:
            print('Bot: I don\'t know the answer. Can you teach me?')
            new_answer = input('Type the answer or "skip" to skip: ')

            if new_answer.lower() != 'skip':
                knowledge_base['questions'].append({"question": user_input, "answer": new_answer})
                save_knowledge_base('knowledge_base.json', knowledge_base)
                print('Bot: Thank you! I learned the response!')

if __name__ == '__main__':
    chat_box()

