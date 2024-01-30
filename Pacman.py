#https://kitao.github.io/pyxel/wasm/launcher/?run=KitsuneNoMegami.pyxels.Pacman&gamepad=enabled
#créer le labyrinthe par un dictionnaire de relation 
dictionnaire={(0,0):[(1,0),(0,1)],
              (1,0):[(0,0),(2,0)],
              (2,0):[(1,0),(3,0)],
              (3,0):[(4,0),(2,0),(3,1)],
              (4,0):[(3,0),(5,0)],
              (5,0):[(4,0),(6,0)],
              (6,0):[(5,0),(7,0)],
              (7,0):[(6,0),(7,1)],
              (8,0):[(8,1)],
              (9,0):[(10,0),(9,1)],
              (10,0):[(9,0),(11,0)],
              (11,0):[(10,0),(12,0)],
              (12,0):[(11,0),(13,0)],
              (13,0):[(12,0),(14,0),(13,1)],
              (14,0):[(13,0),(15,0)],
              (15,0):[(14,0),(16,0)],
              (16,0):[(15,0),(16,1)],
              (0,1):[(0,0),(0,2)],
              (1,1):[(2,1),(1,2)],
              (2,1):[(1,1),(2,2)],
              (3,1):[(3,0),(3,2)],
              (4,1):[(4,2),(5,1)],
              (5,1):[(4,1),(6,1),(5,2)],
              (6,1):[(5,1),(6,2)],
              (7,1):[(7,2),(7,0)],
              (8,1):[(8,0),(8,2)],
              (9,1):[(9,0),(9,2)],
              (10,1):[(11,1),(10,2)],
              (11,1):[(10,1),(12,1),(11,2)],
              (12,1):[(11,1),(12,2)],
              (13,1):[(13,0),(13,2)],
              (14,1):[(14,2),(15,1)],
              (15,1):[(14,1),(15,2)],
              (16,1):[(16,0),(16,2)],
              (0,2):[(0,3),(0,1)],
              (1,2):[(1,1),(2,2)],
              (2,2):[(2,1),(1,2)],
              (3,2):[(3,3),(3,1)],
              (4,2):[(4,1),(5,2)],
              (5,2):[(4,2),(6,2),(5,1)],
              (6,2):[(6,1),(5,2)],
              (7,2):[(7,1),(7,3)],
              (8,2):[(8,1)],
              (9,2):[(9,1),(9,3)],
              (10,2):[(10,1),(11,2)],
              (11,2):[(10,2),(11,1),(12,2)],
              (12,2):[(11,2),(12,1)],
              (13,2):[(13,1),(13,3)],
              (14,2):[(14,1),(15,2)],
              (15,2):[(14,2),(15,1)],
              (16,2):[(16,1),(16,3)],
              (0,3):[(1,3),(0,2),(0,4)],
              (1,3):[(0,3),(2,3)],
              (2,3):[(1,3),(3,3)],
              (3,3):[(4,3),(2,3),(3,2),(3,4)],
              (4,3):[(3,3),(5,3)],
              (5,3):[(4,3),(6,3),(5,4)],
              (6,3):[(5,3),(7,3)],
              (7,3):[(6,3),(7,2),(8,3)],
              (8,3):[(7,3),(9,3)],
              (9,3):[(10,3),(9,2),(8,3)],
              (10,3):[(9,3),(11,3)],
              (11,3):[(10,3),(11,4),(12,3)],
              (12,3):[(11,3),(13,3)],
              (13,3):[(12,3),(14,3),(13,2),(13,4)],
              (14,3):[(13,3),(15,3)],
              (15,3):[(14,3),(16,3)],
              (16,3):[(15,3),(16,2),(16,4)],
              (0,4):[(0,3),(0,5)],
              (1,4):[(2,4)],
              (2,4):[(1,4)],
              (3,4):[(3,3),(3,5)],
              (4,4):[(4,5)],
              (5,4):[(5,3),(5,5)],
              (6,4):[(7,4)],
              (7,4):[(6,4),(8,4)],
              (8,4):[(7,4),(8,5),(9,4)],
              (9,4):[(8,4),(10,4)],
              (10,4):[(9,4)],
              (11,4):[(11,3),(11,5)],
              (12,4):[(12,5)],
              (13,4):[(13,3),(13,5)],
              (14,4):[(15,4)],
              (15,4):[(14,4)],
              (16,4):[(16,3),(16,5)],
              (0,5):[(0,4),(1,5)],
              (1,5):[(0,5),(2,5)],
              (2,5):[(1,5),(3,5)],
              (3,5):[(3,4),(3,6),(2,5)],
              (4,5):[(4,4),(4,6)],
              (5,5):[(5,4),(6,5),(7,5)],
              (6,5):[(5,5),(7,5)],
              (7,5):[(6,5),(7,6)],
              (8,5):[(8,4),(8,6)],
              (9,5):[(10,5),(9,6)],
              (10,5):[(9,5),(11,5)],
              (11,5):[(10,5),(11,4)],
              (12,5):[(12,4),(12,6)],
              (13,5):[(13,4),(13,6),(14,5)],
              (14,5):[(13,5),(15,5)],
              (15,5):[(14,5),(16,5)],
              (16,5):[(15,5),(16,4)],
              (0,6):[(0,7),(1,6)],
              (1,6):[(0,6),(2,6),(1,7)],
              (2,6):[(1,6),(2,7)],
              (3,6):[(3,5),(3,7)],
              (4,6):[(4,5),(4,7),(5,6)],
              (5,6):[(4,6),(6,6)],
              (6,6):[(5,6)],
              (7,6):[(7,5),(7,7)],
              (8,6):[(8,5)],
              (9,6):[(9,5),(9,7)],
              (10,6):[(11,6)],
              (11,6):[(10,6),(12,6)],
              (12,6):[(11,6),(12,5),(12,7)],
              (13,6):[(13,5),(13,7)],
              (14,6):[(14,7),(15,6)],
              (15,6):[(14,6),(15,7),(16,6)],
              (16,6):[(15,6),(16,7)],
              (0,7):[(0,6),(0,8),(1,7)],
              (1,7):[(0,7),(1,6),(1,8),(2,7)],
              (2,7):[(1,7),(2,6),(2,8)],
              (3,7):[(3,6),(3,8)],
              (4,7):[(4,6),(4,8)],
              (5,7):[(5,8),(6,7)],
              (6,7):[(5,7),(7,7)],
              (7,7):[(6,7),(7,6),(8,7)],
              (8,7):[(7,7),(9,7),],
              (9,7):[(10,7),(9,6),(8,7)],
              (10,7):[(9,7),(11,7)],
              (11,7):[(10,7),(11,8)],
              (12,7):[(12,6),(12,8)],
              (13,7):[(13,6),(13,8)],
              (14,7):[(14,6),(14,8),(15,7)],
              (15,7):[(14,7),(16,7),(15,6),(15,8)],
              (16,7):[(15,7),(16,6),(16,8)],
              (0,8):[(0,7),(1,8)],
              (1,8):[(0,8),(1,7),(2,8)],
              (2,8):[(1,8),(2,7)],
              (3,8):[(3,7),(3,9)],
              (4,8):[(4,7)],
              (5,8):[(5,7),(5,9)],
              (6,8):[(6,9),(7,8)],
              (7,8):[(6,8),(7,9),(8,8)],
              (8,8):[(8,7),(9,8),(8,9)],
              (9,8):[(10,8),(9,9),(8,8)],
              (10,8):[(9,8),(10,9)],
              (11,8):[(11,7),(11,9)],
              (12,8):[(12,7)],
              (13,8):[(13,7),(13,9)],
              (14,8):[(14,7),(15,8)],
              (15,8):[(14,8),(16,8),(15,7)],
              (16,8):[(15,8),(16,7)],
              (0,9):[(1,9),(-1,9)],
              (1,9):[(0,9),(2,9)],
              (2,9):[(1,9),(3,9)],
              (3,9):[(3,8),(3,10),(2,9),(4,9)],
              (4,9):[(3,9),(5,9)],
              (5,9):[(5,8),(5,10),(4,9)],
              (6,9):[(6,8),(6,10),(7,9)],
              (7,9):[(6,9),(7,8),(7,10),(8,9)],
              (8,9):[(9,9),(7,9),(8,10),(8,8)],
              (9,9):[(8,9),(9,8),(9,10),(10,9)],
              (10,9):[(9,9),(10,8),(10,10)],
              (11,9):[(11,8),(11,10),(12,9)],
              (12,9):[(11,9),(13,9)],
              (13,9):[(13,8),(13,10),(12,9),(14,9)],
              (14,9):[(13,9),(15,9)],
              (15,9):[(14,9),(16,9)],
              (16,9):[(15,9),(17,9)],
              (0,10):[(0,11),(1,10)],
              (1,10):[(0,10),(1,11),(2,10)],
              (2,10):[(1,10),(2,11)],
              (3,10):[(3,9),(3,11)],
              (4,10):[(4,11)],
              (5,10):[(5,9),(5,11)],
              (6,10):[(6,9),(7,10)],
              (7,10):[(6,10),(7,9),(8,10)],
              (8,10):[(7,10),(9,10),(8,9)],
              (9,10):[(10,10),(9,9),(8,10)],
              (10,10):[(9,10),(10,9)],
              (11,10):[(11,9),(11,11)],
              (12,10):[(12,11)],
              (13,10):[(13,9),(13,11)],
              (14,10):[(14,11),(15,10)],
              (15,10):[(14,10),(16,10),(15,11)],
              (16,10):[(15,10),(16,11)],
              (0,11):[(0,10),(0,12),(1,11)],
              (1,11):[(0,11),(1,10),(1,12),(2,11)],
              (2,11):[(1,11),(2,10),(2,12)],
              (3,11):[(3,10),(3,12)],
              (4,11):[(4,10),(4,12)],
              (5,11):[(5,10),(5,12),(6,11)],
              (6,11):[(5,11),(7,11)],
              (7,11):[(6,11),(8,11)],
              (8,11):[(7,11),(9,11)],
              (9,11):[(10,11),(8,11)],
              (10,11):[(9,11),(11,11)],
              (11,11):[(11,10),(11,12),(10,11)],
              (12,11):[(12,10),(12,12)],
              (13,11):[(13,10),(13,12)],
              (14,11):[(14,10),(14,12),(15,11)],
              (15,11):[(14,11),(16,11),(15,10),(15,12)],
              (16,11):[(15,11),(16,10),(16,12)],
              (0,12):[(0,11),(1,12)],
              (1,12):[(0,12),(1,11),(2,12)],
              (2,12):[(1,12),(2,11)],
              (3,12):[(3,11),(3,13)],
              (4,12):[(4,11)],
              (5,12):[(5,11),(5,13)],
              (6,12):[(7,12)],
              (7,12):[(6,12),(8,12)],
              (8,12):[(7,12),(9,12),(8,13)],
              (9,12):[(10,12),(8,12)],
              (10,12):[(9,12)],
              (11,12):[(11,11),(11,13)],
              (12,12):[(12,11)],
              (13,12):[(13,11),(13,13)],
              (14,12):[(14,11),(15,12)],
              (15,12):[(14,12),(16,12),(15,11)],
              (16,12):[(15,12),(16,11)],
              (0,13):[(1,13),(0,14)],
              (1,13):[(0,13),(2,13)],
              (2,13):[(1,13),(3,13)],
              (3,13):[(4,13),(2,13),(3,12),(3,14)],
              (4,13):[(3,13),(5,13)],
              (5,13):[(4,13),(6,13),(5,12)],
              (6,13):[(5,13),(7,13)],
              (7,13):[(6,13),(7,14)],
              (8,13):[(8,12),(8,14)],
              (9,13):[(10,13),(9,14)],
              (10,13):[(9,13),(11,13)],
              (11,13):[(10,13),(12,13),(11,12)],
              (12,13):[(11,13),(13,13)],
              (13,13):[(12,13),(14,13),(13,12),(13,14)],
              (14,13):[(13,13),(15,13)],
              (15,13):[(14,13),(16,13)],
              (16,13):[(15,13),(16,14)],
              (0,14):[(0,13),(0,15)],
              (1,14):[(2,14)],
              (2,14):[(1,14),(2,15)],
              (3,14):[(3,13),(3,15)],
              (4,14):[(5,14)],
              (5,14):[(4,14),(6,14)],
              (6,14):[(5,14)],
              (7,14):[(7,13),(7,15)],
              (8,14):[(8,13)],
              (9,14):[(9,13),(9,15)],
              (10,14):[(11,14)],
              (11,14):[(10,14),(12,14)],
              (12,14):[(11,14)],
              (13,14):[(13,13),(13,15)],
              (14,14):[(15,14),(14,15)],
              (15,14):[(14,14)],
              (16,14):[(16,13),(16,15)],
              (0,15):[(0,14),(1,15)],
              (1,15):[(0,15),(1,16)],
              (2,15):[(2,14),(2,16)],
              (3,15):[(3,14),(3,16),(4,15)],
              (4,15):[(3,15),(5,15)],
              (5,15):[(4,15),(5,16),(6,15)],
              (6,15):[(5,15),(7,15)],
              (7,15):[(6,15),(7,14),(8,15)],
              (8,15):[(7,15),(9,15)],
              (9,15):[(10,15),(9,14),(8,15)],
              (10,15):[(9,15),(11,15)],
              (11,15):[(10,15),(12,15),(11,16)],
              (12,15):[(11,15),(13,15)],
              (13,15):[(13,14),(13,16),(12,15)],
              (14,15):[(14,14),(14,16)],
              (15,15):[(16,15),(15,16)],
              (16,15):[(15,15),(16,14)],
              (0,16):[],
              (1,16):[(1,15),(1,17)],
              (2,16):[(2,15)],
              (3,16):[(3,15),(3,17)],
              (4,16):[(4,17)],
              (5,16):[(5,15),(5,17)],
              (6,16):[(7,16)],
              (7,16):[(6,16),(8,16)],
              (8,16):[(7,16),(9,16),(8,17)],
              (9,16):[(10,16),(8,16)],
              (10,16):[(9,16)],
              (11,16):[(11,15),(11,17)],
              (12,16):[(12,17)],
              (13,16):[(13,15),(13,17)],
              (14,16):[(14,15)],
              (15,16):[(15,15),(15,17)],
              (16,16):[],
              (0,17):[(0,18),(1,17)],
              (1,17):[(0,17),(1,16),(2,17)],
              (2,17):[(1,17),(3,17)],
              (3,17):[(2,17),(3,16)],
              (4,17):[(4,16),(4,18)],
              (5,17):[(5,16),(6,17)],
              (6,17):[(5,17),(7,17)],
              (7,17):[(6,17),(7,18)],
              (8,17):[(8,16),(8,18)],
              (9,17):[(10,17),(9,18)],
              (10,17):[(9,17),(11,17)],
              (11,17):[(10,17),(11,16)],
              (12,17):[(12,16),(12,18)],
              (13,17):[(13,16),(14,17)],
              (14,17):[(13,17),(15,17)],
              (15,17):[(14,17),(15,16),(16,17)],
              (16,17):[(15,17),(16,18)],
              (0,18):[(0,17),(0,19)],
              (1,18):[(2,18)],
              (2,18):[(3,18),(1,18)],
              (3,18):[(2,18),(4,18)],
              (4,18):[(3,18),(5,18),(4,17)],
              (5,18):[(4,18),(6,18)],
              (6,18):[(5,18)],
              (7,18):[(7,17),(7,19)],
              (8,18):[(8,17)],
              (9,18):[(9,17),(9,19)],
              (10,18):[(11,18)],
              (11,18):[(10,18),(12,18)],
              (12,18):[(11,18),(13,18),(12,17)],
              (13,18):[(12,18),(14,18)],
              (14,18):[(13,18),(15,18)],
              (15,18):[(14,18)],
              (16,18):[(16,17),(16,19)],
              (0,19):[(1,19),(0,18)],
              (1,19):[(0,19),(2,19)],
              (2,19):[(1,19),(3,19)],
              (3,19):[(4,19),(2,19)],
              (4,19):[(3,19),(5,19)],
              (5,19):[(4,19),(6,19)],
              (6,19):[(5,19),(7,19)],
              (7,19):[(6,19),(7,18),(8,19)],
              (8,19):[(7,19),(9,19)],
              (9,19):[(10,19),(9,18),(8,19)],
              (10,19):[(9,19),(11,19)],
              (11,19):[(10,19),(12,19)],
              (12,19):[(11,19),(13,19)],
              (13,19):[(12,19),(14,19)],
              (14,19):[(13,19),(15,19)],
              (15,19):[(14,19),(16,19)],
              (16,19):[(15,19),(16,18)],
              (-1,9):[(0,9)],
              (17,9):[(16,9)],
              }




