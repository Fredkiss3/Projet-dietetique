#coding:Utf-8


class Menu:
    """ classe du menu qui regroupe les aliments choisis """
    def __init__ (self, bmenu = {}, **data_menu):
        """
            @DE KISSIE :
            -> Où se trouve l'attribut "nomMenu" ?

        """
        """ initialisation du menu """
        self._foods = [] # Liste contenant des aliments

        self.Qti_Cal = [] # Quantité de de Calcium
        self.Qti_Fer = [] # Quantité de Fer
        self.Qti_Iode = [] # Quantité d'Iode
        self.Qti_Magn = [] # Quantité de Magnésium
        self.Qti_Mang = [] # Quantité de Manganèse
        self.Qti_Pot = [] # Quantité de Potassium
        self.Qti_Sod = [] # Quantité de Sodium
        self.Qti_Souf = [] # Quantité de Souffre
        self.Qti_Zin = [] # Quantité de Zinc
            # microgramme
        self.Qti_VitA = [] # Quantité de Vitamine A
        self.Qti_VitB1 = [] # Quantité de Vitamine B1
        self.Qti_VitB2 = [] # Quantité de Vitamine B2
        self.Qti_VitB6 = [] # Quantité de Vtamine B6
        self.Qti_VitB9 = [] # Quantité de Vitamine B9
        self.Qti_VitC = [] # Quantité de Vitamine C
        self.Qti_VitD = [] # Quantité de Vitamine D
        self.Qti_VitPP = [] # Quantité de Vitamine PP
            # gramme
                # Quantité Acides Gras
        self.Qti_Poly = [] # Quantité de Polyinsaturés
        self.Qti_Mono = [] # Quantité de Mono-insaturés
        self.Qti_Satu = [] # Quantité de Saturés
                # Quantité Protéines
        self.Qti_Vege = [] # Quantité Végétales
        self.Qti_Ani = [] # Quantité Animals
                # Quantité Glucides
        self.Qti_Suc = [] # Quantité Sucre
        self.Qti_Ami = [] # Quantité Amidon
                # Quantité Lipides
        self.Qti_OAni = [] # Quantité Origine Animale
        self.Qti_OVege = [] # Quantité Origine Végétale

        self.Qti_Chol = [] # Quantité de CHolestérol (mg)

        self.Qti_Ener = [] # Energie en KiloJoules(kj) ou KiloCalorie(kcal)

        self.Qti_Fib = [] # Quantité de Fibre (mg)



        """
            @DE KISSIE : 
                - Selon cette syntaxe, tu n'as pas utilisé de dictionnaire ici mais
                    plutôt ce qu'on appelle un 'set'.
                    
                        Les dicos sont définis selon la syntaxe :
                            dico = {cle1 : valeur1 , cle2 : valeur2, cle3 : valeur3, ...}

                - Où sont définies les variables citées dans ce dico ?
                    (foods, Cals, Fer, ...)
        """

        # Dictionnaire qui accompagne l'aliment
        self.dfood = {foods, Cal, Fer, Iode,
                      Magn, Mang, Pot, Sod,
                      Souf, Zin, VitA, VitB1,
                      VitB2, VitB6, VitB9, VitC,
                      VitD, VitPP, Poly, Mono, Satu,
                      Vege, Ani, Suc, Ami, OAni, OVege,
                      Chol, Ener, Fib}

        """
            @DE KISSIE : 
                Ici la bonne syntaxe est : 
                -> if  not isinstance(bmenu, (dict, Menu)) :

        """
        # Vérification de 'bmenu' si c'est un dictionnaire
        if type(bmenu) not in (dict, Menu): 	# Ce n'est pas la syntaxe optimale
            raise TypeError("Le type attendu est un dictionnaire de menu")

        # Récupéraion des données de 'bmenu'
        for foods in bmenu:
            self[foods] = bmenu[foods]

        # Récupération des données de 'data_menu'
        for foods in data_menu:
            self[foods] = data_menu[foods]

    def __repr__ (self):
        """ Méthode pour traduire en chaine de caractère un dictionnaire """

        chaine_menu = "{"
        pass_menu = True
        for dfood in self.items():
            if not pass_menu:
                chaine_menu += "\n"
            else:
                chaine_menu += repr(foods) + "->" + repr(Cal) + "|" + repr(Fer) + "|" +\
                                 repr(Iode) + "|" + repr(Magn) + "|" + repr(Mang) + "|" + repr(Pot)

                chaine_menu += "|" + repr(Sod) + "|" + repr(Souf) + "|" + repr(Zin) + "|" + repr(VitA) + \
                               "|" + repr(VitB1) + "|" + repr(VitB2) + "|" + repr(VitB6) + "|" + repr(VitB9)

                chaine_menu += "|" + repr(VitC) + "|" + repr(VitD) + "|" + repr(VitPP) + "|" + repr(Poly) + \
                                "|" + repr(Mono) + "|" + repr(Satu) + "|" + repr(Vege) + "|"

                chaine_menu += repr(Ani) + "|" + repr(Suc) + "|" + repr(Ami) + "|" + repr(OAni) + "|" + \
                                 repr(OVege) + "|" + repr(Chol) + "|" +  repr(Ener) + "|" + repr(Fib)
        chaine_menu += "}"

        return chaine_menu

    def __str__ (self):
        """ Méthode fesant appelle à 'repr' pour afficher le dictionnaire """

        return repr(self)

    def __contains__ (self, foods):
        """ Renvoie les valeurs des différents aliments """

        return foods in self._foods

    def __getitem__ (self, foods, dfood):
        """ Renvoie Les valeurs correspondant à l'aliment """
        if foods not in self._foods:
            raise KeyError("L'aliment {} ne se trouve pas dans le menu".format(foods))
        else:
            indice = self._foods.index(foods)
            return self.dfood[indice]

    def __delitem__ (self, foods):
        """ Méthode pour supprimer un aliment ou vider un menu """
        # Vider un menu
        for foods in bmenu:
            indice = self._foods.index(foods)
            del self._foods[indice]
            indice = self.dfood.index(dfood)
            del self.dfood[dfood]
        # Supprimer un aliment
        if foods not in self._foods:
            raise KeyError("L'aliment {} ne se trouve pas dans le menu".format(foods))
        else:
            indice = self._foods.index(foods)
            del self._foods[indice]
            del self.dfood

    def __iter__ (self):
        """ Méthode qui parcourt tous les éléments contenus dans une liste """

        return iter(self._foods)

    def __add__ (self):
        """ Méthode pour ajouter un aliment dans le menu """
        if foods not in self._foods:
            raise KeyError("L'aliment {} n'existe pas dans la base de donnée".format(foods))
        else:
            for foods, dfood in self.items():
                self._foods[foods] = dfood

    def items (self):
        """ Renvoie un générateur contenant l'aliment ainsi que les les nutriments
        qui y sont """
        for i, foods in enumerate(self._foods):
            dfood = self.dfood[i]
            yield (foods, dfood)

    def eating (self):
        """ Methode qui renvoie la liste des aliments """
        return list(self._foods)

    def dictfood (self):
        """ Méthode qui renvoie la liste de tous les nutriments de la base de données """
        return list(self.dfood)



if __name__ == '__main__':
    Menu1 = Menu() # type: object
    print(Menu1)

#NB : S'il y a des probleme fais le moi savoir afin que je puisse me corriger aussi
#Merci
