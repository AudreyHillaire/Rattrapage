
from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Liste des questions possibles
questions = {
    "Q1.": "Qu'est-ce que le système de contrôle de version Git?",
    "Python": "Quelles sont les principales caractéristiques du langage de programmation Python?",
    "Linux": "Qu'est-ce que le noyau Linux?"
}

# Liste des réponses possibles
reponses = {
    "Git": "Git est un système de contrôle de version distribué.",
    "Python": "Python est un langage de programmation interprété, dynamique et orienté objet.",
    "Linux": "Le noyau Linux est le cœur du système d'exploitation Linux."
}

# Route pour afficher une question aléatoire
@app.route('/')
def index():
    sujet = random.choice(list(questions.keys()))
    question = questions[sujet]
    return render_template('index.html', sujet=sujet, question=question)

# Route pour vérifier la réponse de l'utilisateur
@app.route('/verifier', methods=['POST'])
def verifier():
    sujet = request.form['sujet']
    reponse_utilisateur = request.form['reponse']
    reponse_attendue = reponses[sujet]

    if reponse_utilisateur == reponse_attendue:
        resultat = "Bravo! Votre réponse est correcte."
    elif reponse_utilisateur in reponse_attendue:
        resultat = "Votre réponse est partiellement correcte."
    else:
        resultat = "Désolé, votre réponse est incorrecte."

    return render_template('resultat.html', resultat=resultat)

if __name__ == '__main__':
    app.run(debug=True)