#les positions des pieces là où il n'y a pas de mur 
piece_liste=[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(9,0),(10,0),(11,0),(12,0),(13,0),(14,0),(15,0),(16,0),
             (0,1),(3,1),(7,1),(9,1),(13,1),(16,1),
             (0,2),(3,2),(7,2),(9,2),(13,2),(16,2),
             (0,3),(1,3),(2,3),(3,3),(4,3),(5,3),(6,3),(7,3),(8,3),(9,3),(10,3),(11,3),(12,3),(13,3),(14,3),(15,3),(16,3),
             (0,4),(3,4),(5,4),(11,4),(13,4),(16,4),
             (0,5),(1,5),(2,5),(3,5),(5,5),(6,5),(7,5),(9,5),(10,5),(11,5),(13,5),(14,5),(15,5),(16,5),
             (3,6),(7,6),(9,6),(13,6),
             (3,7),(5,7),(6,7),(7,7),(8,7),(9,7),(10,7),(11,7),(13,7),
             (3,8),(5,8),(11,8),(13,8),
             (0,9),(1,9),(2,9),(3,9),(4,9),(5,9),(11,9),(12,9),(13,9),(14,9),(15,9),(16,9),
             (3,10),(5,10),(11,10),(13,10),
             (3,11),(5,11),(6,11),(7,11),(8,11),(9,11),(10,11),(11,11),(13,11),
             (3,12),(5,12),(11,12),(13,12),
             (0,13),(1,13),(2,13),(3,13),(4,13),(5,13),(6,13),(7,13),(9,13),(10,13),(11,13),(12,13),(13,13),(14,13),(15,13),(16,13),
             (0,14),(3,14),(7,14),(9,14),(13,14),(16,14),
             (0,15),(1,15),(3,15),(4,15),(5,15),(6,15),(7,15),(8,15),(9,15),(10,15),(11,15),(12,15),(13,15),(15,15),(16,15),
             (1,16),(3,16),(5,16),(11,16),(13,16),(15,16),
             (0,17),(1,17),(2,17),(3,17),(5,17),(6,17),(7,17),(9,17),(10,17),(11,17),(13,17),(14,17),(15,17),(16,17),
             (0,18),(7,18),(9,18),(16,18),
             (0,19),(1,19),(2,19),(3,19),(4,19),(5,19),(6,19),(7,19),(8,19),(9,19),(10,19),(11,19),(12,19),(13,19),(14,19),(15,19),(16,19),
             ]
