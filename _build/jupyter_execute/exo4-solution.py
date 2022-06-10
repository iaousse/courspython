#!/usr/bin/env python
# coding: utf-8

# # Essayez vous-même !
# 
# <hr style="border:2px solid gray"> </hr>
# 
# ## Exercice 1. 
# Ecrire une procédure dont on passe le nom et l’âge et affiche le message suivant : `Bonjour nom, vous avez age ans.`.
# 
# Appeler la fonction en passant votre nom et votre âge comme arguments.

# In[1]:


def nom_age(nom, age):
    print(f'Bonjour {nom}, vous avez {age} ans.')
    
print(nom_age("Iyad", 2))


# <hr style="border:2px solid gray"> </hr>
# 
# ## Exercice 2. 
# Ecrire une fonction `somme_carree` qui prend deux arguments `a` et `b`. Dans cette fonction créer deux autres fonctions `somme` et `carree` telles que :
# - `somme` permet de calculer la somme de deux nombres,
# - `carree` qui permet de calculer le carré d'un nombre
# 
# La somme de deux nombres. la fonction doit utiliser `somme` et `carree` pour retourner la somme des carrés de `a` et `b` ($a^2 + b^2$).

# In[2]:


def somme_carree(a, b):
    def somme(a, b):
        return a+b
    def carree(a):
        return a**2
    return somme(carree(a), carree(b))
print(somme_carree(2, 3))


# <hr style="border:2px solid gray"> </hr>
# 
# ## Exercice 3. 
# Ecrire une fonction qui permet de résoudre Exercice 3 dans le chapitre précédant: retourne le nombre de lettres, de chiffres et symbole dans une chaine de caractères. Utiliser `'my_n@me%is$meth0s!'` pour l'appeler.
# 

# In[3]:


def compter_chaine(chaine):
    nombre = lettre = symbole = 0
    for char in chaine:
        if char.isdigit():
            nombre += 1
        elif char.isalpha():
            lettre += 1
        else:
            symbole += 1
    return lettre, symbole, nombre

chaine = 'my_n@me%is$meth0s!'
lettre, nombre, symbole = compter_chaine(chaine)
print(f'le nombre de lettres est : {lettre}\nle nombre de chiffres est : {nombre}\nle nombre de symbole est:{symbole}')


# <hr style="border:2px solid gray"> </hr>
# 
# ## Exercice 4. 
# Ecrire une fonction récursive qui permet de calculer le factoriel d'un nombre.

# In[4]:


def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
    
print(fact(10))


# <hr style="border:2px solid gray"> </hr>
# 
# ## Exercice 5. 
# Ecrire une fonction récursive qui permet de calculer la suite de Fibonacci. Afficher les 10 premiers éléments de cette suite.
# 

# In[5]:


def fibonaci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonaci(n-1)+fibonaci(n-2)

    
for i in range(1, 13):
    print(fibonaci(i))


# <hr style="border:2px solid gray"> </hr>
# 
# ## Exercice 6. 
# Importer `sin`,  `cos`, `tan`, et `pi` depuis le module `math` et calculer:
# - sin(0)
# - cos(0)
# - tan(0)
# - sin(pi/2)
# - cos(pi/2)
# - tan(pi/2)
# - sin(pi)
# - cos(pi)
# - tan(pi)
# 

# In[6]:


from math import sin, cos, tan, pi
print(sin(0))
print(cos(0))
print(tan(0))
print(sin(pi/2))
print(cos(pi/2))
print(tan(pi/2))
print(sin(pi))
print(cos(pi))
print(tan(pi))


# <hr style="border:2px solid gray"> </hr>
# 
# ## Exercice 7. 
# Soit l'expérience suivante : On jette deux et on note le résultat de chaque dé. Quelle est la probabilité que les deux nombres obtenus sont égaux ?
# Mathématiquement le résultat est : $\dfrac{6}{36}\approx 0.1666666... \approx 0.167 \approx 0.17$.
# 
# On veut réaliser une simulation avec python pour savoir si l'on peut la calculer avec des nombres aléatoires.
# 
# Pour ce faire, créer le fichier python `generateur.py`tel que :
# - fonction `lancer_des` qui permet de simuler le lancer de deux dés simultanément.
# - une fonction `test` qui permet de tester si le résultat des deux dés sont égaux.
# - une fonction `simulation` qui permet de calculer la proportion des expériences avec les nombres affiches dans les dés égaux dans le nombre total d'expériences.
# 
# Importer les fonctions depuis `generateur.py` et :
# 1. afficher le résultat de 10 expériences du lancer des deux dés.
# 2. tester pour 10 expériences si le nombre dans le premier dés égale au nombre dans le deuxième de.
# 3. calculer les probabilités pour 1, 10, 20, 100, 1000, 5000, 10000 et 100000 expériences.

# In[15]:


import generateur
for i in range(10):
    de1, de2 = generateur.lancer_des()
    print(de1, de2, generateur.test(de1, de2))

liste = [1, 10, 20, 100, 1000, 5000, 10000, 100000]
for i in liste:
    print(generateur.simulation(i))

