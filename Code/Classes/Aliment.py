# coding:utf-8

######################################################
#                                                    #
#       MODULE CONTENANT LA CLASSE 'Aliment'         #
#       auteurs : Frédhel Kissié + Ohui              #
#                                                    #
######################################################

"""
 Précision sur les propriétés :
  On ne peut laisser à l'utilisateur entrer les valeurs :
   - des rapports
   - de la somme d'acides gras saturés ou insaturés

  On empêche donc l'utilisateur de les rentrer, car on les calcule nous-même.
"""


class Aliment:
    """ Classe définissant le comportement des aliments """
    nb_aliments = 0  # Nombres d'aliments créés

    def __init__(self, name=""):
        """ Méthode de création de l'aliment, On peut donner un nom """
        # Augmenter l'indice pour montrer qu'un aliment a été créé
        Aliment.nb_aliments += 1

        # Nom de l'aliment
        if not name:
            self.name = "Aliment_{i:03}".format(i=Aliment.nb_aliments)
        else:
            self.name = name

        # Minéraux
        self.Qti_Calcium = 0
        self.Qti_Fer = 0
        self.Qti_Iode = 0
        self.Qti_Magnesium = 0
        self.Qti_Manganese = 0
        self.Qti_Potassium = 0
        self.Qti_Sodium = 0
        self.Qti_Souffre = 0
        self.Qti_Zinc = 0

        # Rapport Sodium/Potassium
        self._rapport_Na_K = 0

        # Vitamines
        self.Qti_VitA = 0
        self.Qti_VitB1 = 0
        self.Qti_VitB2 = 0
        self.Qti_VitB6 = 0
        self.Qti_VitB9 = 0
        self.Qti_VitC = 0
        self.Qti_VitD = 0
        self.Qti_VitPP = 0
        self.Qti_VitE = 0

        # Acides Gras
        self.Qti_AcidesG_Mono = 0
        self.Qti_AcideMyristique = 0  # Acides G. Saturés
        self.Qti_AcidePalmitique = 0
        self.Qti_Omega6 = 0  # Acides G. Poly-Insaturés
        self.Qti_Omega3 = 0

        # Rapport Omega3 / Omega6
        self._rapport_O3_O6 = 0

        # Acides G. Insaturés, Poly & Saturés
        self._AcidesG_Sat = 0
        self._AcidesG_Poly = 0
        self._AcidesG_Mono = 0

        # Constituants énergétiques
        self.Qti_Proteines_Veg = 0  # Protéines
        self.Qti_Proteines_Ani = 0
        self.Qti_Fructose = 0  # Glucides
        self.Qti_Sucre = 0
        self.Qti_Amidon = 0
        self.Qti_Lipides_Ani = 0  # Lipides
        self.Qti_Lipides_Veg = 0
        self._Qti_Energie = {'kj': 0, 'kcal': 0}

        # Autres
        self.Qti_Cholesterol = 0
        self.Qti_Fibres = 0
        self.Qti_ORAC = 0
        self.Qti_PRAL = 0
        self.Qti_Purines = 0
        self.Index_Insulinique = 0
        self.Index_Glycemique = 0
        self.Charge_Glycemique = 0

    def calcul_qtite(self, quantite: float, unite: str):
        """
            Fonction permettant de calculer la quantité des nutriments selon le poids de l'aliment et l'unité
            demandée.
            arguments :
                quantité : float
                unité : str -> soit 'kg', 'mg' ou 'g'
        """
        # On enlève le underscore('_') devant le nom des propriétés
        dico_proprietes = {'_rapport_O3_O6': self._rapport_O3_O6,
                           '_rapport_Na_K': self._rapport_Na_K,
                           '_AcidesG_Sat': self._AcidesG_Sat,
                           '_AcidesG_Mono': self._AcidesG_Mono,
                           '_AcidesG_Poly': self._AcidesG_Poly,
                           }
        # Dictionnaire à retourner
        dico = dict()

        # Pour accepter des unités en majuscule
        unite = unite.lower()

        if unite not in ['kg', 'g', 'mg']:
            raise ValueError("L'unité n'a que trois valeurs : 'kg', 'g' ou 'mg' ")

        # Conversion :
        if unite == "mg":
            quantite /= 1000  # On convertit en grammes -> 1g = 1000 mg
        elif unite == "kg":
            quantite /= 1e-3  # On convertit en grammes -> 1g = 10^(-3) Kg
        else:
            pass  # Si c'est déjà en grammes, on ne convertit pas

        # Calculs :
        for k, v in self.__dict__.items():
            if isinstance(v, (int, float)) and k not in dico_proprietes:
                dico[k] = (self.__dict__[k] * quantite) / 100

            # Cas de l'énergie
            elif k == '_Qti_Energie':
                energie_kj = v['kj'] * quantite / 100
                energie_kcal = energie_kj * 4.18
                dico['energie'] = {'kj': energie_kj, 'kcal': energie_kcal}

            # du côté des propriétés
            elif k in dico_proprietes:
                if k.startswith('_rapport'):
                    value = v
                else:
                    value = (v * quantite) / 100

                dico[k[1:]] = value

        # On retourne les valeurs que l'on a calculées
        return dico

    def set_values(self, dicovalues=None):
        """
            Méthode pour donner des valeurs à l'aliment
            arguments :
                dico des valeurs = { 'nom de l'attribut' : valeur }

            L'énergie doit être donnée de cette manière :
                dicovalues['energie'] = (valeur, unité)
        """

        if dicovalues is None:
            dicovalues = {}

        if not isinstance(dicovalues, dict):
            raise TypeError("L'argument en entrée doit être un dictionnaire !")
        else:
            for k, v in dicovalues.items():
                if k in self.__dict__:
                    self.__dict__[k] = v

            # Cas de l'énergie
            if 'energie' in dicovalues and isinstance(dicovalues['energie'], tuple):
                if len(dicovalues['energie']) == 2:
                    valeur, unite = dicovalues['energie']
                    self.set_energie(valeur, unite)

            # Appliquer les autres valeurs
            self.set_rapport_o3_o6()
            self.set_rapport_na_k()
            self.set_ag_poly()
            self.set_ag_sat()

    def return_values(self):
        """ Retourner les valeurs de l'aliment """

        # Pour enlever le '_' avant le nom de la propriété
        dico_proprietes = {'_rapport_O3_O6': self._rapport_O3_O6,
                           '_rapport_Na_K': self._rapport_Na_K,
                           '_AcidesG_Sat': self._AcidesG_Sat,
                           '_AcidesG_Mono': self._AcidesG_Mono,
                           '_AcidesG_Poly': self._AcidesG_Poly,
                           '_Qti_Energie': self._Qti_Energie
                           }

        # Dictionnaire de valeurs à retourner
        dico = dict()
        for k, v in self.__dict__.items():
            if k in dico_proprietes:
                attr = k[1:]
                dico[attr] = v
            else:
                dico[k] = v

        return dico

    def __add__(self, other):
        """ Additionner 2 aliments """
        if isinstance(other, Aliment):
            newalim = Aliment()
            dico = dict()

            for k, v in self.__dict__.items():
                if isinstance(v, (int, float)):
                    dico[k] = self.__dict__[k] + other.__dict__[k]

                # Cas de l'énergie
                elif k == '_Qti_Energie':
                    tup = (v['kcal'] + other._Qti_Energie['kcal']), 'kcal'
                    dico['energie'] = tup

                # Appliquer les valeurs au nouvel aliment
                newalim.set_values(dico)

            return newalim
        else:
            raise TypeError("Addition impossible entre ces objets !")

    def __iadd__(self, other):
        """ Additionner 2 aliments """
        newalim = self + other
        newalim.name = self.name
        return newalim

    def __sub__(self, other):
        """ Soustraire 2 aliments """
        if isinstance(other, Aliment):
            newalim = Aliment()
            dico = dict()

            for k, v in self.__dict__.items():
                if isinstance(v, (int, float)):
                    dico[k] = abs(self.__dict__[k] - other.__dict__[k])

                # Cas de l'énergie
                elif k == '_Qti_Energie':
                    tup = abs((v['kcal'] - other._Qti_Energie['kcal'])), 'kcal'
                    dico['energie'] = tup

                # Appliquer les valeurs au nouvel aliment
                newalim.set_values(dico)

            return newalim
        else:
            raise TypeError("Addition impossible entre ces objets !")

    def __isub__(self, other):
        """ Soustraire 2 aliments """
        newalim = self - other
        newalim.name = self.name
        return newalim

    def __repr__(self):
        """ Pour afficher un aliment """
        return self.name

    def __del__(self):
        """ Supprimer un aliment """
        # Diminuer le nombre d'aliments créés
        Aliment.nb_aliments -= 1
        del self

    # ############  PROPRIETES  ################

    # Accesseurs
    def get_rapport_na_k(self):
        """ Récupérer la valeur du rapport Sodium/Potassium"""
        return self._rapport_Na_K

    def get_rapport_o3_o6(self):
        """ Récupérer la valeur du rapport Oméga3/Oméga6 """
        return self._rapport_O3_O6

    def get_ag_sat(self):
        """ Récupérer la valeur de la quantité d'acides gras saturés """
        return self._AcidesG_Sat

    def get_ag_poly(self):
        """ Récupérer la valeur de la quantité d'acides gras polyinsaturés """
        return self._AcidesG_Poly

    def get_energie(self):
        """ Récupérer la quantité d'énergie """
        return self._Qti_Energie

    # Mutateurs
    def set_rapport_na_k(self):
        """ Calculer le rapport Sodium/Potassium """
        if self.Qti_Sodium > 0 and self.Qti_Potassium > 0:
            self._rapport_Na_K = self.Qti_Sodium / self.Qti_Potassium
        else:
            self._rapport_Na_K = 0

    def set_rapport_o3_o6(self):
        """ Calculer le rapport Oméga3/Oméga6 """
        if self.Qti_Omega3 > 0 and self.Qti_Omega6 > 0:
            self._rapport_O3_O6 = self.Qti_Omega3 / self.Qti_Omega6
        else:
            self._rapport_O3_O6 = 0

    def set_ag_sat(self):
        """ Calculer la somme des acides gras saturés """
        self._AcidesG_Sat = self.Qti_AcideMyristique + self.Qti_AcidePalmitique

    def set_ag_poly(self):
        """ Calculer la somme des acides gras polyinsaturés """
        self._AcidesG_Poly = self.Qti_Omega3 + self.Qti_Omega6

    def set_energie(self, *args):
        """
            Affecter des valeurs à l'énergie, elle convertie la valeur dans une unité
            ou l'autre
                arguments :
                    valeur : float
                    unite : str -> soit 'kj' ou 'kcal'
        """
        value = args[0]
        unite = args[1]

        if unite not in ['kj', 'kcal']:
            raise ValueError("L'unité ne peut être que 'kj' ou 'kcal' ")

        else:
            self._Qti_Energie[unite] = value

        if unite == 'kj':
            self._Qti_Energie['kcal'] = 4.18 * value
        else:
            self._Qti_Energie['kj'] = value / 4.18

    # Rapports
    rapport_na_k = property(get_rapport_na_k, set_rapport_na_k)
    rapport_o3_o6 = property(get_rapport_o3_o6, set_rapport_o3_o6)

    # Acides gras
    ag_sat = property(get_ag_sat, set_ag_sat)
    ag_poly = property(get_ag_poly, set_ag_poly)

    # Energie
    energie = property(get_energie, set_energie)


