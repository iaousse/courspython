#!/usr/bin/env python
# coding: utf-8

# # Essayez-vous-même!
# 
# <hr style="border:2px solid gray"> </hr>
# 
# ## Exercice 1. 
# Ecrire un programme qui permet de résoudre l'équation suivante : 
# 
# $$
# ax+b=0
# $$
# 
# - Le programme doit demander à l'utilisateur les paramètres a et b (pas la peine de contrôler le type des paramètres)
# - Le programme doit afficher le résultat de la manière la plus sophistiquée possible.
# 
# _indication_ : 
# - _convertir les données entrées au type de données adéquat_.
# - utiliser les instructions conditionnelles (faite une recherche sur la solution de l'équation $ax+b=0$).
# 

# In[35]:


## votre code ici


# <hr style="border:2px solid gray"> </hr>
# 
# ## Exercice 2. 
# Ecrire un programme qui demande aux étudiant d'entrer les notes des modules suivants : math, informatique, français. Le programme doit afficher les éléments suivants :
# - si les modules sont valides (note supérieure à 10).
# - la moyenne des trois modules (moyenne = .5*note_de_math + .4*note_informatique + .1*note_francais)
# - excellent si la moyenne dépasse 18, très bien si la moyenne entre 16 et 18, bien si la moyenne entre 12 et 16, passable si la moyenne entre 10 et 12, non valide sinon.

# In[ ]:


## votre code ici


# <hr style="border:2px solid gray"> </hr>
# 
# ## Exercice 3. 
# Une fonction qui permet de calculer la somme des éléments d'une liste (et d'autre objets que nous allons voir) est `sum()`. La syntaxe est `sum(liste)` tout simplement. Voici une liste pour calculer la somme de ses éléments : `ma_liste = [ 1, 5, 18181, 55, 100]`
# 
# - créer un variable `somme_avec_sum` qui va contenir la somme des éléments de la liste avec la fonction `sum()`
# - créer une variable `somme_avec_for` qui va contenir la somme des éléments de la liste en utilisant la boucle `for`.
# - créer une variable `test_somme` qui va contenir le test d’égalité des deux variables `somme_avec_sum` et `somme_avec_for`.
# - afficher chaque variable.
# 
# _note_: vous devez avoir True pour `test_somme` sinon vous avez mal calculé de `somme_avec_for`!

# In[2]:


## votre code ici
#ma_liste = [ 1, 5, 18181, 55, 100]


# <hr style="border:2px solid gray"> </hr>
# 
# ## Exercice 4. 
# Ecrire un programme qui permet d'afficher les 20 premiers nombres multiples de 3 avec `while`
# 
# Refaire le programme précédant avec la boucle `for`

# In[7]:


## votre code ici


# <hr style="border:2px solid gray"> </hr>
# 
# ## Exercice 5. 
# Ecrire un programme qui permet d'afficher le modèle suivant à l'aide d'une boucle :
# ```
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
# 1 2 3 4 5 6
# 1 2 3 4 5 6 7
# ```

# In[5]:


## votre code ici


# <hr style="border:2px solid gray"> </hr>
# 
# ## Exercice 6. 
# 
# La suite de Fibonacci est une suite de nombres. On calcule les éléments de cette suite de la manière suivante :
# - Les deux premiers chiffres sont 0 et 1 ;
# - un élément de la suite est calculer en additionnant les deux nombres qui le précèdent. 
# Par exemple, 0, 1 (les deux premières éléments), 1 (obtenu par 0+1), 2 (obtenu par 1+1), 3 (obtenu par 1+2), 5, 8, 13. 
# Le nombre suivant dans cette suite est : 8+13 = 21. Et ainsi de suite.
# 
# Calculer les 12 premiers éléments de cette suite.

# In[23]:


## votre code ici


# <hr style="border:2px solid gray"> </hr>
# 
# ## Exercice 7. 
# 
# Ecrire un programme qui permet d'inverser un nombre entier donné (par exemple : inverser le nombre 89457 revient à donner le nombre 75498).

# In[16]:


## votre code ici


# <hr style="border:2px solid gray"> </hr>
# 
# ## Exercice 8. 
# (**Can you find the secret number?**)
# 
# Ecrire un programme qui implémente le jeu suivant :
# - décider un nombre secret (par exemple 24) ;
# - Afficher un message du bienvenu au jeu qui détaille les règles du jeu (par exemple "bienvenu a notre jeu", …)
# - vous dites au joueur qu'il a 4 tentatives de jeu
# - vous demander au joueur d'entrer un nombre 
# - si le nombre entre est inférieur au nombre secret, vous afficher un message disant que le nombre entre est plus petit que le nombre secret
# - si le nombre entre est supérieure nombre secret, vous afficher un message disant que le nombre entre est plus grands que le nombre secret
# - après chaque tentative, afficher un message disant au joueur qu'il reste moins de tentative (exemple : après la première tentative incorrecte vous afficher qu’il reste 3 tentatives seulement)
# - après la tentative correcte afficher un message de félicitations
# - après 4 tentatives incorrectes afficher un message de regret et le nombre qui doit être ….

# In[28]:


## votre code ici

