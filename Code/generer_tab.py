from random import randint

def generer_tab():
    tab = []
    for _ in range(5):
        tab.append(randint(1, 99))
    return tab

def generer_tab2():
    tab = [0 for i in range(5)]
    for i in range(5):
        tab[i] = randint(1, 99)
    return tab