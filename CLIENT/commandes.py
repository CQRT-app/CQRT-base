# ---------- IMPORATIONS ----------
import json
import os
import random
from passlib.hash import phpass
import secrets
import shutil

from bytes import bytestring
import globals
import connexions

# ---------- VARIABLES GLOBALES ----------
__author__ = "reza0310"
actuel = "home"


# ---------- FONCTIONS UTILES ----------
def identifile_moins(filename):
    if filename.count("[") == 1:
        if filename.count(".json") == 1:
            y = filename.split("]")
            bonus = y[0][1:]
            x = filename.replace(f"[{bonus}]", "").replace(".json", "")
            return x, bonus
        else:
            return filename, "CONVERSATION"
    else:
        return filename, "DOSSIER"


def identifile_plus(filename):
    for x in os.listdir(actuel):
        if x == filename or x == "[CONVERSATION]"+filename or x.count("]") == 1 and x.split("]")[1][:-5] == filename:
            return x, os.path.isdir(actuel+globals.separateur+x)


def pprint(x):
    globals.jeu.commandeur.ecrire(x)
    print(x)


def bite(x):
    res = bytestring(x)
    if res.contenu[0] == "1":
        res.signed = True
    else:
        res.contenu = res.contenu[1:]
    return res


# ---------- FONCTIONS DE COMMANDES ----------
def help():
    return [{"help": "Afficher l'utilisé de chaque commande.",
             "cwd": "Affiche le chemin du dossier actuel",
             "ls": "Affiche le contenu du dossier actuel",
             "mkdir [nom]": "Créé un nouveau dossier nommé comme demandé dans le dossier actuel",
             "cd [chemin]": "Change de dossier actuel",
             "mkr [nom]": "Créé un porte clef, une liste de contacts",
             "rm [nom]": "Supprime un fichier, dossier ou conversation.",
             "mv [nom] [destination]": "Déplace un fichier, dossier ou conversation du dossier actuel vers le chemin absolu 'destination'",
             "lkr [nom]": "Lister les contacts d'un porte-clef",
             "rsa_gen_keys [nom]": "Générer une paire de clefs",
             "client_connect [account/message] [ip]:[port]": "Connecter son client de compte ou de message a un serveur",
             "make_account [pseudo] [clef]": "Se créer un compte avec le pseudo [pseudo] associé à la clef [clef] sur le serveur de comptes actuel",
             "list_accounts [pseudo]": "Lister tout les comptes ayant pour pseudo [pseudo] sur le serveur de comptes actuel",
             "get_account [id] [porte-clef]": "Ajoute le compte d'identifiant [id] de votre serveur à votre porte-clefs [porte-clef]",
             "reset": "SUPPRIME TOUT",
             "send_message [compte] [porteclefs] [pseudo] [titre] [message]": "Envoie le message [message] chiffré au compte [pseudo] du porte-clefs [porteclefs] avec le titre [titre].",
             "pull_messages [compte]": "Récupérera tout les messages adressés à votre compte sur le serveur non-encore dans le dossier",
             "read_message [compte] [message]": "Lira un fichier de message avec le compte [compte]",
             "credits": "Affiche les credits"},
            {"help": "h, ?",
             "cwd": "",
             "ls": "listdir, dir",
             "mkdir [nom]": "",
             "cd [chemin]": "",
             "mkr [nom]": "",
             "rm [nom]": "",
             "mv [nom] [destination]": "",
             "lkr [nom]": "",
             "rsa_gen_keys [nom]": "rgk",
             "client_connect [account/message] [ip]:[port]": "",
             "make_account [pseudo] [clef]": "",
             "list_accounts [pseudo]": "",
             "get_account [id] [porte-clef]": "",
             "reset": "",
             "send_message [compte] [porteclefs] [pseudo] [titre] [message]": "",
             "pull_messages [compte]": "",
             "read_message [compte] [message]": "",
             "credits": ""}]


def cwd(dontcrash):
    return "/"+actuel


def ls():
    resultats = os.listdir(actuel)
    res = []
    for x in resultats:
        x, bonus = identifile_moins(x)
        res.append(x.ljust(69)+" | "+bonus)
    return res


