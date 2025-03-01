# Chatbot IA avec Google Gemini 1.5 et Flask

## Description
Ce projet est un chatbot intelligent utilisant Google Gemini 1.5 pour générer des réponses aux messages des utilisateurs. Il est développé en Python avec Flask pour l'interface web et gère uniquement l'anglais. Si un message est en français, le chatbot répondra qu'il ne supporte que l'anglais.

## Fonctionnalités
- Détection automatique de la langue (anglais/français)
- Génération de réponses en utilisant l'API Google Gemini 1.5
- Interface web simple avec Flask
- Protection de la clé API en utilisant des variables d'environnement

## Prérequis
- Python 3.8+
- Un compte Google Cloud avec accès à l'API Gemini 1.5
- Un fichier `.env` contenant la clé API sous la forme :

```sh
GEMINI_API_KEY="votre_clé_api"
```

## Installation
1. Clonez ce dépôt :
   ```sh
   git clone https://github.com/Chatbot/chatbot-gemini.git
   cd chatbot-gemini
   ```
2. Créez un environnement virtuel et activez-le :
   ```sh
   python -m venv venv
   source venv/bin/activate  # Sur Windows : venv\Scripts\activate
   ```
3. Installez les dépendances :
   ```sh
   pip install -r requirements.txt
   ```
4. Créez un fichier `.env` à la racine et ajoutez votre clé API Google Gemini :
   ```sh
   echo "GEMINI_API_KEY=votre_clé_api" > .env
   ```

## Utilisation
1. Lancez le serveur Flask :
   ```sh
   python app.py
   ```
2. Ouvrez votre navigateur et accédez à `http://127.0.0.1:5000`
3. Commencez à discuter avec le chatbot !

## Déploiement
- Vous pouvez déployer ce projet sur un service cloud comme **Render, Heroku, ou Google Cloud Run**.
- Assurez-vous de configurer correctement les variables d'environnement pour la clé API.

## Améliorations futures
- Ajout d'une meilleure gestion des erreurs
- Interface utilisateur plus avancée
- Support d'autres langues via traduction automatique

## Auteurs
- **Racim ZENATI**

## Licence
Ce projet est sous licence MIT. Vous êtes libre de le modifier et de le distribuer avec attribution.


