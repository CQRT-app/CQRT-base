import json
from CLIENT.bytes import bytestring

testsets = {"TESTS BYTESTRINGS:": open("test_bytestrings.json", "r", encoding="utf-8")}
for testset in testsets.keys():
    print(testset)
    tests = json.load(testsets[testset])
    for x in tests:
        print(x)
        try:
            for test in tests[x]:
                assert eval(test)
            print("Réussi!\n")
        except Exception as e:
            print(f"ÉCHOUÉ! {e}\n")
    print("\n")
    testsets[testset].close()