#liste basé sur celle pour les pièces permettant de placer le bonus meme le joueur a déjà recupéré la piece à cet endroit
liste_bonus=list(piece_liste)



class Labyrinthe:
    def __init__(self,dict={}):
        """Constructeur de la classe
        dico est un dictionnaire où les clés sont les cellules et leurs valeurs sont les cellules voisines"""
        self.dico=dict
    
    def mur(self,cel1,cel2):
        return cel2 not in self.dico[cel1]
    
    def mur_droite (self,cel1):
        voisin= (cel1[0]+1,cel1[1])
        return self.mur(cel1,voisin)
    
    def mur_gauche(self,cel1):
        voisin= (cel1[0]-1,cel1[1])
        return self.mur(cel1,voisin)
    
    def mur_bas(self,cel1):
        voisin=(cel1[0],cel1[1]+1)
        return self.mur(cel1,voisin)
    
    def mur_haut(self,cel1):
        voisin=(cel1[0],cel1[1]-1)
        return self.mur(cel1,voisin)
    
    def ouvrir_passage(cel1,cel2):
        if self.mur(cel1,cel2):
            if cel1 not in self.dico[cel2] and cel2 not in self.dico[cel1]:
                self.dico[cel1].append(cel2)
                self.dico[cel2].append(cel1)
                
