#!/usr/bin/env python
# coding: utf-8

# # Introduction
# 
# 
# ## Python
# 
# Python est un langage de programmation de haut niveau (high-level programming language), avec des applications dans de nombreux domaines, notamment la programmation Web, le calcul scientifique et l'intelligence artificielle !
# 
# Python est très populaire et utilisé par des organisations telles que Google, la NASA, la CIA et Disney.
# 
# Le langage Python est un de langage Interprété et dynamique. Il support la programmation orienté objet et il est ineffaçable avec plusieurs autres langages de programmation. L'un des plus grands avantages de Python est sa lisibilité, la simplicité de sa syntaxe et une large communauté qui est derrière son développement.
# 
# ## Hello world !
# Commençons par créer un programme court qui affiche la fameuse phrase "Hello world!".
# En Python, on utilise la fonction `print` pour afficher du texte comme output.

# In[1]:


print("Hello world!")


# Application : Ecrire un programme qui permet d'afficher "Bonjour tout le monde!".

# In[54]:


# votre code ici


# ## Les opérations arithmétiques en Python
# Dans sa forme la plus élémentaire, Python peut être utilisé tout simplement comme une `calculatrice`. Il peut réaliser les opérations arithmétiques suivantes :
# - Addition : `+`
# - Soustraction : `-`
# - Multiplication : `*`
# - Division entière : `//`
# - Division : `/`
# - Exponentiation : `**`
# - Modulo : `%`
# 
# On rappelle que la division entière renvoi le quotient de la division euclidienne et le modulo renvoie le reste de la division euclidienne. Par exemple 7 // 4 est 1; 7 % 4 est 3, 5//2 est 2; 5%2 est 1.
# 
# Commençons maintenant à programmer. Nous voulons calculer 1+5, 5-4, 4*3, (10+8)/3, 2\**4, 28//6 et 28%6;
# Comme dans la plupart des langages de programmation, on utilise les symboles suivants pour les opérations mathématiques:

# In[13]:


# addition
print(1+5)

# soustraction
print(5-4)

# multiplication
print(4*3)

# division
print((10+8)/3)

# exponentiation
print(2**4)