def mkdir(nom):
    if nom.count("[CONVERSATION]") == 0:
        try:
            os.mkdir(actuel+globals.separateur+nom)
            return "."
        except Exception as e:
            return str(e)
    else:
        return "Je réserve ce nom"


def cd(chemin):
    global actuel
    for x in chemin.split("/"):
        if x == ".." and actuel.count(globals.separateur) != 0:
            nouveau = ""
            for x in actuel.split(globals.separateur)[:-1]:
                nouveau += globals.separateur + x
            actuel = nouveau[1:]
        elif x.ljust(69)+" | DOSSIER" in ls():
            actuel += globals.separateur + x
        elif x == "..":
            return "Déjà à la racine"
        else:
            return "Mauvais nom de dossier"
    return "."


def mkr(nom):
    f = open(actuel+globals.separateur+"[PORTECLEF]"+nom+".json", "w+")
    json.dump({}, f)
    f.close()
    return "."


def rm(nom):
    nom, dir = identifile_plus(nom)
    nom = actuel+globals.separateur+nom
    try:
        if dir:
            shutil.rmtree(nom)
        else:
            os.remove(nom)
        return "."
    except Exception as e:
        return "Erreur: "+str(e)


def mv(nom, destination):
    nom, dir = identifile_plus(nom)
    nom = actuel+globals.separateur+nom
    try:
        shutil.move(nom, "home"+globals.separateur+destination)
        return "."
    except Exception as e:
        return "Erreur: "+str(e)


def lkr(nom):
    f = open(actuel+globals.separateur+identifile_plus(nom)[0], "r")
    data = json.load(f)
    f.close()
    return ["-"+x for x in data.keys()]


def credits():
    return ["Idée de base:",
            "рысь корп#8628",
            "",
            "Membres de l'équipe:",
            "-рысь корп#8628",
            "-viktor#7755",
            "-TBZ_Jules785#5878",
            "-Mazalex#7173",
            "-reza0310#0310",
            "",
            "Planification technique:",
            "-reza0310#0310",
            "",
            "Implémentation:",
            "-reza0310#0310",
            "",
            "Design interface:",
            "C'est juste des lignes de commande...",
            "",
            "Implémentation interface:",
            "-reza0310#0310",
            "",
            "Bibliographie:",
            "-https://passlib.readthedocs.io/en/stable/lib/passlib.hash.phpass.html",
            "-https://fr.wikipedia.org/wiki/Algorithme_d'Euclide_étendu",
            "-https://en.wikipedia.org/wiki/Primality_test",
            "-https://docs.python.org/3/library/secrets.html#module-secrets",
            "-https://fr.wikipedia.org/wiki/Chiffrement_RSA"]


def reset():
    shutil.rmtree("home")
    os.mkdir("home")
    return "."


# ---------- FONCTIONS DE CONNEXION ----------
def client_connect(type, iport):
    ip, port = iport.split(":")
    port = int(port)
    if type == "account":
        globals.account_client.connect((ip, port))
        globals.account_ip = ip
        globals.account_port = port
    else:
        globals.message_client.connect((ip, port))
        globals.message_ip = ip
    return "."


def make_account(pseudo, clef):
    f = open(actuel+globals.separateur+f"[CLEFS]{clef}.json", "r")
    key = json.load(f)
    f.close()
    infos = connexions.echanger(globals.account_client, f"makeaccount\0{pseudo}\0{key['n']}\0{key['e']}")
    if infos[:7] == "Succès!":
        f = open(actuel+globals.separateur+"[COMPTE]"+pseudo+"@"+globals.account_ip+".json", "w+")
        json.dump({"id": infos[-3:], "serveur": globals.account_ip, "clef": {"n": key["n"], "e": key["e"], "d": key["d"]}}, f)
        f.close()
    return infos


def list_accounts(pseudo):
    return ["Identifiants correspondants à ce nom sur votre serveur de comptes actuel:"]+connexions.echanger(globals.account_client, f"listaccounts\0{pseudo}").split("\0")