class Personnage:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
        self.direction=1
        self.vie=1
        
    def dessiner(self):#dessine la pacamn en fonction de la direction où il va
        if pyxel.frame_count % 20 > 10:
            pyxel.blt(self.x*CASE+2, self.y*CASE+2,0,16,16,16,16,0)
        else:
            if self.direction==3:
                pyxel.blt(self.x*CASE+2, self.y*CASE+2,0,0,0,-16,16,0)
            elif self.direction==2:
                pyxel.blt(self.x*CASE+2, self.y*CASE+2,0,16,0,16,16,0)
            elif self.direction==0:
                pyxel.blt(self.x*CASE+2, self.y*CASE+2,0,16,0,16,-16,0)
            else:
                pyxel.blt(self.x*CASE+2, self.y*CASE+2,0,0,0,16,16,0)
        
    def deplacement(self):
        if (pyxel.btnp(pyxel.KEY_LEFT) or  pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT)) and not lab.mur_gauche((self.x,self.y)):
            self.direction=3
        elif (pyxel.btnp(pyxel.KEY_RIGHT)  or  pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT)) and not lab.mur_droite((self.x,self.y)) :
            self.direction=1
        elif (pyxel.btnp(pyxel.KEY_DOWN)  or  pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN)) and not lab.mur_bas((self.x,self.y)):
            self.direction=2
        elif (pyxel.btnp(pyxel.KEY_UP)  or  pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP)) and not lab.mur_haut((self.x,self.y)):
            self.direction=0
            
        #régule sa vitesse   
        if self.direction==0 and not lab.mur_haut((self.x,self.y)) and pyxel.frame_count % 5 == 0:
            self.y-=1
        elif self.direction==1  and not lab.mur_droite((self.x,self.y)) and pyxel.frame_count % 5 == 0:
            self.x+=1
        elif self.direction==2 and not lab.mur_bas((self.x,self.y)) and pyxel.frame_count % 5 == 0:
            self.y+=1
        elif self.direction==3 and not lab.mur_gauche((self.x,self.y)) and pyxel.frame_count % 5 == 0:
            self.x-=1
            
        if self.x>16:
            self.x=0
        if self.x<0:
            self.x=16
            
            
    
    #vérifie s'il y a une contact avec un fantome
    def contact(self):
        if any((self.x,self.y) == (fantome.x, fantome.y) for fantome in liste_fantome):
            self.vie-=1
            
        
