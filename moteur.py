

class Plateau:

    def __init__(self):
        for ligne in range(3):
            for colonne in range(3):
                self.plateau[ligne][colonne] = "vide"
        self.alignement = "null"
    
    def est_vide(self, ligne, colonne):
        if self.plateau[ligne][colonne] == "vide":
            return True
        return False
    
    def alignement(self):
        if (self.plateau[0][0] == self.plateau[0][1] == self.plateau[0][2] == "blanc" or
        self.plateau[0][0] == self.plateau[1][0] == self.plateau[2][0] == "blanc" or 
        self.plateau[2][0] == self.plateau[2][1] == self.plateau[2][2] == "blanc"  or 
        self.plateau[0][2] == self.plateau[1][2] == self.plateau[2][2] == "blanc" or 
        self.plateau[1][0] == self.plateau[1][1] == self.plateau[1][2] == "blanc" or 
        self.plateau[0][1] == self.plateau[1][1] == self.plateau[2][1] == "blanc" or 
        self.plateau[0][0] == self.plateau[1][1] == self.plateau[2][2] == "blanc" or
        self.plateau[0][2] == self.plateau[1][1] == self.plateau[2][0] == "blanc"):
            self.alignement = "blanc"
            return True
        elif (self.plateau[0][0] == self.plateau[0][1] == self.plateau[0][2] == "noir"
            or self.plateau[0][0] == self.plateau[1][0] == self.plateau[2][0] == "noir"
            or self.plateau[2][0] == self.plateau[2][1] == self.plateau[2][2] == "noir" 
            or self.plateau[0][2] == self.plateau[1][2] == self.plateau[2][2] == "noir"
            or self.plateau[1][0] == self.plateau[1][1] == self.plateau[1][2] == "noir"
            or self.plateau[0][1] == self.plateau[1][1] == self.plateau[2][1] == "noir"
            or self.plateau[0][0] == self.plateau[1][1] == self.plateau[2][2] == "noir"
            or self.plateau[0][2] == self.plateau[1][1] == self.plateau[2][0] == "noir"):
            self.alignement = "noir"
            return True
        return False


class Pion:

    def __init__(self, couleur):
        self.couleur = couleur

    def placer_pion(self, abscisse, ordonnee, plateau:Plateau):
        if plateau[abscisse][ordonnee] == "vide":
            self.abscisse = abscisse
            self.ordonnee = ordonnee
            plateau[abscisse-1][ordonnee] = "couleur"
            return True
        return False

    def changer_position(self, abscisse, ordonnee, plateau:Plateau):
        if plateau[abscisse][ordonnee] == "vide":
            plateau[self.abscisse][self.ordonnee] = "vide"
            self.abscisse = abscisse
            self.ordonnee = ordonnee
            plateau[self.abscisse][self.ordonnee] = "occupee"
            return True
        return False
    
    def deplacer_gauche(self):
        coup = self.changer_position(self.abscisse-1, self.ordonnee)
        return coup

    def deplacer_droite(self):
        coup = self.changer_position(self.abscisse+1, self.ordonnee)
        return coup
    
    def deplacer_bas(self):
        coup = self.changer_position(self.abscisse, self.ordonnee+1)
        return coup
    
    def deplacer_haut(self):
        coup = self.changer_position(self.abscisse, self.ordonnee-1)
        return coup

    def deplacer_gauche_bas(self):
        coup = self.changer_position(self.abscisse-1, self.ordonnee+1)
        return coup
    
    def deplacer_gauche_haut(self):
        coup = self.changer_position(self.abscisse-1, self.ordonnee-1)
        return coup

    def deplacer_droite_bas(self):
        coup = self.changer_position(self.abscisse+1, self.ordonnee+1)
        return coup
    
    def deplacer_droite_haut(self):
        coup = self.changer_position(self.abscisse+1, self.ordonnee-1)
        return coup


class Partie:

    def __init__(self):
        self.plateau = Plateau()
        self.blancs = [Pion("blanc") for in range(3)]
        self.noirs = [Pion("noir") for in range(3)]
    
    def estValide(self, ligne, colonne):
        return self.plateau.est_vide(ligne, colonne)

    def recuperer_position(self):
        print("Donner les coordonnées de la case")
        l = int(input("ligne : "))
        c = int(input("colonne : "))
        if not self.estValide(l, c):
            print("Les coordonnées rentrés ne sont pas valides!!\nveuillez rejouer :")
            self.recuperer_position()
        print("Votre coup est bien enregistré!!")

    def begin(self):
        # les blancs commencent
        pass



    
    
        
        