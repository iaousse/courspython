#!/usr/bin/env python
# coding: utf-8

# # Les fonctions
# 
# ## Définition d'une fonction (`function`)
# 
# Une fonction est un bloc de code qui ne s'exécute que lorsqu'elle est appelée. Nous pouvons transmettre des données, appelées paramètres, dans une fonction. Elle peut renvoyer des données en conséquence.
# 
# Nous avons rencontré plusieurs fonction dites `built-in functions` telles que, `print()`, `input()`,  `len()`, `sum()`, ... Il s'agit en fait d'un ensemble d'instruction qui servent à réaliser une tache (déterminer la taille d'une liste, sommer les éléments d'une liste,...)

# ## Création d'une fonction
# 
# En Python, une fonction est définie à l'aide du mot-clé `def` :
# 
# Ls syntaxe pour créer une fonction est la suivante :
# 
# ```python
# def une_fonction(arguments):
#     instructions
#     return donnees (eventuellement)
# ```
# 
# Voici une fonction qui ne renvoie aucune données mais il affiche un message :
# 

# In[38]:


# création d'une fonction sans arguments sans return
def hello_world_function():
    print("hello world!")
          
# création d'une fonction avec arguments sans return
def bonjour_function(nom):
    print("Bonjour "+nom)
          
# création d'une fonction sans argument avec return
def cinq():
          return 5
          
# création d'une fonction avec argument avec return
def caree(nombre):
    return nombre**2


# In[2]:


print(hello_world_function())

print(bonjour_function("iaousse"))

print(cinq()+3)
print(caree(15))


# ## Fonctions et procédures
# Les fonctions et les procédures ont la même syntaxe ; on les distingue de la manière suivante :
# - Une fonction prend des arguments et retourne une valeur ;
# - Une procédure réalise une action : affichage, écriture d'un fichier, ouverture d'une fenêtre graphique, modification d'un objet... Ces changements perdurent après l'appel de la procédure. Elle retourne la valeur `None`. Par exemple, la fonction `hello_world_function` est en fait une procédure.

# In[36]:


var = hello_world_function()
print(var)


# ## Arguments -- Paramètres
# 
# Les termes paramètres et argument peuvent être utilisés pour la même chose : des informations transmises à une fonction.
# 
# Cependant, du point de vue d'une fonction :
# 
# - Un paramètre est la variable répertoriée entre parenthèses dans la définition de la fonction.
# 
# - Un argument est la valeur qui est envoyée à la fonction lorsqu'elle est appelée.
# 

# In[39]:


def multip(x, y): # ici, x et y sont des paramètres de la fonction
    return x*y

x, y = 10, 5 # ici x et y sont des arguments qui doivent être passés à la fonction

print(multip(x, y))


# Lorsqu'on définit une fonction `def fonction(x, y):` les arguments x et y sont appelés `arguments positionnels` (`positional arguments`). Il est strictement obligatoire de les préciser lors de l'appel de la fonction (telle qu la fonction `multip` definie ci-dessus). En effet, si une fonction attend deux arguments et nous ne lui en passons qu'un seul. Un message d'erreur et afficher :

# In[5]:


a = 5
print(multip(a))


# En plus, l'ordre des arguments doit être respecter dans la fonction, nous allons illustrer ça avec la fonction suivante :

# In[40]:


def soustra(x, y):
    return x-y

# le premier argument est 5 le deuxième est 4
print(soustra(5, 4))
# le premier argument est 4 le deuxième est 5
print(soustra(4, 5))
# le premier argument est 5 le deuxième est 4
print(soustra(y=4, x = 5))


# Un argument défini avec une syntaxe `def fonction(arg=val):` est appelé `argument par mot-clé` (`keyword argument`). Le passage d'un tel argument lors de l'appel de la fonction est facultatif.

# In[10]:


def multip1(x, y=1):
    return x*y

print(multip1(5, 10))
print(multip1(5))


# In[15]:


def multip1(x=5, y=2):
    return x*y

print(multip1(5, 10))
print(multip1())


# Les arguments par mot-clé sont pris dans l'ordre dans lesquels on les passe lors de l'appel. 

# In[16]:


print(multip1(5)) # ici x qui prend la valeur 5


# Si l'on souhaite préciser l'argument par mot-clé `y` et garder la valeur de `x` par défaut, on doit simplement préciser le nom de l'argument lors de l'appel :

# In[17]:


print(multip1(5)) # ici x qui prend la valeur 5
print(multip1(y=5)) # ici y qui prend la valeur 5


# Python permet même de rentrer les arguments par mot-clé dans un ordre arbitraire. On peut aussi avoir un mélange d'`arguments positionnels` et `par mot-clé`. Mais, **les arguments positionnels doivent toujours être placés avant les arguments par mot-clé** :

# In[21]:


def soustr2(y=1, x=5):
    return x-y
print(soustr2(x=5, y=10))
print(soustr2(y=5, x=10))


# In[25]:


def fonction(a, b, c, d=100, e=200):
    return a , b, c, d, e

print(fonction(1, 1, 1, 1, 1))

print(fonction(1, 1, 1))


# In[27]:


def fonction(d=100, e=200, a, b, c):
    return a , b, c, d, e

print(fonction(1, 1, 1, 1, 1))

print(fonction(1, 1, 1))


# ## Variables locales et variables globales
# 
# Lorsqu'on manipule des fonctions, il est essentiel de bien comprendre comment se comportent les variables. Une variable est dite `locale` lorsqu'elle est créée dans une fonction. Elle n'existera et ne sera visible que lors de l'exécution de ladite fonction.
# 
# Une variable est dite `globale` lorsqu'elle est créée dans le programme principal. Elle sera visible partout dans le programme.
# 
# Voici un exemple illustratif:

# In[43]:


# Un espace de la mémoire nommé Global frame est alloue au programme principal
def addition(a, b):
    # un espace des variables est alloué à la fonction une fois elle est appelée
    c = a+ b # c, a et b sont des variables locales
    return c
x, y = 1, 3 # x et y sont des variables globales 
z = addition(x, y) # z est une variable globale
# Lorsque Python quitte la fonction, l'espace des variables alloué à la fonction est détruit. 
# Toutes les variables créées dans la fonction n'existent plus.
print(z)


# In[44]:


print(c) # Python ne va pas reconnaitre cette variable car elle n'existe pas dans Global frame


# ## Fonctions récursives
# 
# Une simple définition d'une `fonction récursive` est une fonction qui contient au moins un appel à elle-même. Un `langage récursif` est un langage dans lequel on peut programmer des fonctions récursives. Python est un langage récursif. Un simple exemple pour exploiter les fonctions récursives est le calcul des puissances de deux : $2^n$.

# In[37]:


def puissances_de_deux(n):
    if n == 0:
        return 1
    else:
        return 2*puissances_de_deux(n-1)
    
print(puissances_de_deux(4))


# ```{warning}
# Pour s'assurer de la terminaison d'une fonction récursive, on doit respecter les règles suivantes :
# - La fonction doit contenir un ou plusieurs cas de base ne comportant pas d'appel récursif.
# Dans la fonction puissances_de_deux : c'est le cas $n = 0$.
# - Les appels de la fonction se font des arguments plus simples pour conduire aux cas de base
# Dans l'appel de puissances_de_deux(n) : les arguments successifs sont $n − 1 > n − 2 > · · · > 0$.
# ```
# 
