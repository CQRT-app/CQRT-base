import os
import globals

actuel = "home"


def help():
    return [{"help": "Afficher l'utilisé de chaque commande.",
             "cwd": "Affiche le chemin du dossier actuel",
             "ls": "Affiche le contenu du dossier actuel",
             "mkdir [nom]": "Créé un nouveau dossier nommé comme demandé dans le dossier actuel",
             "rmdir [nom]": "Supprime le dossier nommé comme demandé dans le dossier actuel",
             "cd [chemin]": "Change de dossier actuel",
             "mkr [nom]": "Créé un porte clef, une liste de contacts",
             "rkr [nom]": "Supprime un porte clef, une liste de contacts",
             "lkr": "Lister les porte clefs, les listes de contacts"},
            {"help": "h, ?",
             "cwd": "",
             "ls": "listdir, dir",
             "mkdir [nom]": "",
             "rmdir [nom]": "",
             "cd [chemin]": "",
             "mkr [nom]": "",
             "rkr [nom]": "",
             "lkr": ""}]


def cwd(dontcrash):
    return "/"+actuel


def ls():
    resultats = os.listdir(actuel)
    res = []
    for x in resultats:
        if x.count("[PORTECLEF]") == 1:
            bonus = "PORTECLEF"
            x = x.replace("[PORTECLEF]", "").replace(".json", "")
        elif x.count("[CONVERSATION]") == 1:
            bonus = "CONVERSATION"
            x = x.replace("[CONVERSATION]", "").replace(".json", "")
        else:
            bonus = "DOSSIER"
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


def rmdir(nom):
    if nom.count("conv") == 0:
        try:
            os.remove(actuel+globals.separateur+nom)
            return "Travail terminé"
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
            actuel = nouveau
        elif x.ljust(69)+" | DOSSIER" in ls():
            actuel += globals.separateur + x
        elif x == "..":
            return "Déjà à la racine"
        else:
            return "Mauvais nom de dossier"
    return "Travail terminé"


def mkr(nom):
    f = open("home/[PORTECLEF]"+nom+".json", "w+")
    f.close()
    return "Travail terminé"


def rkr(nom):
    try:
        os.remove("home/[PORTECLEF]"+nom+".json")
        return "Travail terminé"
    except:
        return "Porte clef inexistant"

def lkr():
    res = []
    for x in os.listdir("home"):
        if x.count("[PORTECLEF]") == 1:
            res.append(x.replace("[PORTECLEF]", "").replace(".json", ""))
    return res


"""
Infos:
1. The sender creates a message.
2. The sending OpenPGP generates a random number to be used as a
session key for this message only.
3. The session key is encrypted using each recipient’s public key.
These "encrypted session keys" start the message.
4. The sending OpenPGP encrypts the message using the session key,
which forms the remainder of the message. Note that the message
is also usually compressed.
5. The receiving OpenPGP decrypts the session key using the
recipient’s private key.
6. The receiving OpenPGP decrypts the message using the session key.
If the message was compressed, it will be decompressed.


First, a signature is generated for the message
and attached to the message. Then the message plus signature is
encrypted using a symmetric session key. Finally, the session key is
encrypted using public-key encryption and prefixed to the encrypted
block.

1. The sender creates a message.
2. The sending software generates a hash code of the message.
3. The sending software generates a signature from the hash code
using the sender’s private key.
4. The binary signature is attached to the message.
5. The receiving software keeps a copy of the message signature.
6. The receiving software generates a new hash code for the received
message and verifies it using the message’s signature. If the
verification is successful, the message is accepted as authentic.

OpenPGP implementations SHOULD compress the message after applying
the signature but before encryption.

"""