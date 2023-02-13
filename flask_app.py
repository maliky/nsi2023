
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def accueil():
    date = datetime.datetime.now()
    heure = date.hour
    minute = date.minute
    seconde = date.second

    nb_pieces = 100
    taille_puzzle = nb_pieces ** (1/2)
    mes_images = []

    for cpt in range(nb_pieces):
        nom_image =  f"Images/Puzzle/piece-puzzle-{cpt}.png"
        no_ligne = int(cpt // taille_puzzle)
        no_col = int(cpt % taille_puzzle)

        info_image = (nom_image, no_ligne, no_col)
        mes_images.append(info_image)



    if request.method == "GET":
        reponse = "Bienvenue ! "

    if request.method == "POST":
        choix = request.form["choix"]
        nom = request.form["nom"]
        reponse = ""
        if choix == "oui":
            reponse = f"{nom} avez bon goût merci"
        else:
            reponse = f"Enfin, {nom} cela ne se discute pas !"

        date_naissance = datetime.datetime.strptime(request.form["naiss"], "%Y-%m-%d")
        date_actuelle = datetime.datetime.now()
        ans18 = datetime.timedelta(days=int(18 * 365.25))

        if ans18 < (date_actuelle - date_naissance):
            return render_template("trop_vieux.html")

    return render_template(
        "accueil.html",
        h=heure,
        m=minute,
        s=seconde,
        noms_images=mes_images,
        reponse=reponse,
    )



@app.route('/apropos')
def apropos():
    ma_famille = [('Ali', 'le fils'), ('Alice', 'la fille'), ('Chen', 'le père'),\
    ('Isis', 'la mère'), ('Eve','la grand mère'), ('Hotep','Le grand père')]
    return render_template("apropos.html", famille=ma_famille)


