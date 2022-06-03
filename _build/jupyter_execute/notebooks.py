#!/usr/bin/env python
# coding: utf-8

# Introduction
# ===========
# 
# Le present chapitre introduit les grandes caractéristiques du langage Python, le replace dans l'histoire des langages informatiques, donne les particularités de production des programmes, définit la notion si importante d'algorithme et conclut sur les divers implémentations disponibles.
# Python est un langage de programmation de haut niveau (high-level programming language), avec des applications dans de nombreux domaines, notamment la programmation Web, le calcul scientifique et l'intelligence artificielle !
# 
# Python est très populaire et utilisé par des organisations telles que Google, la NASA, la CIA et Disney.
# 
# Le langage Python , est un de langage Interprété et dynamique. Il support la programmation orienté objet et il est interfacable avec plusieurs autres langage de programmation. L'un des plus grands avantage de Python est sa lisibilite, la simplicite de sa syntaxe et une large communaute qui est deriere son developement.
# 
# ### Hello world!
# Commençons par créer un programme court qui affiche la fameuse phrase "Hello world!".
# En Python, on utilise la fonction `print` pour afficher du texte comme output.

# In[1]:


print("Hello world!")


# Exercice: Ecrire un programme qui permet d'afficher "Bonjour tout le monde!".

# In[54]:


# votre code ici


# ### Les operations arithemetique en Python
# Dans sa forme la plus élémentaire, Python peut être utilisé tout simpliement comme une `calculatrice`. Il peut relaiser les opérations arithmétiques suivantes :
# - Addition : `+`
# - Soustraction : `-`
# - Multiplication : `*`
# - Division entière : `//`
# - Division : `/`
# - Exponentation : `**`
# - Modulo : `%`
# 
# On rappelle que la division entiere revoi le quotient de la division euclidienne et le modulo renvoie le reste de la division euclidienne. Par exemple 7 // 4 est 1; 7 % 4 est 3, 5//2 est 2; 5%2 est 1.
# 
# Commencons maitnant a programmer. Nous voulons calculer 1+5, 5-4, 4*3, (10+8)/3, 2\**4, 28//6 et 28%6;
# Comme dans la plupart des languages de programmation, on utilise les symboles suivants pour les operations mathematique:

# In[13]:


# addition
print(1+5)

# soustraction
print(5-4)

# multiplication
print(4*3)

# division
print((10+8)/3)

#exponentiation
print(2**4)

