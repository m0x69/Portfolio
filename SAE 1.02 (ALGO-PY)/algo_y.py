from numpy import *
###################################
# Algorithme de tri par insertion.#
###################################
# Definition :	
"""
	Le tri par insertion est un algorithme de tri stable et en place. Il est considéré comme étant l'algorithme de tri 
le plus rapide lorsqu'il s'agit de trier de petites listes, ou des listes presque triées mais il est beaucoup 
plus lent lorsqu'il faut trier de grandes listes et il se retrouve loin derrière des algorithmes comme le tri rapide 
ou le tri fusion. Le tri par insertion peut etre utilisé en complément d'autres tris (il peut servir de module d'amélioration 
pour un tri rapide par exemple).
	Le tri par insertion va parcourir une liste ou un tableau et comparer chaque élément avec l'élément qui le suit. Si l'élément 
qui le suit est plus petit alors il permutera les deux valeurs et il recommencera à parcourir le tableau en revenant au début. 
De cette manière, le tri par insertion va trier la partie gauche du tableau et au fur et a mesure qu il avance, il va "insérer" chaque 
chiffre à l'intérieur de la partie triée du tableau.

	Cet algorithme de tri a donc une rapidité qui dépends de la taille du tableau avec une complexité temporelle de O(n²) dans le pire cas (et en moyenne)
et une complexité temporelle de O(n) dans le meilleur cas. Sa complexité spatiale est O(1).

	Le pire des cas pour cet algorithme serait d'avoir à trier un tableau trié à l'envers.

"""
# remplacer 'tab' par 'tab: [int]' au moment de rendre (le 'tab: [int]' cree une erreur)
def algo_a(tab, i: int, j: int) -> None: # foncttion permutation
	"""
	pre-condition: 0 <= i, j < len(tab)
	post-condition: ?
	"""
	tmp=tab[i]
	tab[i]=tab[j]
	tab[j]=tmp
	
	
def algo_main(tab) -> None:
	"""
	pre-condition : 
	post-condition : trie tab par ordre croissant
	"""
	x = 0
	while x < len(tab)-1:
		val = tab[x+1]
		i = x
		while i >= 0 and tab[i] > val:
			algo_a(tab,i+1,i)
			i -= 1
		x += 1
		# print(tab)
import timeit

"""
import timeit # pour mesurer le temps d'execution
# Test du tri
import random
def liste_aleatoire()->int:
	random_ints = []
	for i in range(10):
		random_ints.append(random.randint(0, 10))
	algo_main(random_ints)

def trois_test():
	print("TRI PAR INSERTION")
	print(timeit.timeit("algo_main([10,9,8,7,6,5,4,3,2,1])",setup="from __main__ import algo_main",number=100),"pire cas") # valeurs qui sont sensé etre le pire des cas

	print(timeit.timeit("liste_aleatoire()",setup="from __main__ import liste_aleatoire",number=100),"aleatoire") # valeurs qui sont aleatoires

	print(timeit.timeit("algo_main([1,2,3,5,4,6,8,7,9,10])",setup="from __main__ import algo_main",number=100),"meilleur cas") # valeurs qui sont sensé etre le meilleur cas

trois_test()

# Après les test, nous pouvons conclure que le cas aléatoire et le pire cas font bel et bien parti des ensembles de valeurs qui prennent le plus de temps à être triés.
# Parfois le cas aléatoire prends moins de temps que le meilleur cas mais ca n'est pas représentatif de la moyenne.
"""