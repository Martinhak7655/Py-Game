import random
def gameu(randint):
    user = int(input("Greq Dzer  Tivy"))
    if user == randint:
        print("Apres Duq haxteciq")
    elif user == 5:
        print("Minchev 1 ic 4 tvery")
    else:
        print("Cavoq Duq partveciq")
        gameu(random.randint(1, 4))


gameu(random.randint(1, 4))