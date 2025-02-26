import random

def vérification(m):
    """
    Cette fonction vérifie si un joueur a gagné ou si la partie est terminée sans gagnant.
    Elle prend en paramètre une grille de morpion représentée par une liste de listes (m).
    Elle renvoie 0 si un joueur a gagné ou si la partie est terminée sans gagnant, sinon elle renvoie 1.
    """
    
    # Vérification des lignes
    for i in range(0,3):
        if(m[i][0]==m[i][1]==m[i][2] and m[i][0] not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]):
            print('\nLe joueur',m[i][0],"gagne !\nBravo à toi !")
            return 0
   
    # Vérification des colonnes
    for i in range(0,3):
        if(m[0][i]==m[1][i]==m[2][i] and m[0][i] not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]):
            print('\nLe joueur',m[0][i],"gagne !\nBravo à toi !")
            return 0

    # Vérification de la diagonale principale
    if(m[0][0]==m[1][1]==m[2][2] and m[0][0] not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]):
        print('\nLe joueur',m[1][1],"gagne !\nBravo à toi !")
        return 0

    # Vérification de la diagonale secondaire
    if(m[0][2]==m[1][1]==m[2][0] and m[0][2] not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]):
        print('\nLe joueur',m[1][1],"gagne !\nBravo à toi !")
        return 0

    # Vérification si la partie est terminée sans gagnant
    for i in range(0,3):
        for j in range(0,3):
            if(m[i][j] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]):
                return 1
    print("\nLa partie est terminée, aucun joueur n'a gagné !\ndommage ! =D")
    
    return 0

def grille(m):
    """
    Cette fonction affiche la grille de morpion.
    Elle prend en paramètre une grille de morpion représentée par une liste de listes (m).
    Elle renvoie 1.
    """
    print("-------------")
    for i in range(0,3):
        print("|",m[i][0],"|",m[i][1],"|",m[i][2],"|")
        print("-------------")
    return 1

if __name__ == "__main__":
    # Définition de la grille
    m = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    
    # Sélection aléatoire du premier joueur
    j = random.choice(['x', '0'])
    print(f"\nLe jeu commence ! Le joueur '{j}' joue en premier.")
    
    # Affichage initial de la grille de morpion
    grille(m)

    # Boucle de jeu
    while(vérification(m)):
        choix = input("Choisissez le numéro d'une case entre 1 et 9 (q pour quitter): ")
        
        if choix.lower() == 'q':
            print("Merci d'avoir joué ! À bientôt !")
            break
        
        if not choix.isdigit():
            print("Entrée invalide. Veuillez entrer un chiffre entre 1 et 9.")
            continue
        
        case = int(choix)
        if(not(1<=case<=9)):
            print("Numéro de case invalide. Veuillez choisir entre 1 et 9.")
            continue
        
        # Calcul de la position de la case dans la grille
        case = case - 1
        x=case%3
        y=int((case-x)/3)
        
        # Vérification si la case est déjà jouée
        if(m[y][x] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]):
            m[y][x]=j
            j='0' if j=='x' else 'x'
            grille(m)
        else:
            print("Cette case est déjà jouée. Veuillez en choisir une autre.")