def get_account(id, porteclef):
    path = actuel+globals.separateur+identifile_plus(porteclef)[0]

    with open(path, "r") as f:
        data = json.load(f)

    pseudo, n, e = connexions.echanger(globals.account_client, f"get\0{id}").split("\0")
    data[pseudo] = {"serveur": globals.account_ip, "id": id, "n": n, "e": e}

    with open(path, "w") as f:
        json.dump(data, f)
    return "."


def send_message(compte, porteclef, autre, titre, message):
    with open(actuel+globals.separateur+identifile_plus(compte)[0], "r") as f:
        datmoi = json.load(f)
    with open(actuel+globals.separateur+identifile_plus(porteclef)[0], "r") as f:
        datautre = json.load(f)[autre]

    hash = bytestring(phpass.hash(message))
    message = bytestring(message)
    clef_session = bytestring(secrets.randbits(len(message)))
    signature = bytestring(phpass.hash("Ceci est une signature"))

    datautre["n"] = bite(datautre["n"])
    datautre["e"] = bite(datautre["e"])
    datmoi["clef"]["n"] = bite(datmoi["clef"]["n"])
    datmoi["clef"]["d"] = bite(datmoi["clef"]["d"])

    message_chiffre = message.cypher(clef_session).contenu
    clef_chiffree = bytestring(rsa_cypher(int(clef_session), int(datautre["n"]), int(datautre["e"]))).contenu
    integritee_chiffree = bytestring(rsa_cypher(int(hash), int(datautre["n"]), int(datautre["e"]))).contenu
    signature_chiffree = bytestring(rsa_cypher(int(signature), int(datmoi["clef"]["n"]), int(datmoi["clef"]["d"]))).contenu

    id = connexions.echanger(globals.message_client, "make\0" +
                        f"{datautre['id']}\0{datautre['serveur']}\0" +
                        f"{datmoi['id']}\0{datmoi['serveur']}\0" +
                        f"{titre}")
    connexions.echanger(globals.message_client, f"push\0{id}\0{datautre['id']}\0{datautre['serveur']}\0{message_chiffre}\0{clef_chiffree}\0{integritee_chiffree}\0{signature_chiffree}")
    return "."


def pull_messages(compte):
    # [MESSAGE]id_ip.json
    with open(actuel+globals.separateur+identifile_plus(compte)[0], "r") as f:
        datmoi = json.load(f)
    ip = globals.message_ip

    a_pull = connexions.echanger(globals.message_client, f"pull\0{datmoi['id']}@{datmoi['serveur']}").split("\0")
    pulled = os.listdir(actuel)
    for x in a_pull:
        id = x
        if not("[MESSAGE]"+id+"_"+ip+".json" in pulled):
            with open(actuel+globals.separateur+"[MESSAGE]"+id+"_"+ip+".json", "w+") as f:
                getter = connexions.echanger(globals.message_client, f"get\0{id}").split("\0")
                json.dump({"sender": {"id": getter[0], "serveur": getter[1]},
                           "heure": getter[2], "date": getter[3], "titre": getter[4],
                           "message_chiffre": getter[5], "clef_chiffree": getter[6],
                           "integritee_chiffree": getter[7], "signature_chiffree": getter[8]}, f)
    return "."


