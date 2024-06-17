
####### Trie Rapide #######

from numpy import *


def algo_a(tab, i: int, j: int) -> None:

	"""
	prÃ©-condition: 0 <= i, j < len(tab)
	post-condition: inverse 2 valeur d'un tableau au emplacements i et j
	"""
	tmp=tab[i]
	tab[i]=tab[j]
	tab[j]=tmp
	

def algo_b(tab, g, d, x) -> int:
	"""
	prÃ©-condition: 0 <= g < d < len(tab), 0 <= x <= d
	post-condition: sépare le tableau en 2 parties, les valeurs inférieurs à la valeur médiane du tableaux à gauche et les valeurs supérieurs à droite
	"""
	
	algo_a(tab, d, x) # inverse la valeur central du tableau avec la valeur de fin 
	j = g
	i = g
	while i < d:
		if tab[i] < tab[d]:
			algo_a(tab, i, j)
			j += 1
		i += 1
	algo_a(tab, d, j)
	return j
	
		
def algo_d(tab, g: int, d: int) -> None:
	"""
	prÃ©-condition: 0 <= g <= d < len(tab)
	post-condition: gére la récursivité du programme
	"""
	if g < d:
		m = (d+g)//2
		x = algo_b(tab,g,d,m)
		algo_d(tab,g,x-1) # appel recursif de la partie de gauche du tableau
		algo_d(tab, x+1, d)# appel recursif de la partie de droite du tableau
		
def algo_main(tab) -> int:
	"""
	prÃ©-condition: 
	post-condition : trie tab par ordre croissant
	"""
	algo_d(tab, 0, len(tab)-1)
	return tab


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
	print("TRI RAPIDE")
	print(timeit.timeit("algo_main([10,9,8,7,6,5,4,3,2,1])",setup="from __main__ import algo_main",number=100),"pire cas") # valeurs qui sont sensé etre le pire des cas

	print(timeit.timeit("liste_aleatoire()",setup="from __main__ import liste_aleatoire",number=100),"aleatoire") # valeurs qui sont aleatoires

	print(timeit.timeit("algo_main([1,2,3,5,4,6,8,7,9,10])",setup="from __main__ import algo_main",number=100),"meilleur cas") # valeurs qui sont sensé etre le meilleur cas

trois_test()
	
"""