# coding : utf-8

"""
Bonjour Ohui, Le fait est que je ne comprends pas du tout 
comment tu as fais tes classes. 

-> Je ne retrouve pas la méthode pour ajouter et donner des valeurs aux attributs de l'objet "Aliment" 
-> La méthode pour retourner les valeurs de l'objet "Aliment" est assée ambigüe 
-> La méthode pour additionner deux Aliments est tout aussi ambigüe 
-> Sans oublier La méthode pour soustraire deux Aliments 
-> Je n'ai pas retrouvé les attributs identifiants dans chacune des classes :
	nomAliment, nomCategorie & nomMenu.


Donne moi des exemples d'utilisation de tes classes pour que je sache comment les utiliser
-> Fais des modules de tests pour que je sache que tes méthodes marchent et comment elles marchent 

Par exemple : 
	Supposons que j'ai fait une classe "Telephone" :
"""


#
# Ceci est un module d'exemple, où 
# j'illustre comment on doit utiliser ma classe : 
#

class Telephone:
	def __init__(self, numero):
		...
		pass

	def appeler(self, numero):
		...
		pass

	def naviguer_sur_internet(self, volume_internet, unite):
		...
		pass


if __name__ == '__main__': 
	# Voici comment on utilise cette classe : 
	
	# Crée un téléphone avec un numéro sous forme de chaîne
	tel = Telephone("89 20 99 07")

	# Pour appeler, il faut indiquer le numéro sous forme de chaîne
	tel.appeler("87 20 45 10")

	# Pour naviguer sur internet, on indique le volume internet que l'on a sous forme
	# de réel ainsi que l'unité qui peut être 'Mb', 'Kb', 'Gb'

	tel.naviguer_sur_internet(15.12 , "Mb") # -> 15,12 Mégabytes



" @DE KISSIE :  Please fais moi un Module de test pour chaque Classe"