# division entière
print(28//6)

# modulo
print(28%6)


# ```{note}
# Toute chose commençant par `#` est un **commentaire**, il sera ignoré par Python. Les commentaires sont une bonne manière de savoir ce qu'on fait ou pour qu’une autre personne sache ce qu'on fait.
# ```
# ## Affectation et variables
# 
# Une variable est concept fondamental en programmation. Elle permet de stocker une valeur (par exemple la valeur 2) ou un objet (par exemple une fonction, liste, tableau, vecteur, ...). Cela permet de l'utiliser ultérieurement pour accéder facilement à la valeur ou à l'objet qui est stocké dans cette variable.
# 
# On affecte une valeur a une variable en utilisant le symbole `=`. Si vous voulez stocker la valeur 4 dans une variable nommée `ma_valeur` on peut faire comme suit :
# 

# In[15]:


# affecter la valeur 4 a la variable ma_valeur
ma_valeur = 4
# afficher le contenu de la variable ma_valeur
print(ma_valeur)


# On peut faire toutes les opérations susmentionnées avec les variables à la place de valeurs. Voici un exemple : Dans une classe, le nombre des hommes est 10 le nombre des femmes est 18.

# In[16]:


# Affecter le nombre des étudiants de sexe masculin à la variable hommes
hommes = 10
# Affecter le nombre des étudiants de sexe féminin à la variable femmes
femmes = 18

# Affecter le nombre total des étudiants à la variable total_etudiant
total_etudiant = hommes + femmes

# Afficher le nombre total d'étudiants
print(total_etudiant)


# Python supporte les opérateurs d'affectation suivants : `=`, `+ =`, `– =`, `*=`, `/=`, `%=`, `**=` et `//=`.
# 
# Hormis le premier opérateur `=`, les autres opérateurs ont la même logique. Nous allons illustrer cette logique avec `+=` et vous alles comprendre l'utilisation des autres.
# 
# Supposons que nous avons une variable (soit `var`) qui contient une valeur (soit, par exemple 2) et pour une raison (vous allez confronter plusieurs raisons dans la suite de ce cours) nous voulons que cette variable reçoive l'ancienne valeur (2) plus une nouvelle valeur (soit, par exemple 1). On peut faire ça avec l'opérateur `=` comme suit :

# In[36]:


# la variable var contient la valeur 2
var = 2
# la variable var reçoit l'ancienne valeur plus 1
var = var +1
# afficher le contenu de la variable var
print(var)


# On peut faire la même instruction avec l'opérateur `+=` comme suit :

# In[37]:


# la variable var contient la valeur 2
var = 2
# la variable var reçoit l'ancienne valeur plus 1
var += 1
# afficher le contenu de la variable var
print(var)


# ```{warning}
# Sous Python, les noms de variables doivent en outre obéir à quelques règles simples :
# - Un nom de variable est une séquence de lettres (a → z, A → Z) et de chiffres (0 → 9), qui doit
# **toujours commencer par une lettre**.
# - Seules les lettres ordinaires sont autorisées. Les lettres accentuées, les cédilles, les espaces, les caractères spéciaux tels que $, #, @, etc. sont interdits, à l'exception du caractère _ (souligné).
# - Python est "case sensitive" (les caractères majuscules et minuscules sont distingués). Par exemple : Var1, var1, VAR1 sont donc des variables différentes. 
# 
# - il est interdit d'utiliser comme nom de variables les mots réservés a python. Ils sont :
# **and, as, assert, break, class, continue, def,
# del, elif, else, except, False, finally, for,
# from, global, if, import, in, is, lambda,
# None, nonlocal, not, or, pass, raise, return,
# True, try, while, with, yield,**
# ```

# ## Types de données de base dans Python
# Il existe de nombreux types de données dans Python. Voici quelques-uns les plus basiques :
#  
# - `float`: Les valeurs décimales (ou en virgule flottante) telles que 10,15 (attention en utilise `.` comme décimal au lieu de `,`).
# - `int` (les nombres entiers)": les valeurs comme 8; 4; 10 sont des entiers (`int`). Les entiers font aussi partie des valeurs numériques.
# - `bool` (les valeurs booléennes (`True` ou `False`) sont dites valeurs logiques.
# - `str` (les caractères, ou chaînes de caractères). Les guillemets `"texte"` (ou encore les apostrophes `'texte'`) indiquent que `texte` est de type `str`.
# - `complex`(les nombre complexes):  sont les nombres contenant une partie réelle et une partie imaginaire. En mathématiques, on note $i$ le nombre complexe dans le carrée est égale à 1. Cependant, en Python, on utilise la lettre `j` (ou `J`) pour indiquer ce nombre. Par exemple, si on voulait écrire le nombre `3+1.5i` (le nombre complexe dont la partie réelle est 3 et la partie imaginaire est 1.5) en python on écrit `3 + 1.5j`.
# - `None`: type Le mot-clé `None` est utilisé pour définir une valeur nulle (pas 0), ou aucune valeur du tout. `None` n'est pas la même chose que `0`, `False` ou une chaîne vide `''`. `None` est un type de données en soi (`NoneType`) et la seule valeur qui peut être de type `None` est le mot-clé `None`.
# 
# si nous avons un variable (ou même une valeur) et nous voulons savoir son type de données, on utilise la fonction `type`. Il faut être prudent lorsqu'on voulait faire des opérations sur des variables si leur type n'est le même!

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


# Sous Python, on peut aussi définir une liste comme une collection d'éléments séparés par des virgules, l'ensemble étant enfermé dans des crochets `[ ]`. Les éléments de la liste peuvent être de n'importe quel type. Voici un exemple d'un liste en python :`jour_et_nombre = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche', 0, 1, 5]`.

# In[51]:


#
jour_et_nombre = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche', 0, 1, 5]

#
print(jour_et_nombre)

#
print(type(jour_et_nombre))


# Lorsqu'on dit que les éléments d'une liste peuvent contenir n'importe quel type, on ne rigole pas !! Voici une illustration :

# In[53]:


# on peut avoir une liste contenant des listes comme des éléments
# une première liste
list1 = [1, 3, 'bonjour']

# une deuxième liste
list2 = [None, True, 3+2j, '']

# une troisième liste contenante list1 et list2 comme éléments
list3 = [list1, list2]

# une quatrième liste contenante list1, list2, et list3 comme éléments
list4 = [list1, list2, list3]

# afficher les listes
print(list1)
print(list2)
print(list3)
print(list4)


# ## Opérateurs logiques :
# En python, il existe trois opérateurs logiques : `or` qui signifie ou, `and` qui signifie et, et `not` qui signifie non.
# 
# Pour mieux illustrer ces opérations, soient `var1= True` et `var2 = False`. Quel serait le résultat des instructions suivantes :
# - `var1 or var2`
# - `var1 and var2`
# - `not var1`
# - `(var1 and var2) or (not var2)`

# In[38]:


# initialiser les deux variables
var1 = True; var2 = False # remarquer qu'on peut faire plusieurs instructions dans une même linge. Cependant, il est déconseillé
#
print(var1 or var2)

#
print(var1 and var2)

#
print(not var1)

# 
print((var1 and var2) or (not var2))


# ## Opérateurs relationnels (tests) :
# 
# En python, il existe six opérateurs relationnels : 
# - `<` qui permet de tester si une valeur et strictement inférieure à une autre ;
# - `<=` qui permet de tester si une valeur et inférieure ou égale à une autre ;
# - `>` qui permet de tester si une valeur et strictement supérieure à une autre ;
# - `>=` qui permet de tester si une valeur et supérieure ou égale à une autre ;
# - `!=` ou `<>` qui permet de tester si une valeur est égale a une autre;
# - et `==` qui permet de tester l’égalité de deux valeurs.
# 
# Soient `var1 = 5`, `var2 = 2+3`, `var3 = 6`, `var4 = "bonjour"`, `var5 = True`. Quel serait le résultat des instructions suivantes :
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


# ## Affichage
# 
# Nous avons rencontré, dans ce qui précède, la fonction `print` qui affiche une chaîne de caractères (`print("Hello world!")`). 
# Pour avoir des informations sur la fonction `print` (éventuellement sur toute autre fonction en python) on utilise la fonction `help`.

# In[57]:


help(print)


# La fonction `print` peut prendre plusieurs arguments, les valeurs de tous types de données, les variables. Par défaut, le séparateur entre les arguments est l'espace (`sep=' '`) et la fin de l'affichage est un retour a la ligne (`end='\n'`). Dans les exemples suivants nous allons voir comment cette fonction affiche plusieurs arguments et nous allons modifier le séparateur (sep) et la fin de l'affichage (end).

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


# Nous allons revenir à la fonction `print` lorsque nous allons parler de `l'écriture formatée`. 
# ## Lecture d'informations
# Parfois, on est amené a ce que notre programme dépend d’intervention de l'utilisateur (entrée d'un paramètre, clic de souris sur un bouton, etc.). Dans un programme simple, on utilise la fonction `input`. Cette fonction invite l'utilisateur à entrer des données au clavier puis taper `<entrer>`. Lorsque le programme est exécuté, une case apparait à l'utilisateur pour entrer ces donner. Puis le programme continue à s'exécuter pour rendre un output. Les données entrées par l'utilisateur peuvent être stockées dans une variable. Il est à noter que cette variable sera de type `str`. Donc, si l'on veut des données numériques par exemple, on doit convertir cette variable au type de donne que nous souhaitons. Enfin, on peut y mettre comme argument un texte qui oriente à l'utilisateur lors de l'entrée des données. 
# Voici un exemple dont on demande à l'utilisateur d'entrer son nom.

# In[2]:


x = input()
print(x)


# Voici le même exemple avec un message explicatif:

# In[3]:


x = input("Veuillez entrer votre nom ici: ")
print(x)


# Le type de la variable qui stocke le contenu de `input` est toujours `str`:

# In[4]:


x = input("merci d'entrer un chiffre: ")
print(type(x))


# In[5]:


x = input("merci d'entrer True: ")
print(type(x))


# ## convertir les types de données
# Il existe plusieurs raisons pour lesquelles nous somme devant l'obligation de convertir les types de données (une raison est celle de `input` que nous avons vu). Les fonctions qui servent à la conversion entre les types de données sont les suivantes :
# - `int()`: pour convertir un type de données en entier;
# - `float()`: pour convertir un type de données en virgule flottante.
# - `str()`: pour convertir un types de donnes en chaine de caractères;
# - et `bool()`: pour convertir les types de donnes en valeurs booléennes.
# 
# Les types de données `int` et `float` peuvent être convertis en tous autre type de données. La seule remarque est que la conversion d’une valeur de type `float` en `int` rend les chiffres avant la virgule (1.9 devient 1 après conversion). Pour avoir l'entier le plus proche au nombre que nous voulons convertir, nous devons utiliser la fonction `round()`.

# In[25]:


# int() va renvoyer 1
print(int(1.9))
# round() va renvoyer 2
print(round(1.9))


# Prenons un exemple d'un nombre entier (`1`), un nombre en virgule flottante (`4.5`) et une valeur booléenne (`True`) puis voyons comment les convertir à chaque type de donnes que nous avons vu jusqu'à maintenant.

# In[7]:


x = 1
x_float = float(x)
x_str = str(x)
x_bool = bool(x)

print ("\t\t\tAvant conversion", end="\n================\n")
print ("La valeur de x :", x, "\t\t\t\tLe type :", type(x), end="\n================\n")
print ("\t\t\t Après conversion", end="\n================\n")
print ("virgule flottante. \tValeur :", x_float, "\t\tLe type :", type(x_float), end="\n================\n")
print ("Chaine de caractères. \tValeur :", x_str, "\t\tLe type :", type(x_str), end="\n================\n")
print ("Valeur booléenne. \tValeur :", x_bool, "\t\tLe type :", type(x_bool), end="\n================\n")


# In[14]:


y = 4.5

y_int = int(y)
y_str = str(y)
y_bool = bool(y)

print ("\t\t\tAvant conversion", end="\n================\n")
print ("La valeur de y :", y, "\t\t\tLe type :", type(y), end="\n================\n")
print ("\t\t\tAprès conversion", end="\n================\n")
print ("Entier. \t\tValeur :", y_int, "\tLe type :", type(y_int), end="\n================\n")
print ("Chaine de caractères. \tValeur :", y_str, "\tLe type :", type(y_str), end="\n================\n")
print ("Valeur booléenne. \tValeur :", y_bool, "\tLe type :", type(y_bool), end="\n================\n")


# In[19]:


z = True
z_float = float(z)
z_str = str(z)
z_int = int(z)


print ("\t\t\tAvant conversion", end="\n================\n")
print ("La valeur de z :", z, "\t\t\tLe type :", type(z), end="\n================\n")
print ("\t\t\tAprès conversion", end="\n================\n")
print ("virgule flottante. \tValeur:", z_float, "\tLe type :", type(z_float), end="\n================\n")
print ("Chaine de caractères. \tValeur:", z_str, "\tLe type :", type(z_str), end="\n================\n")
print ("Entier. \t\tValeur:", z_int, "\tLe type :", type(z_int), end="\n================\n")


# Le type de données `str` est un peu particulier. On doit faire attention lors de la conversion. Si la valeur est une chaine de caractères qui contient des lettres (a, b,...) ou d'autres symboles (+, @, ...). La conversion en `int` ou `float` renvoi une erreur.

# In[85]:


x = "bonjour"
print(int(x))


# In[86]:


x = "bonjour"
print(float(x))


# ```{note}
# Lorsqu’on convertit tout valeur (à l'exception de`0`, `''`, `None`, `[]`, et tous les types composés ou structurés vides) on reçoit `True`.
# ```

# In[88]:


print(bool("bonjour"))
print(bool("5"))
print(bool(1.5))

print(bool(0))
print(bool(''))
print(bool(None))
print(bool([]))


# - Si la chaine de caractères est un nombre (par exemple `"1.4"`) on peut la convertir en `float`
# - Si la chaine de caractères est un nombre entier (par exemple `"5"`), on peut la convertir en `int`

# In[95]:


#
print(float("1.4"))
print(int("1"))


# Cependant, On ne peut pas convertir un nombre en virgule flottante directement en `int`

# In[96]:


print(int("1.4"))


# L'astuce est de le convertir en `float` puis en `int`:

# In[100]:


#
int(float("1.4"))