# ################################### POUR TESTER ##################################
if __name__ == '__main__':
    def afficher_aliment(aliment):
        print(80 * '-')
        print(aliment)
        print("Pour 100 grammes : ")
        print()
        for k, v in aliment.return_values().items():
            print("{k} : {v}".format(k=k, v=v))

        print()


    # Création d'aliments
    new = Aliment("Pain")  # Avec un nom
    new2 = Aliment()  # Sans nom

    # Ajout des valeurs à l'aliment
    new.set_values({
        'energie': (62.7, 'kcal'),
        'Qti_ORAC': 121,
        'Qti_Sucre': 12,
        'Qti_Amidon': 100,
        'Qti_Sodium': 24,
        'Qti_Potassium': 12,
        'Qti_Omega3': 12,
        'Qti_Omega6': 15,
    })

    # Afficher les caractéristiques de l'aliment
    afficher_aliment(new)

    # Afficher l'aliment
    print("Nom de l'aliment ", new)
    print()

    # Calcul de la quantité pour 1 grammes
    dic = new.calcul_qtite(1, 'G')
    print("Après calcul : ")
    print("'Qti_Omega3' = {o3}\n'Qti_Omega6' = {o6}\n'AcidesG_Poly' = {ag}".format(
        o3=dic['Qti_Omega3'],
        o6=dic['Qti_Omega6'],
        ag=dic['AcidesG_Poly'])
    )

    new2.set_values({
        'name': "Riz",
        'energie': (205, 'kj'),
        'Qti_ORAC': 11,
        'Qti_Sucre': 112,
        'Qti_Amidon': 150,
        'Qti_Sodium': 244,
        'Qti_Potassium': 112,
        'Qti_Omega3': 0.12,
        'Qti_Omega6': 0.915,
    })

    # Additionner deux aliments
    new2 += new

    # Supprimer l'aliment
    del new

    # Afficher les caractéristiques de l'aliment
    afficher_aliment(new2)

    # Calculer la quantité pour 1 kilogrammes
    dic = new2.calcul_qtite(1, 'kg')
    print("Après calcul : ")
    print("'Qti_Omega3' = {o3}\n'Qti_Omega6' = {o6}\n'AcidesG_Poly' = {ag}".format(
        o3=dic['Qti_Omega3'],
        o6=dic['Qti_Omega6'],
        ag=dic['AcidesG_Poly'])
    )

    # Pour plus d'informations
    help(Aliment)
