#coding:Utf-8

class Categorie:
	""" Classe regroupant les catégorie des aliments """

	def __init__ (self, cate, bcateg = {},  **data):
		cate = list() #Liste d'une catégarie créée dans une liste de différents catégories

		"""	
			@DE KISSIE : 
				La liste des catégories ne peut être contenue dans une Classe, elle
				sera contenue dans un fichier.
		"""

		self._cate = [cate] # Liste contenant les catégories 
		self._aliment = [] # Liste contenant les aliments

		# Vérification que 'bcateg' est un dictionnaire exploitable

		if type(bcateg) not in (dict, Categorie): #  @DE KISSIE : --->  if not isinstance(bcateg, (dict, Categorie))

			raise TypeError("Le type attendu est un dictionnire de catégorie")

		# Récupération des données de 'bcateg'
		for cate in bcateg:
			self[cate] = bcateg[cate]

		# Récupération ds données de 'data'
		for cate in data:
			self[cate] = data[cate]

	def __repr__ (self):
		""" Methode pour traduit déférents donées dans un dictionnaire """

		chaine_categorie = "{"
		pass_first = True
		for cate, aliment in self.items():
			if not pass_first:
				chaine += ","
			else:
				pass_first = False
			chaine_categorie += repr(cate) + ": " + repr(aliment)
		chaine_categorie += "}"
		return chaine_categorie

	def __str__ (self):
		""" Methode fesant appelle à 'repr' qui permet de l'afficher sous forme de chaine de caractère
		"""

		return repr(self)

	def __contains__ (self, cate):
		""" Renvoie les differents type de catégorie """
		return cate in self._cate

	def __getitem__ (self, cate, aliment):
		""" Renvoie Les valeurs correspondant à la catégorie et aussi renvoie
		la valeur de l'aliment """
		if cate not in self._cate:
			raise KeyError("La catégorie {} ne se trouve pas dans la base de donnée".format(cate))
		else:
			indice = self._cate.index(cate)
			return self._aliment[indice]

	def __delitem__ (self, cate, aliment):
		""" Méthode pour supprimer un aliment ou vider une catégorie """
		# Vider une catégorie
		if cate not in self._cate:
			raise KeyError("La catégorie {} ne se trouve pas dans la base de donnée".format(cate))
		else:
			indice = self._cate.index(cate)
			del self._aliment[indice]
		# Supprimer un aliment
		if aliment not in self._aliment:
			raise KeyError("L'aliment {} ne se trouve pas dans la base d'aliment".format(aliment))
		else:
			indice = self._aliment.index(aliment)
			del self._aliment[indice]

	def __iter__ (self):
		""" Methode qui parcours les élément contenus dans une liste: la liste de catégorie 
		"""
		return iter(self._cate)
	def __add__ (self):
		""" Methode permettant d'ajouter un aliment dans une catégorie """
		if cate not in self._cate:
			raise KeyError("La catégorie {} n'existe pas dans la base de donnée".format(cate))
		else:
			for cate, aliment in self.items():
				self._cate[cate] = aliment

	def items (self):
		""" Renvoie un générateur contenant les catégories ainsi que les aliments
		qui y sont """
		for i, cate in enumerate(self._cate):
			aliment = self._aliment[i]
			yield (cate, aliment)

	def cates (self):
		""" Methode qui renvoie la liste des catégories """
		return list(self._cate)

	def food (self):
		""" Méthode qui renvoie la liste de tous les aliments de la base de données """
		return list(self._aliment)

#NB : S'il y a des probleme fais le moi savoir afin que je puisse me corriger aussi
#Merci

if __name__ == '__main__':
	new = Categorie("céréales")
	print(new)