# ---------- IMPORATIONS ----------
import os
import random

import globals
from passlib.hash import phpass

# ---------- VARIABLES GLOBALES ----------
__author__ = "reza0310"
actuel = "home"


# ---------- FONCTIONS DE MANIPULATION ----------
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


def credits():
    return """BASÉ SUR OPENPGP

Idée de base:
рысь корп#8628

Membres de l'équipe:
-рысь корп#8628
-viktor#7755
-TBZ_Jules785#5878
-Mazalex#7173
-reza0310#0310

Planification technique:
-reza0310#0310

Implémentation:
-reza0310#0310

Design interface:
C'est juste des lignes de commande...

Implémentation interface:
-reza0310#0310

Bibliographie:
-RFC 4880 (OpenPGP Message Format)
-RFC 2119 (Key words for use in RFCs to Indicate Requirement Levels)
-https://passlib.readthedocs.io/en/stable/lib/passlib.hash.phpass.html"""


# ---------- S2K (RFC 4880 PAGE 10) ----------
def S2K(donnees, id, taille, c=10):
    if id == 0:
        return str(etendre_clef(donnees, taille)).zfill(taille+8)
    else:
        caracteres_valides = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                              "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                              "s", "t", "u", "v", "w", "x", "y", "z",
                              "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                              "S", "T", "U", "V", "W", "X", "Y", "Z"]
        sel = ""
        for i in range(8):
            sel += random.choice(caracteres_valides)

        if id == 1:
            return str(1 << taille | etendre_clef(donnees, taille, sel=sel)).zfill(taille+8) + string_to_bytestring(sel)
        elif id == 3:
            return str(3 << taille | etendre_clef(donnees, taille, sel=sel, fois=c-1)).zfill(taille+8) + string_to_bytestring(sel) + int_to_bytestring((16 + (c & 15)) >> ((c << 4) + 6))


def etendre_clef(donnees, taille, sel=None, fois=0):
    i = 1
    hash = nettoyer_hash(donnees, sel=sel)
    for i in range(fois):
        hash = nettoyer_hash(hash, sel=sel)
    res = hash
    # Augmentation de la taille
    while res.bit_length() < taille:
        for x in range(i):
            res <<= 8  # Le padding mentionné dans la RFC
        res <<= 176  # Concatenation binaire par décalage et ou logique
        res |= hash
        i += 1
    # Réduction de la taille
    res >>= res.bit_length()-taille
    return res


def nettoyer_hash(texte, sel):
    if sel is None:
        hash = phpass.hash(texte.encode("utf-8"))
    else:
        hash = phpass.hash(texte.encode("utf-8"), salt=sel)

    # Découpe de la variable hash par caractères:
    # 1-3: Préfixe
    # 4: Nombre de rounds
    # 5 - 12: Sel
    # 13 - 34: Checksum
    return int(string_to_bytestring(hash[12:]), 2)


# ---------- PACKETS (RFC 4880 PAGE 13) ----------


def packet_header(tag, data_size):
    # data_size est un nombre d'octets pas de bits
    partial = False
    header = "11"
    header += tag  # 6 bits
    if data_size < 192:
        # Premier octet entre 0 et 191
        header += int_to_bytestring(data_size).zfill(8)
    elif data_size < 8384:
        # Premier octet entre 192 et 223
        octet1 = data_size >> 8
        octet2 = data_size - (octet1 << 8)
        header += int_to_bytestring(((octet1 - 192) << 8) + (octet2) + 192).zfill(16)
    elif data_size < 4294967296:
        # Premier octet = 255
        octets = []
        for i in range(5):
            octets.append((data_size >> (8*i)) - (data_size >> (8*(i+1))))
        header += "11111111" + int_to_bytestring((octets[1] << 24) | (octets[2] << 16) | (octets[3] << 8) | octets[4]).zfill(32)
    else:
        # Premier octet entre 224 et 254
        header += int_to_bytestring(1 << ((data_size >> (data_size.bit_length() - 8)) & 0x1F)).zfill(8)
    return header, partial


# ---------- FIN ----------


# Commencer les fichiers de clefs privées par 11111111 01010000 00000011 si chiffré et 0 sinon
# These are followed by an Initial Vector of the same length as the block size of the cipher for the decryption of the secret values, if they are encrypted, and then the secret-key values themselves.

# Packets: 11XXXXXX

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