# division entiere
print(28//6)

# modulo
print(28%6)


# _**Note**_: Toute chose commencant par `#` est un **commentaire**, il sera ingnore par Python. Les commentaires sont une boone maniere de svoir ce qu'on fait ou pour que une autre personne sache ce qu'on fait.
# 
# ### Affectation et variable
# 
# Une variable est concept fondamental en programmation. Elle permet de stocker une valeur (par exemple  la valeur 2) ou un objet (par exemple une fonction, liste, tableau, vecteur, ...). Cela permet de l'utiliser ultérieurement pour accéder facilement à la valeur ou à l'objet qui est stocké dans cette variable.
# 
# On affecte une valeur a une variable on utilisant le symbole `=`. Si vous voulez stocker la valeur 4 dans une varaible nomee `ma_valeur` on peut faire comme suit:
# 

# In[15]:


# affecter la valeur 4 a la varaible ma_valeur
ma_valeur = 4
# afficher le contenu de la variable ma_valeur
print(ma_valeur)


# On peut faire toutes les operations susmentionnees avec les variables a la place de valeurs. Voici un exemple, le nombre des hommes dans la classe est 10 le nombre des femmes est 18.

# In[16]:


# affecter le nombre des etudiants de sexe masculin a la variable hommes
hommes = 10
#affecter le nombre des etudiants de sexe fiminin a la variable femmes
femmes = 18

# affecter le nombre total des etudiants a la variable total_etudiant
total_etudiant = hommes + femmes

# Aficher le nombre total d'etudiants
print(total_etudiant)


# Python supporte les opérateurs d'affectation suivants : `=`, `+ =`, `– =`, `*=`, `/=`, `%=`, `**=` et `//=`.
# 
# Le premier operateur. Les autres operateur ont la meme logique. Nous allons illustrer cette logique avex `+=` et vous alles comprendre l'utilisation des autres.
# 
# Supponsons que nous avons un variables (soit `var`) qui contient une valeur (soit, par exemple 2). Et pour une raison (vous allez conforenter plusieurs raisons dans la suite de ce cours) nous voulons que cette varaible recoit l'ancienne valeur (2) plus une nouvelle valeur (soit, par exemple 1). On peut faire ca avec l'operateur `=` comme suit:

# In[36]:


#la variable var contient la valeur 2
var = 2
# la varaible var recoit l'ancienne valeur plus 1
var = var +1
# afficher le contenu de la variable var
print(var)


# On peut faire la meme instruction avec l'operateur `+=` comme suit:

# In[37]:


#la variable var contient la valeur 2
var = 2
# la varaible var recoit l'ancienne valeur plus 1
var += 1
# afficher le contenu de la variable var
print(var)


# ### Types de données de base dans Python
# Il existe de nombreux types de donnees dans Python. Voic quelques uns les plus basiques :
#  
# - `float`: Les valeurs décimales telles que 10,15 (attention en utilise `.` comme decimal au lieu de `,`).
# - `int` (les nombres entiers)": les valeurs comme 8; 4; 10 sont des entiers (`int`). Les entiers font aussi partie des valeurs numeriques.
# - `bool` (les valeurs booléennes (`True` ou `False`) sont dites valeurs logiques.
# - `str` (les characteres, ou chaînes de characters). Les guillemets`"texte"` (ou encore les apostrophes `'texte'`) indiquent que `texte` est de type `str`.
# - `complex`(les nombre complexes):  sont les nombres contenant une partie reelle et une partie imaginaire. En mathematique, on note $i$ le nombre complexe dans le caree est egale a 1. Cependant, en Python, on utilise la lettre `j` (ou `J`) pour indiquer ce nombre. Par exemple, si on voulais ecrire le nombre `3+1.5i` (le nombre complexe dont la partie reelle est 3 et la partie imaginaire est 1.5) en python on ecrit `3 + 1.5j`.
# - `None`: type Le mot-clé `None` est utilisé pour définir une valeur nulle (pas 0), ou aucune valeur du tout. `None` n'est pas la même chose que `0`, `False` ou une chaîne vide `''`. `None` est un type de données en soi (`NoneType`) et la seule valeur qui peut être de type `None` est le mot-clé`None`.
# 
# Ces nous avons un varaible (ou meme une valeur) et nous voulons savoir son types de donnees, on utilise la fonction `type`. Il faut etre prudent lorsqu'on voulais faire des operations sur des variables si leur type n'est le meme!

# In[91]:


# cette instruction va afficher int
print(type(1))
# cette instruction va afficher float
print(type(1.5))

# cette instruction va afficher  bool
print(type(True))
# cette instruction va afficher str
print(type("bonjour"))

# cette instruction va afficher complex
print(type(5+17.89j))

# cette instruction va afficher NoneType
print(type(None))


# Sous Python, on peut aussi  définir une liste comme une collection d’éléments séparés par des virgules, l’ensemble étant enfermé dans des crochets `[ ]`. les elements de la liste peuvent etre de n'importe quel type. Voic un exemple d'un liste en python :`jour_et_nombre = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche', 0, 1, 5]`.

# In[51]:


#
jour_et_nombre = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche', 0, 1, 5]

#
print(jour_et_nombre)

#
print(type(jour_et_nombre))


# Lorsqu'on dit que les elements d'une liste peuvent contenir n'importe quel type, on ne rigole pas. Voici une illustration:

# In[53]:


# on peut avoir une liste contenant des listes comme des elements
# une premiere liste
list1 = [1, 3, 'bonjour']

# une deuxieme liste
list2 = [None, True, 3+2j, '']

# une troisieme list contenant list1 et list2 comme elements
list3 = [list1, list2]

# une quatrieme list contenant list1, list2, et list3 comme elements
list4 = [list1, list2, list3]

# afficher les listes
print(list1)
print(list2)
print(list3)
print(list4)


# ### Opérateurs logiques:
# En python, il exeste trois operateurs logiques: `or` qui signifie ou, `and` qui signifie et, et `not` qui signifie non.
# 
# Pour mieux illustrer ces operations, soient `var1= True` et `var2 = False`. Quel serait le resultat des instructions suivantes:
# - `var1 or var2`
# - `var1 and var2`
# - `not var1`
# - `(var1 and var2) or (not var2)` 

# In[38]:


# initialiser les deux variables
var1 = True; var2 = False # remarquer qu'on peut faire plusieures instructions dans un meme linge. Cependant, il est deconsille
#
print(var1 or var2)

#
print(var1 and var2)

#
print(not var1)

# 
print((var1 and var2) or (not var2))


# ### Opérateurs relationnels (tests):
# 
# En python, il exeste six opérateurs relationnels: 
# - `<` qui permet de tester si une valeur et strictement inferieure a une autre;
# - `<=` qui permet de tester si une valeur et inferieure ou egale a une autre;
# - `>` qui permet de tester si une valeur et strictement superieure a une autre;
# - `>=` qui permet de tester si une valeur et superieure ou egale a une autre;
# - `!=` ou `<>` qui permet de tester si une valeur est egale a une autre;
# - et `==` qui permet de tester l'egalite de deux valeurs.
# 
# Soient `var1 = 5`, `var2 = 2+3`, `var3 = 6`, `var4 = "bonjour"`, `var5 = True`. Quel serait le resultat des instructions suivantes:
# - `var1 == var2`;
# - `var2 != var4`;
# - `var3 > var1+ var2`;
# - `var3< var1 + var2`;

# In[47]:


#
var1 = 5; var2 = 2+3; var3 = 6; var4 = "bonjour"; var5 = True

#
print(var1 == var2)

#
print(var1 != var4)

#
print(var3 > var1 + var2)

#
print(var3 < var1 + var2)


# ### Affichage
# 
# Nous avons rencontré, dans ce qui precede, la fonction `print` qui affiche une chaîne de caractères (`print("Hello world!")`). 
# Pour avoir des informations sur la fonction `print` (eventuellement sur toute autre fonction en python) on utilise la fonction `help`.

# In[57]:


help(print)


# la fonction `print` peut prendre plusieur arguments, les valeurs de tout types de donnees, les variables, par defaut, le separateur entre les arguments est l'espace (`sep=' '`) et la fin de l'affichage est un retuour a la ligne (`end='\n'`). Dans les exemple suivnat nous allons voir comment cette fonction affiche plusieur arguments et nous allons modifier le separateur (sep) et la fin de l'affichage (end).

# In[58]:


#
print('Hello')
print('World')


# In[62]:


#
print('Hello','World')


# In[63]:


#
var1 = 'Hello'; var2 = 'World'
print(var1,var2)


# In[64]:


#
print(var1, end='')
print('World')


# In[65]:


#
print(var1, 'world', sep = '--')


# In[66]:


#
x = 10
print('la valeur de la variable x est',x, sep=': ')


# Nous allons revenir a la fonction `print` lorsque nous allons parler de `l'écriture formatée`. 
# ## Lecture d'informations
# Parfois, on est amene a ce que notre programme depend de intervention de l'utilisateur (entrée d'un paramètre, clic de souris sur un bouton, etc.). Dans un programme simple, on utilise la fonction `input`. Cette fonction invite l'utilisateur a entrer des donnees au clavier puis taper `<entrer>`. Lorsque le programme est execute, une case apparait a l'utilisateur pour entrer ces donner. Puis le programme continue a s'exucuter pour rendre un output. Les donnees entrees par l'utilisateur peuvent etre stockees dans une variable. Il est a noter que cette variable sera de type `str`. Donc, si l'on veut des donnees numeriques par exemple, on doit convertir cette variable au type de donne que nous souhaitons. Enfin, on peut y mettre comme argument un text qui oriente à l'utilisateur lors de l'entree des donnees. 
# Voici un exemple dont on demande a l'utilisateur d'entrer son nom.

# In[2]:


x = input()
print(x)


# Voici le meme exemple avec un message explicatif:

# In[3]:


x = input("Veuillez entrer votre nom ici: ")
print(x)


# Le type de la variable qui stock le contenu de `input` est toujours `str`:

# In[4]:


x = input("merci d'entrer un chiffre: ")
print(type(x))


# In[5]:


x = input("merci d'entrer True: ")
print(type(x))


# ## convertir les types de donnees
# Il existe plusieurs raison pour lesquelles nous somme devant l'obligation de convertir les types de donnees (une raison est celle de `input` que nous avons vu). Les fonctions qui servent a la conversion entre les types de donnees sont les suivantes:
# - `int()`: pour convertir un type de donees en entier;
# - `float()`: pour convertir un type de donnees en vergule floattante.
# - `str()`: pour convertir un types de donnes en chaine de caracteres;
# - et `bool()`: pour convertir les types de donnes en valeurs booleennes.
# 
# Les types de donnees `int` et `float` peuvent etre converti on tous autre type de donnees. La seule remarque est que la conversion d'un valeur de type `float` en `int` rend les chiffre avant la vegule (1.9 devient 1 apres conversion). Pour avoir l'entier le plus proche au nombre que nous voulons convertir, nous devons utiliser la fonction `round()`.

# In[25]:


# int() va renvoyer 1
print(int(1.9))
# round() va renvoyer 2
print(round(1.9))


# Prenons un exemple d'un nombre entier (`1`), un nombre en vergule flottante (`4.5`) et une valeur booleene (`True`)  puis voyons comment les convertir a chaque type de donnes que nous avons vu jusqu'a maintenant.

# In[60]:


x = 1
x_float = float(x)
x_str = str(x)
x_bool = bool(x)


print ("\t\tAvant convertion:", end="\n================\n")
print ("La valeur de x :", x, "\t\t\tLe type:", type(x), end="\n================\n")
print ("\t\t Apres convertion", end="\n================\n")
print ("vergule flotante. Valeur:", x_float, "\t\tLe type:", type(x_float), end="\n================\n")
print ("Chaine de caracteres. Valeur:", x_str, "\tLe type:", type(x_str), end="\n================\n")
print ("Valeur booleene. Valeur:", x_bool, "\t\tLe type:", type(x_bool), end="\n================\n")


# In[59]:


y = 4.5

y_int = int(y)
y_str = str(y)
y_bool = bool(y)

print ("\t\tAvant convertion:", end="\n================\n")
print ("La valeur de y :", y, "\t\t\tLe type:", type(y), end="\n================\n")
print ("\t\t Apres convertion", end="\n================\n")
print ("Entier. Valeur:", y_int, "\t\t\tLe type:", type(y_int), end="\n================\n")
print ("Chaine de caracteres. Valeur:", y_str, "\tLe type:", type(y_str), end="\n================\n")
print ("Valeur booleene. Valeur:", y_bool, "\t\tLe type:", type(y_bool), end="\n================\n")


# In[62]:


z = True
z_float = float(z)
z_str = str(z)
z_int = int(z)


print ("\t\tAvant convertion:", end="\n================\n")
print ("La valeur de z :", z, "\t\t\tLe type:", type(z), end="\n================\n")
print ("\t\t Apres convertion", end="\n================\n")
print ("vergule flotante. Valeur:", z_float, "\t\tLe type:", type(z_float), end="\n================\n")
print ("Chaine de caracteres. Valeur:", z_str, "\tLe type:", type(z_str), end="\n================\n")
print ("Entier. Valeur:", z_int, "\t\tLe type:", type(z_int), end="\n================\n")


# Le type de donnees `str` est un peu particulier. On doit fair attention lors de la conversion. Si la valeur est une chaine de caracteres qui contient des lettres (a, b,...) ou d'autres symboles (+, @, ...). la converstion en `int` ou `float` renvoi une erreur.

# In[85]:


x = "bonjour"
print(int(x))


# In[86]:


x = "bonjour"
print(float(x))


# ```{note}
# lorsqu'on convertit tout valeur (a l'exception de) on recoit `True`.
# ```

# In[88]:


print(bool("bonjour"))
print(bool("5"))
print(bool(1.5))

print(bool(0))
print(bool(''))
print(bool(None))
print(bool([]))


# In[89]:


type(None)


# In[8]:


z = "1.4"; u = True; v = "5"; w = "False"


# In[10]:


y_int = int(y)
print(y)
print(y_int)
print(type(y_int))


# In[ ]:


yy = float(y)
zz = float(z)
uu = float(u)
vv = float(v)
ww = float(z)


# <hr style="border:2px solid gray"> </hr>
# 
# ### Essayez vous-meme!
# 
# 1. Ordre des operations: quelle est selon vous le resulats de ces operations :$(4/2)^2\times 2 + 1$, $4/2^{(2\times 2)} + 1$, $4/2^2\times (2 + 1)$, $4/2^2\times 2 + 1$ ? verifier avec Python.
# 2. Un pere a une somme d'argent de 1554 dh, il veut la partager sur ses 9 enfants de maniere equitable et s'il reste quelque dirham, il va acheter des chocolat a 1 dh l'unite. combien chanque enfant va recevoir? combien d'unite de chocolat peut-il acheter avec le reste?
# 3. Quel est le type de donnees de valeurs suivantes:
#     - `1`
#     - `1.`
#     - `False`
#     - `"False"`
#     - `var1/var2` avec `var1 = 1` et `var2 = 2`

# In[35]:


# votre code ici


# There is a lot more that you can do with outputs (such as including interactive outputs)
# with your book. For more information about this, see [the Jupyter Book documentation](https://jupyterbook.org)
