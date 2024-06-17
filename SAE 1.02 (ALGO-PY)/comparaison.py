import math

import algo_x as f1
import algo_y as f2
import algo_z as f3

import timeit # pour mesurer le temps d'execution
# Test du tri
import random

def liste_aleatoire_x(taille : int)->int:
	random_ints = []
	for i in range(taille):
		random_ints.append(random.randint(0, 100))
	f1.algo_main(random_ints)

def liste_aleatoire_y(taille : int)->int:
	random_ints = []
	for i in range(taille):
		random_ints.append(random.randint(0, 100))
	f2.algo_main(random_ints)

def liste_aleatoire_z(taille : int)->int:
	random_ints = []
	for i in range(taille):
		random_ints.append(random.randint(0, 100))
	f3.algo_main(random_ints)
def comparaison_graphique():
	# declaration des tableaux qui vont contenir les informations de temps d'execution
	temps_execution_5 = []
	temps_execution_10 = []
	temps_execution_50 = []
	temps_execution_100 = []
	temps_execution_500 = []
	temps_execution_1000 = []
	temps_execution_5000 = []
	temps_execution_10000 = []
	print("                  algo_x      algo_y      algo_z")
	# dans la partie suivante, nous allons sauvegarder le temps d'execution des algorithmes dans une variable temporaire afin de les tester avec plusieures tailles de tableaux
	# nous utiliserons une variable temporaire car nous avons besoin de la stocker uniquement le temps de l'ajouter dans le tableau
	# nous utiliserons aussi le round pour ne pas avoir trop de décimales et le format pour que le tableau s'affiche correctement dan lors de l'execution
	tmp = timeit.timeit("liste_aleatoire_x(5)", setup="from __main__ import liste_aleatoire_x", number=1)
	temps_execution_5 += [format((round(tmp,5)), '.6f')]
	tmp = timeit.timeit("liste_aleatoire_y(5)", setup="from __main__ import liste_aleatoire_y", number=1)
	temps_execution_5 += [format((round(tmp,5)), '.6f')]
	tmp = timeit.timeit("liste_aleatoire_z(5)", setup="from __main__ import liste_aleatoire_z", number=1)
	temps_execution_5 += [format((round(tmp,5)), '.6f')]

	print("Taille : 5    ",temps_execution_5)

	tmp = timeit.timeit("liste_aleatoire_x(10)", setup="from __main__ import liste_aleatoire_x", number=1)
	temps_execution_10 += [format((round(tmp,5)), '.6f')]
	tmp = timeit.timeit("liste_aleatoire_y(10)", setup="from __main__ import liste_aleatoire_y", number=1)
	temps_execution_10 += [format((round(tmp,5)), '.6f')]
	tmp = timeit.timeit("liste_aleatoire_z(10)", setup="from __main__ import liste_aleatoire_z", number=1)
	temps_execution_10 += [format((round(tmp,5)), '.6f')]

	print("Taille : 10   ",temps_execution_10)

	tmp = timeit.timeit("liste_aleatoire_x(50)", setup="from __main__ import liste_aleatoire_x", number=1)
	temps_execution_50 += [format((round(tmp,5)), '.6f')]
	tmp = timeit.timeit("liste_aleatoire_y(50)", setup="from __main__ import liste_aleatoire_y", number=1)
	temps_execution_50 += [format((round(tmp,5)), '.6f')]
	tmp = timeit.timeit("liste_aleatoire_z(50)", setup="from __main__ import liste_aleatoire_z", number=1)
	temps_execution_50 += [format((round(tmp,5)), '.6f')]

	print("Taille : 50   ",temps_execution_50)

	tmp = timeit.timeit("liste_aleatoire_x(100)", setup="from __main__ import liste_aleatoire_x", number=1)
	temps_execution_100 += [format((round(tmp,5)), '.6f')]
	tmp = timeit.timeit("liste_aleatoire_y(100)", setup="from __main__ import liste_aleatoire_y", number=1)
	temps_execution_100 += [format((round(tmp,5)), '.6f')]
	tmp = timeit.timeit("liste_aleatoire_z(100)", setup="from __main__ import liste_aleatoire_z", number=1)
	temps_execution_100 += [format((round(tmp,5)), '.6f')]

	print("Taille : 100  ",temps_execution_100)

	tmp = timeit.timeit("liste_aleatoire_x(500)", setup="from __main__ import liste_aleatoire_x", number=1)
	temps_execution_500 += [format((round(tmp,5)), '.6f')]
	tmp = timeit.timeit("liste_aleatoire_y(500)", setup="from __main__ import liste_aleatoire_y", number=1)
	temps_execution_500 += [format((round(tmp,5)), '.6f')]
	tmp = timeit.timeit("liste_aleatoire_z(500)", setup="from __main__ import liste_aleatoire_z", number=1)
	temps_execution_500 += [format((round(tmp,5)), '.6f')]

	print("Taille : 500  ",temps_execution_500)

	tmp = timeit.timeit("liste_aleatoire_x(1000)", setup="from __main__ import liste_aleatoire_x", number=1)
	temps_execution_1000 += [format((round(tmp,5)), '.6f')]
	tmp = timeit.timeit("liste_aleatoire_y(1000)", setup="from __main__ import liste_aleatoire_y", number=1)
	temps_execution_1000 += [format((round(tmp,5)), '.6f')]
	tmp = timeit.timeit("liste_aleatoire_z(1000)", setup="from __main__ import liste_aleatoire_z", number=1)
	temps_execution_1000 += [format((round(tmp,5)), '.6f')]

	print("Taille : 1000 ",temps_execution_1000)

	tmp = timeit.timeit("liste_aleatoire_x(5000)", setup="from __main__ import liste_aleatoire_x", number=1)
	temps_execution_5000 += [format((round(tmp,5)), '.6f')]
	tmp = timeit.timeit("liste_aleatoire_y(5000)", setup="from __main__ import liste_aleatoire_y", number=1)
	temps_execution_5000 += [format((round(tmp,5)), '.6f')]
	tmp = timeit.timeit("liste_aleatoire_z(5000)", setup="from __main__ import liste_aleatoire_z", number=1)
	temps_execution_5000 += [format((round(tmp,5)), '.6f')]

	print("Taille : 5000 ",temps_execution_5000)

	tmp = timeit.timeit("liste_aleatoire_x(10000)", setup="from __main__ import liste_aleatoire_x", number=1)
	temps_execution_10000 += [format((round(tmp,5)), '.6f')]
	tmp = timeit.timeit("liste_aleatoire_y(10000)", setup="from __main__ import liste_aleatoire_y", number=1)
	temps_execution_10000 += [format((round(tmp,5)), '.6f')]
	tmp = timeit.timeit("liste_aleatoire_z(10000)", setup="from __main__ import liste_aleatoire_z", number=1)
	temps_execution_10000 += [format((round(tmp,5)), '.6f')]

	print("Taille : 10000",temps_execution_10000)
	print("                  rapide    insertion    cocktail")
	print("")
	print("")

	# Conclusion sur les comparaisons :

	# Conversion en float des valeurs du tableau afin de pouvoir manipuler les chiffres et faire des opérations
	temps_tri_rapide = float(temps_execution_5[0])
	temps_tri_insertion = float(temps_execution_5[1])

	print("Pour des tableaux très courts, les algorithmes de tri cocktail et tri par insertion (qui sont du meme type) vont s'avérer plus efficaces que le tri rapide.")
	print("")
	print("     Quand le tableau est de taille 5 ou 10, les algorithmes de tri par insertion et tri cocktail sont ",format(temps_tri_rapide/temps_tri_insertion,'.3f')," fois plus rapides que le tri rapide car la liste à trier est relativement petite.")
	print("")
	temps_tri_rapide = float(temps_execution_50[0])
	temps_tri_insertion = float(temps_execution_50[1])
	print("A partir de tableaux de plus grande taille, les algorithmes de tri par insertion et tri cocktail deviennent de moins en moins efficaces, et l'algorithme de tri rapide commence a prouver son efficacité.")
	print("")
	print("     Quand le tableau est de taille 50, nous pouvons constater cela : l'algorithle de tri rapide est ",format(temps_tri_insertion/temps_tri_rapide,'.3f'),"fois plus rapide que l'algorithme de tri par insertion.")
	print("")
	print("Jusque là, la différence entre les algorithmes de tri par insertion et tri cocktail n'est pas à noter car soit leur temps d'execution est identique soit le temps d'execution le plus rapide alterne entre les deux algorithmes en fonction des tableaux générés.")
	print("")
	temps_tri_rapide = float(temps_execution_500[0])
	temps_tri_insertion = float(temps_execution_500[1])
	temps_tri_cocktail = float(temps_execution_500[2])
	print("La différence entre le tri par insertion et le tri cocktail commence à se faire sur des tableaux de plus en plus grands.")
	print("     Grâce à notre test sur un tableau de 500 entiers, nous avons pu repérer un écart récurrent entre le tri cocktail et le tri par insertion.")
	print("Quand le tableau est de taille 500, l'algorithme de tri par insertion est ",format(temps_tri_cocktail/temps_tri_insertion,'.3f')," fois plus rapide que le tri cocktail.")
	print("")
	temps_tri_rapide = float(temps_execution_10000[0])
	temps_tri_insertion = float(temps_execution_10000[1])
	temps_tri_cocktail = float(temps_execution_10000[2])
	print("Si nous faisons un saut dans l'analyse jusqu'au dernier test qui est une liste de taille 10 000, nous finissons avec un écart non négligeable entre chaque algorithme :")
	print("L'algorithme de tri rapide est",format(temps_tri_insertion/temps_tri_rapide,'.3f'),"fois plus rapide que l'algorithme de tri par insertion.")
	print("L'algorithme de tri rapide est",format(temps_tri_cocktail/temps_tri_rapide,'.3f'),"fois plus rapide que l'algorithme de tri cocktail.")
	print("L'algorithme de tri par insertion est",format(temps_tri_cocktail/temps_tri_insertion,'.3f'),"fois plus rapide que l'algorithme de tri cocktail.")
	print("")
	print("")
	# Création d'un graphique (entrer 'pip install matplotlib' dans le terminal pour avoir le module)
	import matplotlib.pyplot as plt
	import numpy as np

	sizes = [5, 10, 50, 100, 500, 1000, 5000, 10000]
	algo_x_times = [float(temps_execution_5[0]), float(temps_execution_10[0]), float(temps_execution_50[0]), float(temps_execution_100[0]), float(temps_execution_500[0]), float(temps_execution_1000[0]), float(temps_execution_5000[0]), float(temps_execution_10000[0])]
	algo_y_times = [float(temps_execution_5[1]), float(temps_execution_10[1]), float(temps_execution_50[1]), float(temps_execution_100[1]), float(temps_execution_500[1]), float(temps_execution_1000[1]), float(temps_execution_5000[1]), float(temps_execution_10000[1])]
	algo_z_times = [float(temps_execution_5[2]), float(temps_execution_10[2]), float(temps_execution_50[2]), float(temps_execution_100[2]), float(temps_execution_500[2]), float(temps_execution_1000[2]), float(temps_execution_5000[2]), float(temps_execution_10000[2])]

	plt.plot(sizes, algo_x_times, label="Tri Rapide")
	plt.plot(sizes, algo_y_times, label="Tri Insertion")
	plt.plot(sizes, algo_z_times, label="Tri Cocktail")

	plt.title("Temps d'exécution des algorithmes en fonction de la taille du tableau")
	plt.xlabel("Taille")
	plt.ylabel("Temps d'exécution (en secondes)")

	plt.legend()
	plt.show()

comparaison_graphique()