class Piece:#classe pour les pieces a récuperer
    def __init__(self,x=0, y=0):
        self.x=x
        self.y=y
        self.score=0
        
    def dessiner(self):
        pyxel.rect(self.x*CASE+7, self.y*CASE+7,3,3,14)
 
class Bonus:#classe pour les bonus de points
    def __init__(self,x=5,y=5):
        self.x=x
        self.y=y
        self.recupere = True
        
        
    def dessiner(self):#dessine une cerise
        pyxel.blt(self.x*CASE+2, self.y*CASE+2,0,0,17,15,16,0)
 
 
class Ennemi:#classe pour les 4 fantômes
    def __init__(self, x=0, y=0,s=10):
        self.x = x
        self.y = y
        self.speed=s
        self.indice=0
        self.old_case=(0,0)


    def dessiner(self, u,v):#dessine le fantome de la bonne couleur
        pyxel.blt(self.x*CASE+2, self.y*CASE+2,0,u,v,14,15,0)

    def deplacement_fantome(self, speed):
        directions = [(0, 1),(0, -1),(-1, 0), (1, 0)]
        direction_dispo=[]
        if pyxel.frame_count% speed == 0:
            if 8 <= self.y <= 10 and 6 <= self.x <= 10:#verifie qu'il se trouve dans la maison
                self.sortir_de_maison(speed)
            else:#remplit la liste des directions possible et en choisi une 
                for direction in directions:
                    nv_x, nv_y = self.x + direction[0], self.y + direction[1]
                   
                # Vérifier si la nouvelle position ne chevauche pas un mur ou un autre fantôme
                    if not lab.mur((self.x, self.y), (nv_x, nv_y)) and (nv_x,nv_y)!= self.old_case:
                        direction_dispo.append((nv_x,nv_y))
                #Choisi une case au hasard, qui n'est pas la case où il était avant   
                self.old_case=(self.x, self.y)
                if direction_dispo:
                    random.shuffle(direction_dispo)
                    self.x, self.y = direction_dispo[0][0],direction_dispo[0][1]
                        
            if self.x>16:
                self.x=0
            if self.x<0:
                self.x=16
                

    def sortir_de_maison(self,speed):#permet de sortir de la maison : la case du milieu
        if pyxel.frame_count % speed == 0 and not any(self.y-1 == fantome.y for fantome in liste_fantome):
        # Contrôle de la vitesse de sortie
            self.y -= 1

                    
        