def read_message(compte, message):
    # Extraction données
    with open(actuel+globals.separateur+identifile_plus(compte)[0], "r") as f:
        datmoi = json.load(f)
    with open(actuel+globals.separateur+identifile_plus(message)[0], "r") as f:
        message_data = json.load(f)
    if message_data["sender"]["serveur"] != globals.account_ip:
        return f"Veuillez vous connecter au serveur de comptes {message_data['sender']['serveur']} pour lire ce message."
    sender_pseudo, sender_n, sender_e = connexions.echanger(globals.account_client, f"get\0{message_data['sender']['id']}").split("\0")

    # Méta-informations
    globals.jeu.commandeur.ecrire(f"Message envoyé par {sender_pseudo} le {message_data['date']} à {message_data['heure']}:")

    # Signature
    sender_n = bite(sender_n)
    sender_e = bite(sender_e)

    signature = str(bytestring(rsa_cypher(int(message_data["signature_chiffree"], 2), int(sender_n), int(sender_e))))
    globals.jeu.commandeur.ecrire(f"Indicateur de signature (False => l'envoyeur est un imposteur et non pas celui qu'il prétend être): {phpass.verify('Ceci est une signature', signature)}")

    # Récupération clef symmétrique
    datmoi["clef"]["n"] = bite(datmoi["clef"]["n"])
    datmoi["clef"]["d"] = bite(datmoi["clef"]["d"])

    clef = bytestring(rsa_cypher(int(message_data["clef_chiffree"], 2), int(datmoi["clef"]["n"]), int(datmoi["clef"]["d"])))

    # Récupération hash msg
    hash = str(bytestring(rsa_cypher(int(message_data["integritee_chiffree"], 2), int(datmoi["clef"]["n"]), int(datmoi["clef"]["d"]))))
    print(hash)

    # Récupération msg
    message = str(bytestring(message_data["message_chiffre"]).cypher(clef))
    print(message)
    globals.jeu.commandeur.ecrire(f"Indicateur d'intégrité (False => le message a été truqué): {phpass.verify(message, hash)}")

    globals.jeu.commandeur.ecrire(f'"{message_data["titre"]}":')
    return message


# ---------- RSA ----------
def miller_rabin_prime(n):
    # Source: https://gist.github.com/tbenjis/c8a8cf8c4bf6272f2be0
    num_trials = 5  # number of bases to test
    assert n >= 2  # make sure n >= 2 else throw error
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n - 1
    while True:
        quotient, remainder = divmod(d, 2)  # here we get the quotient and the remainder
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert (2 ** s * d == n - 1)  # make sure 2**s*d = n-1
    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:  # defined as pow(x, y) % z = 1
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                return False
        return True  # n is definitely composite
    for i in range(num_trials):
        # try several trials to check for composite
        a = random.randrange(2, n)
        if try_composite(a):
            return False
    return True  # no base tested showed n as composite


def bezout_euclide_etendu(rn, rn1, un=1, un1=0, vn=0, vn1=1):
    q = rn // rn1
    rn2 = rn - q * rn1
    while rn2 != 0:
        (rn, rn1, un, un1, vn, vn1) = (rn1, rn2, un1, (un - q * un1), vn1, (vn - q * vn1))
        q = rn // rn1
        rn2 = rn - q * rn1
    return rn1, un1, vn1


def rsa_gen_keys(nom):

    pprint(f"Début de la génération des clefs {nom}")

    p = secrets.randbits(1024)

    pprint("Recherche de p")

    while not(miller_rabin_prime(p)):
        p = secrets.randbits(1024)

    pprint("p trouvé")

    q = secrets.randbits(1024)

    pprint("Recherche de q")

    while not(miller_rabin_prime(q)):
        q = secrets.randbits(1024)

    pprint("q trouvé")

    n = bite(bytestring(p*q).signed_version())
    indic = (p-1) * (q-1)
    e = secrets.randbits(3072)

    pprint("Recherche de e")

    while not(bezout_euclide_etendu(e, indic)[0] == 1):
        e = secrets.randbits(3072)

    pprint("e trouvé")

    d = bite(bytestring(bezout_euclide_etendu(e, indic)[1]).signed_version())
    e = bite(bytestring(e).signed_version())

    pprint("d calculé")
    pprint("test des clefs")

    x = secrets.randbits(10)
    if pow(pow(x, int(e), int(n)), int(d), int(n)) == pow(pow(x, int(d), int(n)), int(e), int(n)) == x:
        pprint("test validé")
        with open(actuel+globals.separateur+f"[CLEFS]{nom}.json", "w+") as file:
            json.dump({"n": n.signed_version(), "e": e.signed_version(), "d": d.signed_version()}, file)
        return "."
    else:
        pprint("test échoué")
        return rsa_gen_keys(nom)


def rsa_cypher(message, n, ed):
    # Utiliser n et e pour public, n et d pour privé
    return pow(message, ed, n)

# ---------- FIN ----------
