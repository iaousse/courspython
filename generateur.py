import random
def lancer_des():
    de_1, de_2 = random.randint(1, 6), random.randint(1, 6)
    return de_1, de_2

def test(de1, de2):
    if de1==de2:
        var_test = True
    else:
        var_test = False
    return var_test

def simulation(n):
    if n ==0:
        print("veuillez entre un nombre different de zero")
    else:
        liste_vrai = []
        for i in range(n):
            x, y = lancer_des()
            if test(x, y):
                liste_vrai.append(1)
        return len(liste_vrai)/n