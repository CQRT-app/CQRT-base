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
                                  "rm": commandes.rm,
                                  "cd": commandes.cd,
                                  "mkr": commandes.mkr,
                                  "mv": commandes.mv,
                                  "rsa_gen_keys": commandes.rsa_gen_keys,
                                  "rgk": commandes.rsa_gen_keys,
                                  "reset": commandes.reset,
                                  "client_connect": commandes.client_connect,
                                  "make_account": commandes.make_account,
                                  "get_account": commandes.get_account}
        self.commandes_listes = {"ls": commandes.ls,
                                 "listdir": commandes.ls,
                                 "dir": commandes.ls,
                                 "lkr": commandes.lkr,
                                 "list_accounts": commandes.list_accounts,
                                 "credits": commandes.credits}

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
            try:
                self.ecrire(self.commandes_simples[commande](*arguments))
            except Exception as e:
                self.ecrire("Erreur: "+str(type(e))+": "+str(e))
        elif commande in self.commandes_listes:
            self.ecrire("")
            try:
                for x in self.commandes_listes[commande](*arguments):
                    self.ecrire(x, True)
            except Exception as e:
                self.ecrire("Erreur: "+str(type(e))+": "+str(e))
        elif commande == "help" or commande == "h" or commande == "?":
            res = commandes.help()
            for x in res[0].keys():
                self.ecrire("")
                self.ecrire(x.upper()+": "+res[0][x])
                if res[1][x] != "":
                    self.ecrire("ALIASES: "+res[1][x])
        elif commande == "send_message":
            try:
                commandes.send_message(arguments[0], arguments[1], arguments[2], arguments[3], ''.join('{} '.format(x) for x in arguments[4:]))
                self.ecrire("")
                self.ecrire("Message envoyé")
            except Exception as e:
                self.ecrire("Erreur: "+str(type(e))+": "+str(e))
        else:
            print("|"+commande+"|", arguments)
            self.ecrire('Mauvaise commande. Essayez de taper "help"')

    def afficher(self):
        hauteur = 985
        for i in range(self.nbre_lignes):
            globals.hud.texte(10, hauteur, self.historique[i], centrer=self.centre_historique[i])
            hauteur -= 20