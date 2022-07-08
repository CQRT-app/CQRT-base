__author__ = "reza0310"

import commandes
import globals

class Commandeur():

    def __init__(self):
        self.nbre_lignes = 44
        self.historique = [""] * self.nbre_lignes
        self.centre_historique = [False] * self.nbre_lignes
        self.commandes_simples = {"cwd": commandes.cwd,
                                  "mkdir": commandes.mkdir,
                                  "rmdir": commandes.rmdir,
                                  "cd": commandes.cd,
                                  "mkr": commandes.mkr,
                                  "rkr": commandes.rkr,
                                  "rsa_gen_keys": commandes.rsa_gen_keys,
                                  "rgk": commandes.rsa_gen_keys}

    def ecrire(self, ligne, centrer=False):
        self.historique.pop(0)
        self.historique.append(ligne)
        self.centre_historique.pop(0)
        self.centre_historique.append(centrer)

    def execute(self, commande):
        self.ecrire("")
        self.ecrire("> "+commande)
        c = commande.split(" ")
        arguments = c[1:]
        commande = c[0]
        if commande in self.commandes_simples:
            self.ecrire("")
            self.ecrire(self.commandes_simples[commande](*arguments))
        elif commande == "help" or commande == "h" or commande == "?":
            res = commandes.help()
            for x in res[0].keys():
                self.ecrire("")
                self.ecrire(x.upper()+": "+res[0][x])
                if res[1][x] != "":
                    self.ecrire("ALIASES: "+res[1][x])
        elif commande == "ls" or commande == "listdir" or commande == "dir":
            res = commandes.ls()
            self.ecrire("")
            for x in res:
                self.ecrire(x, True)
        elif commande == "lkr":
            res = commandes.lkr()
            self.ecrire("")
            for x in res:
                self.ecrire(x, True)
        else:
            print("|"+commande+"|", arguments)
            self.ecrire('Mauvaise commande. Essayez de taper "help"')

    def afficher(self):
        hauteur = 985
        for i in range(self.nbre_lignes):
            globals.hud.texte(10, hauteur, self.historique[i], centrer=self.centre_historique[i])
            hauteur -= 20