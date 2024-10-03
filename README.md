# lilcute chatBot
 
This is a Python-based chatbot that leverages a simple knowledge base stored in a JSON file. The chatbot can respond to questions by finding the closest match using fuzzy matching and will prompt the user to provide answers to new questions. The knowledge base dynamically updates as the chatbot learns from user interactions, allowing it to improve its responses over time.

**Features:**
Knowledge Base: Stores questions and answers in a JSON file.
Fuzzy Matching: Utilizes the difflib library to find the closest match to user input.
Self-Learning: If the chatbot doesn't know the answer, it asks the user and updates its knowledge base with new information.
File Handling: Handles potential errors like missing or invalid files when loading the knowledge base.

**How it Works:**
The chatbot loads the knowledge base from a JSON file.
It uses fuzzy matching to find the closest match to the user's input.
If a match is found, the chatbot responds with the stored answer.
If no match is found, the chatbot asks the user for the correct answer and saves it for future use.
