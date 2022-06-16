import os
import globals

actuel = "home"


def help():
    return [{"help": "Afficher l'utilisé de chaque commande.",
             "cwd": "Affiche le chemin du dossier actuel",
             "ls": "Affiche le contenu du dossier actuel",
             "mkdir [nom]": "Créé un nouveau dossier nommé comme demandé dans le dossier actuel",
             "cd [chemin]": "Change de dossier actuel"},
            {"help": "h, ?",
             "cwd": "",
             "ls": "listdir, dir",
             "mkdir [nom]": "",
             "cd [chemin]": ""}]


def cwd():
    return "/"+actuel


def ls():
    resultats = os.listdir(actuel)
    res = []
    for x in resultats:
        y = x.count("conv")
        if y == 0:
            bonus = "DOSSIER"
        else:
            bonus = "CONVERSATION"
            x = x.replace("conv", "")
        res.append(x.ljust(69)+" | "+bonus)
    return res


def mkdir(nom):
    if nom.count("conv") == 0:
        try:
            os.mkdir(actuel+globals.separateur+nom)
            return "Travail terminé"
        except Exception as e:
            return str(e)
    else:
        return "Je réserve ce nom"

def cd(chemin):
    global actuel
    for x in chemin.split("/"):
        if x == ".." and actuel.count(globals.separateur) == 0:
            nouveau = ""
            for x in actuel.split(globals.separateur)[:-1]:
                nouveau += globals.separateur + x
            actuel = nouveau
        elif x.ljust(69)+" | DOSSIER" in ls():
            actuel += globals.separateur + x
        elif x == "..":
            return "Déjà à la racine"
        else:
            return "Mauvais nom de dossier"
    return "Travail terminé"