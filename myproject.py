
from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Liste des questions possibles
questions = {
    "Q1.": "Comment afficher le chemin du répertoire de travail en Linux ?",
    "Q2.": "Comment exécuter les actions de l’administrateur, demander un mot de passe en Linux ?",
    "Q3.": "Comment supprimer les commits d'une branche en Git ?",
    "Q4.": "Comment ignorer les fichiers engagés dans votre projet et visibles par d’autres en Git ?",
    "Q5.": "Comment créer un dépôt Git à partir d’un dossier existant ?",
    "Q6.": "Comment enregistrer quelques modifications pour le prochain commit en Git ?",
    "Q7.": "Comment ajouter des modifications à l’historique Git local ?",
    "Q8.": "Comment envoyer des objets Git vers un dépôt distant ?",
    "Q9.": "Comment générer des fichiers et répertoires temporaires en Python ?",
    "Q10.": "Comment générer des nombres pseudo-aléatoires en python ?",
    "Q11.": "Comment mesurer le temps d’exécution de petits fragments de code en python ?",
    "Q12.": "Comment créer des fonctions créant des itérateurs pour une boucle efficace en Python ?",
    "Q13.": "Comment télécharger des objets Git depuis un dépôt distant ?",
    "Q14.": "Comment passer une sortie de commande en entrée pour la suivante en Linux ?",
    "Q15.": "Comment télécharger un fichier à partir d’une URL en Linux ?",
    "Q16.": "Comment sélectionner des parties de fichiers qui correspondent à un modèle dans Linux ?",
    "Q17.": "Comment analyser et transformer les données texte en Linux ?",
    "Q18.": "Comment récupérer ET fusionner depuis un dépôt distant dans Git ?",
    "Q19.": "Comment fusionner une branche avec deux commandes différentes dans Git ?",
    "Q20.": "Comment exécuter la commande précédente en Linux ?"
}

# Liste des réponses possibles
reponses = {
    "Q1.": "pwd print working directory",
    "Q2.": "sudo <command> substitute user do",
    "Q3.": "git reset <commit>",
    "Q4.": ".gitignore",
    "Q5.": "git init",
    "Q6.": "git add",
    "Q7.": "git commit",
    "Q8.": "git push",
    "Q9.": "tempfile",
    "Q10.": "random",
    "Q11.": "timeit",
    "Q12.": "itertools",
    "Q13.": "git fetch",
    "Q14.": "pipeline",
    "Q15.": "wget World Wide Web GET",
    "Q16.": "grep Global Regular Expressions Print",
    "Q17.": "sed Stream EDitor",
    "Q18.": "git pull",
    "Q19.": "git merge et git rebase",
    "Q20.": "!!"
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

