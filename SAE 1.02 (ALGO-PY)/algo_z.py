from numpy import *

##############################
# Algorithme de tri cocktail.#
##############################
# Definition :
"""
Le Tri Cocktail est une version améliorée du Tri à Bulles. 
	Le tri à bulles consiste à parcourir le tableau de gauche 
à droite en comparant deux valeurs consécutives plusieursfois 
tant que le tableau n'est pas trié. 
	Le tri cocktail fonctionne de la même manière
mais il parcours aussi le tableau de droite à gauche, ce qui fait
gagner un allé retour au tri.

L'algorithme va donc déplacer l'élément le plus grand à son emplacement définitif
quand il parcourra le tableau de gauche à droite, et déplacera l'élément le plus petit
à son emplacement définitif quand il parcourra le tableau de droite à gauche.

Complexité : 
O(n²) dans le pire des cas ou dans les cas moyens.
O(n) quand la liste est presque ordonnée.

"""

# remplacer 'tab' par 'tab: [int]' au moment de rendre (le 'tab: [int]' cree une erreur)
def algo_main(tab) -> None:
	"""
	pre-condition : 
	post-condition : trie tab par ordre croissant
	"""
	d = 0
	f = len(tab)-1
	end = False
	while end == False:
		end = True
		i=0
		while i < f:
			if tab[i] > tab[i+1] :
				# print(tab, "test 1-")#test
				tmp = tab[i]
				tab[i]=tab[i+1]
				tab[i+1] = tmp # 1 err tab[i+1] et pas tab[i]
				end = False
			i += 1
		f -= 1
		i=f
		while i > d:
			if tab[i-1] > tab[i] :
				# print(tab, "test -2")#test
				tmp = tab[i]
				tab[i]=tab[i-1]
				tab[i-1] = tmp # 2 err tab[i-1] et pas tab[i]
				end = False
			i -= 1
		d += 1
		i=d # 3 err : mettre i à d pour partir de + haut


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
	print("TRI COCKTAIL")
	print(timeit.timeit("algo_main([10,9,8,7,6,5,4,3,2,1])",setup="from __main__ import algo_main",number=100),"pire cas") # valeurs qui sont sensé etre le pire des cas

	print(timeit.timeit("liste_aleatoire()",setup="from __main__ import liste_aleatoire",number=100),"aleatoire") # valeurs qui sont aleatoires

	print(timeit.timeit("algo_main([1,2,3,5,4,6,8,7,9,10])",setup="from __main__ import algo_main",number=100),"meilleur cas") # valeurs qui sont sensé etre le meilleur cas

trois_test()
"""