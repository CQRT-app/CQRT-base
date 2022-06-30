class bytestring:
    # ---------- Initialisation ----------
    def __init__(self, val):
        if type(val) == str:
            if val.count("0") + val.count("1") == len(val):  # Conversion depuis un string de bytes
                self.contenu = val
                self.signed = False
            else:  # Conversion depuis une chaine de caracteres
                self.contenu = ''.join('{0:08b}'.format(ord(x), 'b') for x in val)
                self.signed = False
        elif type(val) == int:
            if val < 0:
                ainverser = bin(val)[3:]
                inverse = ""
                for x in ainverser:
                    if x == "0":
                        inverse += "1"
                    else:
                        inverse += "0"
                self.contenu = "1"+bytestring(int(inverse, 2) + 1).contenu
                self.signed = True
            else:
                self.contenu = bin(val)[2:]
                self.signed = False
        else:
            raise Exception("bytestring: Type non pris en charge pour la conversion")

    # ---------- Méthodes prédéfinies ----------

    # Mathématiques:

    def __abs__(self):  # abs(self)
        pass

    def __add__(self, other):  # self + other
        pass

    # Comparaisons:

    def __ge__(self, other):  # self >= other
        pass

    # Opérations binaires:

    def __invert__(self):  # ~ self
        pass

    # Conversions:

    def __str__(self):  # str(self)
        pass

    def __int__(self):  # int(self)
        pass

    def __str__(self):  # str(self)
        pass

    # Assignations:

    def __iadd__(self, other):
        res = self + other
        self.contenu = res.contenu
        self.signed = res.signed

    def __isub__(self, other):
        res = self - other
        self.contenu = res.contenu
        self.signed = res.signed

    # ---------- Méthodes définies ----------

    def signed_version(self):
        if self.signed:
            return self.contenu
        else:
            return "0"+self.contenu

    def hexa(self):
        res = ""
        hex_dict = {
            "0000": "0",
            "0001": "1",
            "0010": "2",
            "0011": "3",
            "0100": "4",
            "0101": "5",
            "0110": "6",
            "0111": "7",
            "1000": "8",
            "1001": "9",
            "1010": "A",
            "1011": "B",
            "1100": "C",
            "1101": "D",
            "1110": "E",
            "1111": "F",
        }
        self.contenu.pad(4)
        for i in range(0, len(self.contenu), 4):
            res += hex_dict[self.contenu[i]+self.contenu[i+1]+self.contenu[i+2]+self.contenu[i+3]]

    def fill(self, val):
        self.contenu = self.contenu.zfill(val)
        return self.contenu

    def pad(self, val):
        taille = len(self.contenu)
        if taille % val == 0:
            return self.contenu
        else:
            return self.fill(taille + (val - (taille % val)))

    def complement(self, numero):
        pass