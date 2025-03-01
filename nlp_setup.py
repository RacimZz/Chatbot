import nltk
import spacy

# Télécharger les ressources nécessaires pour NLTK
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('punkt_tab')
# Télécharger le modèle de langue pour SpaCy
spacy.cli.download("en_core_web_sm")

print("📌 Configuration NLP terminée !")
