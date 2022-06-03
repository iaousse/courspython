#!/usr/bin/env python
# coding: utf-8

# # Instructions conditionnelles et boucles
# 
# 
# ## Instructions conditionnelles (tests)
# En Python, il existe trois structures de test :
# 
# - La première est la plus simple contenant juste `if` :
# 
# ```python
# if condition:
#     instructions
# ```
# - La deuxième fait apparaitre `else` :
# ```python
# if condition:
#     instructions_1
# else:
#     instructions_2
# ```
# 
# 
# - La dernière fait apparaitre `elif` :
# ```python
# if condition_1:
#     Bloc d'instructions 1
# elif condition_2:
#     Bloc d'instructions 2
# elif condition_3:
#     Bloc d'instructions 3
# ...
# elif condition_n:
#     Bloc d'instructions n
# else:
#     Bloc d'instructions n+1
# ```
# 
# - pour la structure simple `if`: si  la condition est vrai, le bloc d'instructions en dessous est exécuté. Sinon, il ne sera pas exécuté.

# In[19]:


x = 10
# la condition est x<15
if x < 15:
    print(x, "est plus petit que 15")


# In[17]:


x = 10
# la condition est x==15
if x == 15:
    print(x, "est egale a 15")


# - Pour la structure `if...else` : si la condition de `if` est vrai, le bloc d'instructions en dessous de `if` sera exécuté. Sinon, le bloc en dessous de `else` sera exécuté.

# In[1]:


x = 10
# la condition est x<10
if x < 10:
    print(x, "est plus grand que 10")
else:
    print(x, "est plus petit ou égale à 10")


# - Pour la structure ‘if...elif.....else`: si  la condition de if est vrai, le bloc d'instructions en dessous de `if` sera exécuté. Sinon, si le bloc de `elif` est vrai le bloc en dessous de `elif` sera exécuté…. Sinon, si le bloc de `else` est vrai le bloc en dessous de `else` sera exécuté.

# In[2]:


x = 10
# la condition est x>10
if x > 10:
    print(x, "est plus grand que 10")
elif x < 10:
    print(x, "est plus petit ou égale à 10")
else:
    print(x, "est égale à 10")


# On peut également avoir une structure de test au sien d'une autre structure de test. Aussi, les conditions peuvent être composé de plusieurs conditions à l'aide des opérateurs logiques (`or`, `and`, et `not`).
# 
# Explorer le code ci-dessous est essayer de savoir son output.

# In[3]:


#
x = 6
# les conditions
condition1 = x>0; condition2 = x<9; condition3= x==2; condition4 = x == 3; 
condition5 = (x==5) or (x==7); condition6 = x<0; condition7= x>9

if condition1 and condition2:  ## remarquer qu'on a pas besoin de faire condition1==True
    if condition3 or condition4 or condition5:
        print(x, "est premier")
    else:
        print(x, "n'est pas premier")
else:
    if condition6:
        print(x, "est négatif")
    else:
        print(x, "est supérieur à 9")


# ## Les Boucles
# Lorsqu'on voulait répéter plusieurs fois l'exécution d'une partie du programme, on utilise les boucles. Il en existe deux types : 
# ### Les boucles bornées 
# Elles sont utilisées lorsqu'on a une idée a priori sur le nombre de répétition. Il s'agit de la boucle `for` ; la syntaxe de la boucle for est la suivante : 
# ```python
# for var in valeurs_possibles:
#     instructions
# ```
#     * `var` est le nom d'une variable locale à la fonction `for()` 
#     * `valeurs_possibles` un objet comprenant des éléments définissant les valeurs que prendra objet pour chaque itération, 
#     *  `instructions` est le bloc d'instructions qui seront exécutées à chaque itération.
# Voici deux exemples simples de l'utilisation de la boucle `for` :
# 1. Calculer le carrée de chaque nombre 1, 2, 3 et 4;
# 2. Calculer la somme des nombres 1, 2, 3 et 4.

# In[6]:


for i in [1, 2, 3, 4]:
    print("le carré de", i, "est:", i**2)


# In[4]:


somme = 0
for i in [1, 2, 3, 4]:
    somme += i
print(somme)


# Une fonction très importante qui est souvent utilisée en Python pour la boucle `for` est la fonction `range()`. Cette fonction prend les arguments suivants :
# - `start` : (optionnel, par défaut, 0) valeur de début pour la séquence (inclue) ;
# - `stop` : valeur de fin de la séquence (**non inclue**) ;
# - `step` : (optionnel, par défaut 1) le pas.
# 
# 
# On peut refaire les exemples suivants comme suit :

# In[7]:


for i in range(1, 5):
    print("le carré de", i, "est:", i**2)


# In[6]:


somme = 0
for i in range(5):
    somme += i
print(somme)


# Rien n'empêche avoir une boucle for dans un bloc d'instructions d'une autre boucle for. Ou encore une instruction conditionnelle dans un bloc de la boucle for (vice versa). Par exemple si on veut calculer le produit de chaque élément de la liste `[1, 5, 9, 10]` par chaque élément de la liste `[2, 3, 5]`:

# In[8]:


for i in [1, 5, 9, 10]:
    for j in [2, 3, 5]:
        print("Le produit de", i, "fois", j, "est:", i*j)


# Ou si l'on veut tester la parité de chaque élément entre 3, et 14 `(range(3,15)`);

# In[9]:


for i in range(3, 15):
    if i%2==0:
        print("Le nombre", i, "est pair")
    else:
        print("Le nombre", i, "est impair") 


# ### Les boucles non bornées 
# Elles sont utilisées si on ne connait pas à l'avance le nombre de répétitions. Il s'agit de la boucle `while`.
# Le principe d'une boucle `while()` est que les instructions à l'intérieur de la boucle seront répétées tant qu'une condition est respectée. L'idée est de faire dépendre cette condition d'un ou plusieurs objets qui seront modifiés au cours des itérations (sans cela, la boucle tournerait à l'infini).
# 
# La syntaxe est la suivante :
# ```python
# while condition:
#     instructions
# ```
#     
# Nous allons illustrer le rôle de chaque boucle dans l'exemple suivant. Supposons que nous voulons calculer le factoriel d'un nombre (soit 10), voici le code pour le calculer :

# In[13]:


i = 1
fact = 1
while i<=10:
    fact *= i
    i+=1

print(fact)


# Reprenons l'exemple précédant dont on veut tester la parité de chaque élément entre 3, et 14 avec la boucle while:

# In[10]:


i = 3
while i<15:
    if i%2==0:
        print("Le nombre", i, "est pair")
    else:
        print("Le nombre", i, "est impair")
    i+=1

