__author__ = "reza0310"

import structures
import framework
import CQRT
import globals


if __name__ == "__main__":
    globals.initialize()
    print("Variables ultra-globales:", [x for x in globals.__dict__.keys() if x[0] != "_" and x != "initialize"])
    framework.start()
