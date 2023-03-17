from tabulate import tabulate
import time
import random
score = {}

class Casino:

    def __init__(self,nom,solde):
        self.nom = nom
        self.solde = solde
        score[self.nom] = self.solde
        self.bienvenue()

    def bienvenue(self):
        #message de bienvenue
        print("═════════════════════════════════════════════════════════════════════════\n  ____  _                                      \n | __ )(_) ___ _ ____   _____ _ __  _   _  ___ \n |  _ \| |/ _ \ '_ \ \ / / _ \ '_ \| | | |/ _  \n | |_) | |  __/ | | \ V /  __/ | | | |_| |  __/\n |____/|_|\___|_| |_|\_/ \___|_| |_|\__,_|\___|\n                                               ")
        self.accueil()
        
    def accueil(self):
        print("═════════════════════════════════════════════════════════════════════════\n\n➜ Que voulez-vous faire ", self.nom, " ?\n")
        rep = input("[B] Jouer au blackjack\n[R] Jouer à la roulette\n[M] Jouer à la machine à sous\n\n[T] Afficher le tableau des plus gros joueurs\n[C] Consulter son solde\n\n[S] Sortir du casino\n═════════════════════════════════════════════════════════════════════════\n⮞ ").upper()
        if rep == "S":
            print("Enregistrement de vos résultats...")
            time.sleep(2.5)
            print("Vous êtes sorti du casino.")
        elif rep == "C":
            print("ᐅᐅᐅ Votre solde est de ", self.solde, " euros. ᐊᐊᐊ")
            time.sleep(2)
            self.accueil()
        elif rep == "R":
            self.roulette()
            score[self.nom] = self.solde
            self.accueil()
        elif rep == "B":
            print("Bienvenue sur la table de BlackJack ! ")
            self.blackjack()
            score[self.nom] = self.solde
            self.accueil()
        elif rep == "M":
            self.machine()
            score[self.nom] = self.solde
            self.accueil()
        elif rep == "T":
            self.tableau()
            self.accueil()
        else:
            print("⚠ Veuillez saisir un choix valide ⚠")
            time.sleep(1)
            self.accueil()

    def roulette(self):
        time.sleep(1)
        num, noir, rouge, pairs, impairs, multi, bille, rejoue =  [], [15,4,2,17,6,13,11,8,10,24,33,20,31,22,29,28,35,26], [32,19,21,25,34,27,36,30,23,5,16,1,14,9,18,7,12,3], [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36], [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35], 0, random.randint(0,36), "oui"
        while rejoue == "oui":
            num=[]
            bille = random.randint(0,36)
            choix = input("Où souhaitez vous miser ? ( numéro / couleur / pairs / impairs ) ⮞ ")
            if choix == "numéro":
                num.append(int(input("Veuillez saisir un numéro ⮞ ")))
                if num[0]<0:
                    num=[]
                    num.append(int(input("Veuillez saisir un numéro entre 0 et 36 ⮞ ")))
                elif num[0]>36:
                    num=[]
                    num.append(int(input("Veuillez saisir un numéro entre 0 et 36 ⮞ ")))
            elif choix == "couleur":
                couleur = input("Saisissez une couleur (rouge / noir / vert) ⮞ ")
                if couleur == "noir":
                    num = noir
                    multi = 2
                elif couleur == "rouge":
                    num = rouge
                    multi = 2
                elif couleur == "vert":
                    num.append(0)
                    multi = 35
                else:
                    couleur = input("Saisissez une couleur valide (rouge / noir / vert) ⮞ ")
            elif choix == "pairs":
                num = pairs
                multi = 2
            elif choix == "impairs":
                num = impairs
                multi = 2
            else :
                print("Veuillez saisir une mise valide ⮞ ")
                self.roulette()
            print("Vous avez ",self.solde," €.")
            bet = int(input("Combien souhaitez-vous miser ? ⮞ "))
            self.solde -= bet
            print("➜ La roue tourne...")
            time.sleep(1.5)
            print("—┬————┬—\n ",bille,"◯\n—┴————┴—")
            time.sleep(0.5)
            if bille in num:
                self.solde = self.solde + bet*multi
                print("Vous avez gagné ! Votre nouveau solde est ", self.solde, ".")
            else:
                print("Vous avez perdu ! Solde actuel : ", self.solde)
            rejoue = input("Voulez vous rejouer ? ⮞ ")

    def machine(self):
        mise, tours = int(input("Combien souhaitez-vous miser ? ⮞ ")), int(input("Combien de fois souhaitez-vous jouer ? ⮞ "))
        if mise*tours > self.solde or self.solde == 0:
            print("Vous n'avez pas assez d'argent.")
            time.sleep(2)
        else:
            self.solde = self.solde - mise*tours
            print("Le jeu commence !")
            time.sleep(1)
            for i in range(tours):
                symboles = ["☘", "☘", "☘", "☘", "🖤", "🖤", "🖤", "❼", "❼", "＄"]
                resultat = [random.choices(symboles), random.choices(symboles), random.choices(symboles)]
                print("┌―――――――――――――――――――――┐\nᐅ", resultat[0], resultat[1], resultat[2], "ᐊ\n└―――――――――――――――――――――┘")
                time.sleep(0.3)
                if resultat[0] == resultat[1] and resultat[0] == resultat[2]:
                    if resultat[0] == ['☘']:
                        self.solde = self.solde + mise*25
                        print("Vous avez gagné ", mise*25, "euros !")
                    elif resultat[0] == ['🖤']:
                        self.solde = self.solde + mise*50
                        print("Vous avez gagné ", mise*50, "euros !")
                    elif resultat[0] == ['❼']:
                        self.solde = self.solde + mise*177
                        print("Vous avez gagné ", mise*177, "euros !")
                    elif resultat[0] == ['＄']:
                        self.solde = self.solde + mise*1000
                        print("JACKPOT ! Vous avez gagné ", mise*1000, "euros !")
                else:
                    print("Vous avez perdu !")
                time.sleep(1.5)
         
    def blackjack(self):
        sabot, main_c, main_j = [1,2,3,4,5,6,7,8,9,10,10,10,10], 0, 0
        bet = int(input("Combien souhaitez-vous miser ? ⮞ "))
        if self.solde-bet < 0:
            print("Vous n'avez pas assez d'argent !")
            self.accueil()
        self.solde -= bet
        time.sleep(1)
        carte = random.choice(sabot)
        print("➜ Carte tirée par le joueur :\n┌—————┐\n│",carte,"\n│  ♠  │\n│  ",carte,"\n└—————┘")
        if carte == 1:
            main_j += 11
        else:
            main_j += carte
        time.sleep(1)
        carte = random.choice(sabot)
        print("➜ Carte tirée par le croupier :\n┌—————┐\n│",carte,"\n│  ♣  │\n│  ",carte,"\n└—————┘")
        if carte == 1:
            main_c += 11
        else:
            main_c += carte
        time.sleep(1)
        carte=random.choice(sabot)
        print("➜ Carte tirée par le joueur :\n┌—————┐\n│",carte,"\n│  ♥  │\n│  ",carte,"\n└—————┘")
        if carte == 1 and main_j+11 < 22:
            main_j += 11
        else:
            main_j += carte
        time.sleep(1)
        if main_j == 21:
            print("🎉BlackJack, vous avez gagné !🎉")
            time.sleep(1)
            self.solde += bet*2.5
            print("Solde actuel : ", self.solde)
            rejoue = input("Voulez vous rejouer ? ⮞ ")
            if rejoue == "oui":
                self.blackjack()
            else:
                self.accueil()
        else:
            print("▸ Votre main vaut : ", main_j , " et le croupier a : ", main_c,".")
            time.sleep(0.5)
            tour = input("Voulez vous tirer ou arreter ? ⮞ ")
        while tour == "tirer" and main_j < 21:
            carte = random.choice(sabot)
            print("➜ Carte tirée par le joueur :\n┌—————┐\n│",carte,"\n│  ♦  │\n│  ",carte,"\n└—————┘")
            time.sleep(0.5)
            if carte == 1 and main_j+11 < 22:
                main_j += 11
            else:
                main_j += carte
            print("▸ Votre main vaut : ", main_j)
            time.sleep(0.5)
            if main_j < 22:
                tour = input("Voulez vous tirer ou arreter ? ⮞ ")
        if main_j > 21:
            print("Vous avez perdu !")
            time.sleep(1)
            print("Solde actuel : ", self.solde)
            rejoue=input("Voulez vous rejouer ? ⮞ ")
            if rejoue == "oui":
                self.blackjack()
            else:
                self.accueil()
        while main_c < 17:
            carte = random.choice(sabot)
            print("➜ Carte tirée par le croupier :\n┌—————┐\n│",carte,"\n│  ♥  │\n│  ",carte,"\n└—————┘")
            time.sleep(1)
            if carte == 1 and main_c+11 < 22:
                main_c += 11
            else:
                main_c += carte
            print("▸ Main du croupier : ", main_c)
            time.sleep(1)
        if main_c > 21:
            print("🎉Vous avez gagné !🎉 ")
            self.solde += bet*2
            time.sleep(1)
            print("Solde actuel : ", self.solde)
            rejoue=input("Voulez vous rejouer ? ⮞ ")
            if rejoue == "oui":
                self.blackjack()
            else:
                self.accueil()
        elif main_j > main_c:
            print("🎉Vous avez gagné !🎉 ")
            self.solde += bet*2
            time.sleep(1)
            print("Solde actuel : ", self.solde)
            rejoue=input("Voulez vous rejouer ? ⮞ ")
            if rejoue == "oui":
                self.blackjack()
            else:
                self.accueil()
        elif main_c == main_j:
            print("Égalité !")
            self.solde += bet
            time.sleep(1)
            print("Solde actuel : ", self.solde)
            rejoue=input("Voulez vous rejouer ? ⮞ ")
            if rejoue == "oui":
                self.blackjack()
            else:
                self.accueil()
        elif main_c > main_j:
            print("Vous avez perdu ! ")
            time.sleep(1)
            print("Solde actuel : ", self.solde)
            rejoue=input("Voulez vous rejouer ? ⮞ ")
            if rejoue == "oui":
                self.blackjack()
            else:
                self.accueil()

    def tableau(self):
        time.sleep(1.5)
        soldes, tableau = [], [["Rang", "Nom", "Solde"]]
        for i in score:
            soldes.append(score[i])
        soldes.sort()
        soldes.reverse()
        for i in range(len(soldes)):
            for j in score:
                if score[j] == soldes[i]:
                    tableau.append([i+1, j, score[j]])
        print(tabulate(tableau , headers = "firstrow" , tablefmt = "grid"))
        input("\nAppuyez sur entrée pour revenir au menu principal. ")

joueur = Casino("Thomas",1500)
