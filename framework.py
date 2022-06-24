__author__ = "reza0310"

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.graphics import Rectangle
from kivy.core.text import Label as CoreLabel
from kivymd.app import MDApp
from kivy.uix.widget import Widget

import globals
#import connexions


class TextInput():
    liste = []

    def __init__(self, x, y, tx, ty, placeholder, password=False):
        self.text = ""
        self.shown_text = placeholder
        self.id = len(TextInput.liste)
        TextInput.liste.append(self)
        self.action = "TextInput.liste["+str(self.id)+"].focus()"
        globals.hud.bind((x, y), (tx, ty), self.action)
        self.clavier = None
        self.sent = False

        self.x = x
        self.y = y
        self.tx = tx
        self.ty = ty
        self.placeholder = placeholder

        self.password = password
        self.is_focused = False

        self.event = Clock.schedule_interval(self.actualiser, 1/globals.FPS)  # 60 fps

    def actualiser(self, dt):
        globals.hud.texte(self.x-(self.tx//2)+10, self.y, "> "+self.shown_text)

    def focus(self):
        global layout
        print("Focusing")
        self.clavier = Window.request_keyboard(self.unfocus, layout, 'text')
        self.clavier.bind(on_key_down=self.press)

    def unfocus(self):
        self.clavier.unbind(on_key_down=self.press)
        self.clavier = None

    def press(self, clavier, code, texte, modificateurs):
        if code[0] in [303, 304, 308, 301]:  # rshift, shift, alt, capslock
            pass
        elif code[0] == 8:
            self.text = self.text[:-1]
        elif code[0] == 13:
            self.sent = True
        elif texte == None:
            print("Code: ", code)
        else:
            if "capslock" in modificateurs or "shift" in modificateurs:
                if code[0] == 59:
                   self.text += "."
                else:
                    self.text += texte.upper()
            else:
                self.text += texte
        if len(self.text) == 0:
            self.shown_text = self.placeholder
        elif self.password:
            self.shown_text = "*"*len(self.text)
        else:
            self.shown_text = self.text

    def remove(self):
        TextInput.liste[self.id] = None
        if self.clavier is not None:
            self.unfocus()
        self.event.cancel()
        globals.hud.unbind(self.action)


class HUD:

    def __init__(self):
        self.longueur, self.largeur = Window.size
        self.boutons = []
        self.event = Clock.schedule_interval(self.actualiser, 1/20)  # 60 fps

    def bind(self, emplacement, taille, action, type="Bouton"):
        print("Binding", action, 'sur x variant de', (emplacement[0]-(taille[0]//2), emplacement[0]+(taille[0]//2)), 'et y', (emplacement[1]-(taille[1]//2), emplacement[1]+(taille[1]//2)))
        self.boutons.append({"type": type, "x": (emplacement[0]-(taille[0]//2), emplacement[0]+(taille[0]//2)), "y": (emplacement[1]-(taille[1]//2), emplacement[1]+(taille[1]//2)), "action": action})

    def unbind(self, unbin="all"):
        if unbin == 'all':
            self.boutons = []
        else:
            for bouton in [x for x in self.boutons]:  # Je sais que ça change rien par rapport à bouton in self.boutons de base mais visiblement pour le Menu.MENU.closemenu() c'est nécessaire
                if bouton["action"] == unbin:
                    self.boutons.remove(bouton)

    def press(self, touch):
        for bouton in self.boutons:
            if bouton["x"][0] < touch.spos[0]*1000 < bouton["x"][1] and bouton["y"][0] < touch.spos[1]*1000 < bouton["y"][1]:
                eval(bouton["action"])  # Handle joysticks
                return True
        return False

    def recoordonner(self, tupl):
        return int((tupl[0] / 1000) * self.longueur), int((tupl[1] / 1000) * self.largeur)

    def recoordonner_double(self, tupl):
        return int((tupl[0] / 1000) * self.longueur), int((tupl[1] / 1000) * self.largeur), int((tupl[2] / 1000) * self.longueur), int((tupl[3] / 1000) * self.largeur)

    def texte(self, x, y, texte, remove=True, color=(0, 1, 0, 1), taille_police=15, centrer=False):
        label = CoreLabel(text=str(texte), font_size=taille_police, color=color)
        label.refresh()
        text = label.texture
        rec = Rectangle(size=((len(texte)*5, text.size[1]) if centrer else text.size), pos=self.recoordonner((x, y - (text.size[1]//2))), texture=text)
        layout.canvas.add(rec)
        if remove:
            def rmv(dt):
                layout.canvas.remove(rec)
            Clock.schedule_once(rmv, 1/globals.FPS)
        else:
            return rec, False

    def image(self, x, y, tx, ty, image, remove=True):
        texture = Image(source=image).texture
        rec = Rectangle(size=globals.hud.recoordonner((tx, ty)), pos=self.recoordonner((x - (tx//2), y - (ty//2))), texture=texture)
        layout.canvas.add(rec)
        if remove:
            def rmv(dt):
                layout.canvas.remove(rec)
            Clock.schedule_once(rmv, 1/globals.FPS)
        else:
            return rec, False

    def actualiser(self, dt):
        self.longueur, self.largeur = Window.size


class Ecran(Widget):

    def add_entity(self, entity):
        self.entities.add(entity)
        self.canvas.add(entity.image)

    def remove_entity(self, entity):
        if entity in self.entities:
            self.entities.remove(entity)
            self.canvas.remove(entity.image)

    def on_touch_down(self, touch):
        x = globals.hud.press(touch)
        if not(x):
            super().on_touch_down(touch)
        

class PROJETApp(MDApp):
    def build(self):
        global layout
        self.title = 'PROJET'
        Window.clearcolor = (1, 1, 1, 1)
        if globals.mode == "DEV":
            if globals.orientation == "portrait":
                Window.size = globals.largeur_dev, globals.longueur_dev
            else:
                Window.size = globals.longueur_dev, globals.largeur_dev
        layout = Ecran()
        globals.jeu.initialiser()
        return layout


def start():
    PROJETApp().run()
