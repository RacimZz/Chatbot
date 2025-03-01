import random
import json
import nltk
import spacy
import torch
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import sys
sys.stdout.reconfigure(encoding='utf-8')


# Charger SpaCy et les stopwords
nlp = spacy.load("en_core_web_sm")
stop_words = set(stopwords.words('english'))

# Charger les données des intents
intents = {
    "greetings": {
        "patterns": ["hello", "hi", "hey", "bonjour"],
        "responses": ["Hello!", "Hey there!", "Hi, how can I help you?"]
    },
    "goodbye": {
        "patterns": ["bye", "goodbye", "see you"],
        "responses": ["Goodbye!", "See you later!", "Have a great day!"]
    },
    "thanks": {
        "patterns": ["thanks", "thank you"],
        "responses": ["You're welcome!", "No problem!", "Glad I could help!"]
    }
}

# Fonction de nettoyage du texte
def preprocess_text(text):
    tokens = word_tokenize(text.lower())  # Tokenization
    tokens = [word for word in tokens if word.isalpha() and word not in stop_words]  # Supprimer stopwords & symboles
    return tokens

# Fonction pour obtenir une réponse du chatbot
def get_response(user_input):
    user_tokens = preprocess_text(user_input)
    
    for intent, data in intents.items():
        for pattern in data["patterns"]:
            pattern_tokens = preprocess_text(pattern)
            if set(user_tokens).intersection(set(pattern_tokens)):  # Correspondance basique
                return random.choice(data["responses"])
    
    return "Sorry, I don't understand. Can you rephrase?"

# Boucle pour tester le chatbot
if __name__ == "__main__":
    print("🤖 Chatbot activé ! Tape 'quit' pour arrêter.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        response = get_response(user_input)
        print(f"Bot: {response}")