import pyxel
import random
TITLE="PacMan"
WIDTH =255
HEIGHT=300
CASE=15
lab= Labyrinthe(dictionnaire)
points=Piece()
bonu=Bonus()
boule=Bonus()
win=False
start=False
perso= Personnage(8,11)
fantome1=Ennemi(8,7,10)
fantome2=Ennemi(7,9,15)
fantome3=Ennemi(8,9,30)
fantome4=Ennemi(9,9,20)
liste_fantome=[fantome1,fantome2,fantome3,fantome4]
pyxel.init(WIDTH,HEIGHT,title=TITLE,display_scale=2,quit_key=pyxel.KEY_ESCAPE)
pyxel.load("image.pyxres")


def draw():
    global start
    pyxel.cls(0)
    if perso.vie>0  and  start==True and not  win:
        
        #dessine les cases du labyrinthe 
        for case in lab.dico:
            if  lab.mur_droite(case):
                pyxel.rect(CASE*(case[0]+1),CASE*case[1],2,CASE,1)
            if  lab.mur_bas(case):
                pyxel.rect(CASE*case[0],CASE*(case[1]+1),CASE,2,1)
                
        #dessine les pieces       
        for  case in piece_liste:
             piece=Piece(case[0],case[1])
             piece.dessiner()
            
        #dessine le bonus    
        if not  bonu.recupere:
             bonu.dessiner()
        elif pyxel.frame_count*7 % 100==3:#pour que le bonus mette du temps a apparaitre
             bonu.recupere=False
        
        #dessine chaque entité ainsi que le score
        perso.dessiner()
        fantome1.dessiner(33,0)
        fantome2.dessiner(49,0)
        fantome3.dessiner(49,16)
        fantome4.dessiner(33,16)
        pyxel.text(5, 5, f"Score: { points.score}", 7)
    elif  start==False:
        pyxel.text(120, 100, "PACMAN", 10)
        pyxel.text(91, 145, "ESPACE POUR COMMENCER", 1)
        pyxel.text(90,145,"ESPACE POUR COMMENCER",7)
        if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
             start=True
        
