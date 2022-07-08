import json
from CLIENT.bytes import bytestring
from CLIENT.commandes import bezout_euclide_etendu

testsets = {"TESTS BYTESTRINGS:": open("test_bytestrings.json", "r", encoding="utf-8"),
            "TESTS ARITHMETIQUES:": open("test_arith.json", "r", encoding="utf-8")}
for testset in testsets.keys():
    print(testset, "\n")
    tests = json.load(testsets[testset])
    for x in tests:
        print(x)
        i = 1
        try:
            for test in tests[x]:
                assert eval(test)
                print("Test", i, "passé")
                i += 1
            print("Réussi!\n")
        except AssertionError as e:
            print(f"TEST {i} ÉCHOUÉ! {e}\n")
        except Exception as e:
            print(f"ERREUR! {e}\n")
    print("\n")
    testsets[testset].close()
