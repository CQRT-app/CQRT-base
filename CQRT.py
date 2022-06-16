__author__ = "reza0310"

from kivy.clock import Clock

from random import randint

#from connexions import echanger, recevoir
from structures import Commandeur
import framework
import globals


class Coeur:

    def initialiser(self):
        self.zone_de_texte = framework.TextInput(500, 60, 1000, 100, "Entrez vos commandes ici")
        self.zone_de_texte.event.cancel()  # On actualise à la main après l'arrière plan sinon ce sera caché
        self.commandeur = Commandeur()
        self.event = Clock.schedule_interval(self.actualiser, 1/globals.FPS)  # 60 fps

    def actualiser(self, dt):
        globals.hud.image(500, 500, 1000, 1000, globals.images["arriere_plan"])
        if self.zone_de_texte.sent:
            self.commandeur.execute(self.zone_de_texte.text)
            self.zone_de_texte.sent = False
            self.zone_de_texte.text = ""
            self.zone_de_texte.shown_text = self.zone_de_texte.placeholder
        self.commandeur.afficher()
        self.zone_de_texte.actualiser(dt)