#a modifier si vous voulez d'autre résultats en cas de réussite ou de perte 
    elif win==True:
        pyxel.text(116, 130, "YOU WIN", 1)#pour avoir une ombre
        pyxel.text(115,130,"YOU WIN",7)
        pyxel.text(110, 140, f"Score: {points.score}", 7)
    else:
        pyxel.text(116, 130, "GAME OVER", 1)#pour avoir une ombre
        pyxel.text(115,130,"GAME OVER",7)
        pyxel.text(110,140, f"Score: {points.score}", 7)
            
def update():
    global win
    if  perso.vie>0 and start==True and not  win:
        perso.deplacement()
        #récuperation des pièces
        if ( perso.x, perso.y) in piece_liste:
            piece_liste.remove((perso.x,perso.y))
            points.score+=100
                
        #condition de victoire       
        if piece_liste==[]:
            win=True
        #récuperation des bonus  
        if (perso.x,perso.y)==(bonu.x,bonu.y):
            bonu.recupere = True
            random.shuffle(liste_bonus)
            bonu.x,bonu.y=liste_bonus[0][0],liste_bonus[0][1]
            points.score+=1000
            
        #creer un tableau avec les fantome   
        for i,fantome in enumerate(liste_fantome):
            fantome.deplacement_fantome(fantome.speed)
            
        #évite un bug de mourir dès le début
        if points.score>300:
            perso.contact()

        
    
    
pyxel.run(update,draw)