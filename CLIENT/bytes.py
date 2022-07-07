def equalize(fonction):
    def wrapper(x, y, *args, **kwargs):
        if type(y) == bytestring:
            maxlen = max(len(x), len(y))
            x.fill(maxlen)
            y.fill(maxlen)
            res = fonction(x, y, *args, **kwargs)
            x.clean()
            y.clean()
            return res
        else:
            return fonction(x, y, *args, **kwargs)
    return wrapper


class bytestring:
    # ---------- Initialisation ----------
    def __init__(self, val):
        if type(val) == bytes:
            self.contenu = ""
            for x in val:
                if x == 49:
                    self.contenu += "1"
                else:
                    self.contenu += "0"
        elif type(val) == str:
            if val.count("0") + val.count("1") == len(val):  # Conversion depuis un string de bytes
                self.contenu = val
                self.signed = False
            else:  # Conversion depuis une chaine de caracteres
                self.contenu = ''.join('{0:08b}'.format(ord(x), 'b') for x in val)
                self.signed = False
        elif type(val) == int:
            if val < 0:
                self.contenu = "1"+bytestring(bin(val)[3:]).complement(2)
                self.signed = True
            else:
                self.contenu = bin(val)[2:]
                self.signed = False
        else:
            raise TypeError("bytestring: Type non pris en charge pour la conversion")

    # ---------- Méthodes prédéfinies ----------

    # Générales:

    def __len__(self):
        return len(self.contenu) if not self.signed else len(self.contenu)-1

    # Mathématiques:

    def __abs__(self):  # abs(self)
        if not self.signed:
            return self.contenu
        elif self.signed and self.contenu[0] == "0":
            return self.contenu[1:]
        else:
            return bytestring(self.contenu[1:]).complement(2)

    @equalize
    def __add__(self, other):  # self + other
        if type(other) == int:
            return int(self) + other
        elif type(other) == bytestring:
            feeling = 2*len(self)

            self.clean()
            self.fill(feeling)
            self.contenu = self.signed_version()
            self.signed = True

            other.clean()
            other.fill(feeling)
            other.contenu = other.signed_version()
            other.signed = True

            cpt = 0
            res = ""
            for i in range(len(self)-1, -1, -1):
                if self.contenu[i] == "1":
                    cpt += 1
                if other.contenu[i] == "1":
                    cpt += 1
                res = str(cpt % 2) + res
                cpt -= (cpt // 2 + cpt % 2)
            res = str(cpt) + res
            r = bytestring(res)
            r.signed = True
            return r
        else:
            raise TypeError("bytestring: Type non pris en charge pour la conversion")

    @equalize
    def __sub__(self, other):  # self - other
        other.contenu = other.signed_version().complement(2)
        other.signed = True
        return self + other

    def __mul__(self, other):  # self * other
        pass

    def __floordiv__(self, other):  # self // other
        pass

    def __truediv__(self, other):  # self / other
        raise NotImplementedError("bytestring: Inutile a mon implémentation")

    def __mod__(self, other):  # self % other
        pass

    def __pow__(self, power, modulo=None):  # self ** other ou pow(self, power, modulo)
        pass

    # Comparaisons:

    @equalize
    def __lt__(self, other):  # self < other
        # Cas facile
        if self == other:
            return False
        # Signes
        if self.signed_version()[0] > other.signed_version()[0]:
            return True
        elif self.signed_version()[0] < other.signed_version()[0]:
            return False
        elif self.signed_version()[0] == other.signed_version()[0] == "1":
            return abs(self) > abs(other)
        else:
            # Comparaison
            for i in range(len(self)):
                if self.contenu[i] < other.contenu[i]:
                    return True
                elif self.contenu[i] > other.contenu[i]:
                    return False
            raise Exception("Cas impossible")

    @equalize
    def __le__(self, other):  # self <= other
        if self == other:
            return True
        else:
            return self < other

    @equalize
    def __gt__(self, other):  # self > other
        # Cas facile
        if self == other:
            return False
        # Signes
        if self.signed_version()[0] > other.signed_version()[0]:
            return False
        elif self.signed_version()[0] < other.signed_version()[0]:
            return True
        elif self.signed_version()[0] == other.signed_version()[0] == "1":
            return abs(self) < abs(other)
        else:
            # Comparaison
            for i in range(len(self)):
                if self.contenu[i] > other.contenu[i]:
                    return True
                elif self.contenu[i] < other.contenu[i]:
                    return False
            raise Exception("Cas impossible")

    @equalize
    def __ge__(self, other):  # self >= other
        if self == other:
            return True
        else:
            return self > other

    def __eq__(self, other):  # self == other
        return self.contenu == other.contenu and self.signed == other.signed

    def __ne__(self, other):  # self != other
        return self.contenu != other.contenu or self.signed != other.signed

    # Opérations binaires:

    def __invert__(self):  # ~ self
        self.contenu = self.complement(1)
        return self.contenu

    def __rshift__(self, other):  # self >> other
        ajout = self.signed_version()[0]
        for i in range(other):
            self.contenu = self.contenu[:-1]
            self.contenu = ajout + self.contenu
        self.clean()
        return self

    def __lshift__(self, other):  # self << other
        self.contenu += "0"*other
        return self

    @equalize
    def __and__(self, other):  # self & other
        r = bytestring("")
        for i in range(len(self)):
            if self.contenu[i] == "1" and other.contenu[i] == "1":
                r.contenu += "1"
            else:
                r.contenu += "0"
        r.clean()
        return r.contenu

    @equalize
    def __or__(self, other):  # self | other
        r = ""
        for i in range(len(self)):
            if self.contenu[i] == "1" or other.contenu[i] == "1":
                r += "1"
            else:
                r += "0"
        return r

    @equalize
    def __xor__(self, other):  # self ^ other
        r = ""
        for i in range(len(self)):
            if self.contenu[i] == other.contenu[i]:
                r += "0"
            else:
                r += "1"
        return r

    # Conversions:

    def __str__(self):  # str(self)
        res = ""
        self.pad(8)
        for i in range(0, len(self.contenu), 8):
            res += chr(int(self.contenu[i:i+8], 2))
        return res

    def __int__(self):  # int(self)
        if self.signed and self.contenu[0] == "1":
            return -1 * int(abs(self), 2)
        else:
            return int(self.contenu, 2)

    def __float__(self):  # float(self)
        raise NotImplementedError("bytestring: Inutile a mon implémentation")

    def __bytes__(self):
        test = b''
        for x in self.contenu:
            if x == "1":
                test += b'1'
            else:
                test += b'0'
        return test

    # Assignations:

    def __iadd__(self, other):
        self.be(self + other)

    def __iand__(self, other):
        self.be(self & other)

    def __ifloordiv__(self, other):
        self.be(self // other)

    def __ilshift__(self, other):
        self.be(self << other)

    def __imod__(self, other):
        self.be(self % other)

    def __imul__(self, other):
        self.be(self * other)

    def __ior__(self, other):
        self.be(self | other)

    def __ipow__(self, other):
        self.be(self ** other)

    def __irshift__(self, other):
        self.be(self >> other)

    def __isub__(self, other):
        self.be(self - other)

    def __itruediv__(self, other):
        self.be(self / other)

    def __ixor__(self, other):
        self.be(self ^ other)

    # ---------- Méthodes définies ----------

    def signed_version(self):
        if self.signed:
            return self.contenu
        else:
            return "0"+self.contenu

    def fill(self, val):
        self.contenu = self.contenu.zfill(val)
        return self

    def pad(self, val):
        taille = len(self.contenu)
        if taille % val == 0:
            return self.contenu
        else:
            return self.fill(taille + (val - (taille % val))).contenu

    def be(self, other):
        if type(other) != bytestring:
            other = bytestring(other)
        self.contenu = other.contenu
        self.signed = other.signed

    def complement(self, numero):
        if numero == 1:
            retourner = True
        else:
            retourner = False
        inverse = ""
        for i in range(len(self.contenu)-1, -1, -1):
            if retourner:
                if self.contenu[i] == "0":
                    inverse = "1" + inverse
                else:
                    inverse = "0" + inverse
            else:
                inverse = self.contenu[i] + inverse
                if self.contenu[i] == "1":
                    retourner = True
        return inverse

    def clean(self):
        if self.signed:
            firstbit = self.contenu[0]
            self.contenu = self.contenu[1:]
        while self.contenu[0] == "0" and len(self.contenu) > 1:
            self.contenu = self.contenu[1:]
        if self.signed:
            self.contenu = firstbit + self.contenu
        return self

    def hexa(self):  # Impossible de réécrire hex(self) sans devoir renvoyer un int en passant par __index__
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
        self.pad(4)
        for i in range(0, len(self.contenu), 4):
            res += hex_dict[self.contenu[i]+self.contenu[i+1]+self.contenu[i+2]+self.contenu[i+3]]
        return res

    def sur(self, x):
        self.fill(x)
        return self.contenu[len(self)-x:]

    def crc(self):
        cric = bytestring(0xB704CE)
        for i in range(len(self)):
            cric ^= self << 16
            self += 1
            for y in range(8):
                cric <<= 1
                if cric.contenu[len(cric)-7] == 1:
                    cric ^= bytestring(0x864CFB)
        return cric.sur(6)

    def cypher(self, other):
        while len(other) < len(self):
            other.contenu += other.contenu
        while len(other) > len(self):
            other.contenu = other.contenu[:-1]
        return bytestring(self ^ other)