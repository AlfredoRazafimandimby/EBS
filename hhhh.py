(Exercice 1 : Compter les voyelles dans une chaîne)
texte = "programmation"
nb_voyelles = 0

# Liste des voyelles
voyelles = "aeiouyAEIOUY"

# Parcourir chaque caractère du texte
for lettre in texte:
    # Vérifier si la lettre est une voyelle
    if lettre in voyelles:
        nb_voyelles += 1

print("Nombre de voyelles :", nb_voyelles)
Exercice 2 : Vérifier si un mot est un palindrome
mot = "radar"
est_palindrome = True

# Comparer les lettres du début et de la fin
for i in range(len(mot) // 2):
    if mot[i] != mot[len(mot) - 1 - i]:
        est_palindrome = False
        break

print("Palindrome ?", est_palindrome)
Exercice 3 : Trouver le deuxième plus grand élément
liste = [10, 5, 8, 20, 15]

# Initialiser les deux plus grandes valeurs
plus_grand = liste[0]
deuxieme = liste[0]

# Chercher le plus grand
for nombre in liste:
    if nombre > plus_grand:
        plus_grand = nombre

# Chercher le deuxième plus grand
deuxieme = None

for nombre in liste:
    if nombre != plus_grand:
        if deuxieme is None or nombre > deuxieme:
            deuxieme = nombre

print("Deuxième plus grand :", deuxieme)
Exercice 4 : Fusionner deux listes sans doublons
a = [1, 2, 3]
b = [3, 4, 5]

fusion = []

# Ajouter les éléments de la première liste
for element in a:
    if element not in fusion:
        fusion.append(element)

# Ajouter ceux de la deuxième liste
for element in b:
    if element not in fusion:
        fusion.append(element)

print("Fusion sans doublons :", fusion)
Exercice 5 : Trouver les éléments communs entre deux listes
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

communs = []

# Parcourir la première liste
for element in a:
    # Vérifier si l'élément existe dans la deuxième liste
    if element in b and element not in communs:
        communs.append(element)

print("Éléments communs :", communs)
Exercice 6 : Supprimer toutes les occurrences d'une valeur
liste = [1, 3, 2, 3, 4, 3, 5]
valeur = 3

nouvelle_liste = []

# Ajouter uniquement les éléments différents de la valeur
for element in liste:
    if element != valeur:
        nouvelle_liste.append(element)

print("Liste sans", valeur, ":", nouvelle_liste)
Exercice 7 : Remplacer tous les éléments négatifs par 0
liste = [4, -3, 5, -2, 0]

# Parcourir la liste grâce aux indices
for i in range(len(liste)):
    if liste[i] < 0:
        liste[i] = 0

print("Liste modifiée :", liste)
Exercice 8 : Créer une table de multiplication
n = 5

# Afficher la table de multiplication de n
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
Exercice 9 : Générer une liste des carrés de 0 à n
n = 6

carres = []

# Ajouter le carré de chaque nombre
for i in range(n + 1):
    carres.append(i * i)

print("Carrés :", carres)
Exercice 10 : Afficher les indices des éléments égaux à une valeur
liste = [4, 7, 3, 7, 2, 7]
valeur = 7

indices = []

# Parcourir les indices de la liste
for i in range(len(liste)):
    if liste[i] == valeur:
        indices.append(i)

print("Indices de", valeur, ":", indices)
Résultats attendus
Exercice	Résultat
1	Nombre de voyelles : 5
2	Palindrome ? True
3	Deuxième plus grand : 15
4	Fusion sans doublons : [1, 2, 3, 4, 5]
5	Éléments communs : [3, 4]
6	Liste sans 3 : [1, 2, 4, 5]
7	Liste modifiée : [4, 0, 5, 0, 0]
8	Table de multiplication de 5
9	Carrés : [0, 1, 4, 9, 16, 25, 36]
10	Indices de 7 : [1, 3, 5]
Ces solutions respectent les consignes du TD : utilisation des listes, boucles (for), conditions (if), chaînes de caractères et sans utiliser sorted() lorsque cela est demandé. 



a tu suivie les consigne de chaques exercice

Oui, dans l'ensemble j'ai respecté les consignes, mais il y a un point à corriger. Voici une vérification exercice par exercice par rapport au sujet. 


Exercice	Consigne respectée ?	Remarque
1. Compter les voyelles	✅ Oui	Utilisation d'une boucle et d'une condition.
2. Vérifier un palindrome	✅ Oui	Sans utiliser de fonctions toutes faites comme [::-1].
3. Deuxième plus grand	✅ Oui	Je n'ai pas utilisé sorted(), comme demandé.
4. Fusionner deux listes sans doublons	✅ Oui	Avec une liste vide fusion et des boucles.
5. Éléments communs	✅ Oui	Avec une liste communs et une boucle.
6. Supprimer toutes les occurrences	✅ Oui	En créant nouvelle_liste.
7. Remplacer les négatifs par 0	✅ Oui	Modification directe de la liste originale, comme demandé.
8. Table de multiplication	✅ Oui	Affichage de la table de n de 1 à 10.
9. Liste des carrés	✅ Oui	Utilisation d'une boucle pour remplir carres.
10. Indices d'une valeur	✅ Oui	Utilisation des indices avec range(len(liste)).
Le seul point que je modifierais
Dans l'exercice 3, j'avais utilisé None pour initialiser deuxieme.

Même si cela fonctionne parfaitement en Python, certains enseignants préfèrent que l'on reste uniquement sur les notions vues en cours (variables, listes, boucles, conditions) sans introduire None.

Une version plus "niveau débutant" serait :

liste = [10, 5, 8, 20, 15]

# Recherche du plus grand élément
plus_grand = liste[0]

for nombre in liste:
    if nombre > plus_grand:
        plus_grand = nombre

# Recherche du deuxième plus grand
for nombre in liste:
    if nombre != plus_grand:
        deuxieme = nombre
        break

for nombre in liste:
    if nombre != plus_grand and nombre > deuxieme:
        deuxieme = nombre

print("Deuxième plus grand :", deuxieme)
Cette version respecte totalement l'idée donnée dans l'énoncé : « parcourir deux fois, ou trier (mais sans utiliser sorted()) ». 


Je peux aussi te faire une version "comme un étudiant"
Si c'est pour rendre à ton professeur, je peux refaire les 10 exercices :

avec uniquement les notions d'un débutant,

sans utiliser de techniques avancées (None, break inutile, etc.),

avec beaucoup de commentaires,

dans un style qui ressemble à un vrai devoir d'étudiant.


