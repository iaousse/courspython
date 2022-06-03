#!/usr/bin/env python
# coding: utf-8

# # Essayez-vous-même !
# 
# <hr style="border:2px solid gray"> </hr>
# 
# ## Exercice 1. 
# Ordre des opérations : quelle est selon vous le résultat de ces opérations :
# - $(4/2)^2\times 2 + 1$, $4/2^{(2\times 2)} + 1$, 
# - $4/2^2\times (2 + 1)$, 
# - $4/2^2\times 2 + 1$ 
# verifier avec Python.

# In[35]:


## votre code ici


# <hr style="border:2px solid gray"> </hr>
# 
# ## Exercice 2. 
# Un père a une somme d'argent de 1554 dh, il veut la partager sur ses 9 enfants de manière équitable et s'il reste quelque dirham, il va acheter des chocolats a 1 dh l'unité. Combien chaque enfant va recevoir ? combien d'unité de chocolat peut-il acheter avec le reste?

# In[ ]:


## votre code ici


# <hr style="border:2px solid gray"> </hr>
# 
# ## Exercice 3. 
# Quel est le type de données de valeurs suivantes :
# - `1`
# - `1.`
# - `False`
# - `"False"`
# - `"5.4"`
# - `var1/var2` avec `var1 = 1` et `var2 = 2`
# - `list()`
# - `None`
# - `""`

# In[7]:


## votre code ici


# <hr style="border:2px solid gray"> </hr>
# 
# ## Exercice 4. 
# Convertir, si c'est possible, de valeurs suivantes aux types de données que nous avons vues. Expliciter les cas qui ne sont pas possible :
# - `1`
# - `1.`
# - `False`
# - `"False"`
# - `"5.4"`
# - `var1/var2` avec `var1 = 1` et `var2 = 2`
# - `list()`
# - `None`
# - `""`

# In[7]:


## votre code ici


# <hr style="border:2px solid gray"> </hr>
# 
# ## Exercice 5. 
# Soient `x = True`, `y= 7<6`, and `z= not y`. Déterminer la valeur logique de `x, y,` et `z` (`True` ou `False`) puis la valeur de chacun des expression suivantes:
# - `x != False`
# - `x and y`
# - `x or y`
# - `not y`
# - `x and (y or z)`
# - `(x and y) or z`
# - `(not x or not y) and (not z)`
# - `not ((x and y) or z)`

# In[23]:


## votre code ici


# <hr style="border:2px solid gray"> </hr>
# 
# ## Exercice 6. 
# On veut recevoir ce message avec `print()`:
# ```
# La valeur de x est : @@True@@
# *********==============********
# ```
# En utilisant les arguments suivants :
# - `x = True`
# - `a = "la valeur de x est :"`
# 
# Toute modification devra être faite au niveau de `sep=`, et `end=`.

# In[24]:


## votre code ici


# <hr style="border:2px solid gray"> </hr>
# 
# ## Exercice 7. 
# Ecrire un petit programme qui permet de demander à l'utilisateur d'entrer son nom, son poids en kilogramme (sans entrer l'unité), et sa taille en mètre (sans entrer l'unité). Puis il affiche l'indice du poids (Body mass index (BMI)) :
# _Formule du BMI_ : $BMI = \dfrac{poids}{taille^2}$.

# <hr style="border:2px solid gray"> </hr>
# 
# ## Exercice 8. 
# Il existe plusieurs methodes d'affectation des variables. Essayer le code ci-dissous:

# In[24]:


## votre code ici
## votre code ici
#initialisation
a, b, c, d = 1,1, 0, 4
print('==================')
print('Initialisation')
print('==================')
print(a,b,c,d, sep='\n')

# reaffectation des variables
a, b, c, d = d, -a, c+b, 5
print('==================')
print('Reaffectation')
print('==================')
print(a,b,c,d, sep='\n')

