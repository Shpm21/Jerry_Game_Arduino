import random
import pyfirmata
import time
import tkinter as tk
from clases import*
import csv

pygame.init()
nameList = []
pointsList = []

def saveList(lista1,lista2):
    with open("Dates.csv", "w") as f:
        w = csv.writer(f)
        w.writerow(["Name","Point"])
        i = 0
        while i < len(lista1):
            row = [nameList[i],pointsList[i]]
            w.writerow(row)
            i +=1

def main():
    raiz = tk.Tk()
    raiz.wm_title("The Jerry Game")
    windows(master=raiz)

class windows(tk.Frame):
    #-------------CONSTRUCTOR----------------------
    def __init__(self, master=None):
        super().__init__(master, master.minsize(300,200))
        self.master = master
        self.config(bg = "#282A36")
        self.place(relwidth = 1, relheight = 1)
        self.initialize() #QUITAR EL "#" DE "self.inicializar()" PARA PROBAR EL ARDUINO
        self.widget()  
        self.master.mainloop()
        saveList(nameList,pointsList)
    #------------METODOS--------------------------
    def initialize(self): #ACA INICIALIZAMOS EL ARDUINO  
        self.arduino = pyfirmata.Arduino("COM3") #DEBEN CAMBIAR EL PUERTO A SU PUERTO CORRESPONDIENTE
        self.it = pyfirmata.util.Iterator(self.arduino)
        self.it.start()
        self.left_button = self.arduino.get_pin("d:9:i")
        self.up_button = self.arduino.get_pin("d:10:i")
        self.right_button = self.arduino.get_pin("d:11:i")
        self.down_button = self.arduino.get_pin("d:12:i")
        
    #---------------------------------VENTANA TKINTER-----------------------------------------------------------
    def widget(self): 
        self.entry_name_label = tk.Label(self, text = "Name:", bg = "#282A36", fg = "#FFFFFF")
        self.entry_name_label.place(x = 0, y = 0)
        self.entry_name = tk.Entry(self)
        self.entry_name.place(x = 50, y = 3)
        self.start_button = tk.Button(self, text = "Start", width = 7, command = lambda: (self.str_name(), self.Jerry_Game()), bg = "#282A36", fg = "#FFFFFF")
        self.start_button.place(x = 50, y = 30)
        self.finish_button = tk.Button(self, text = "Finish", width = 7, command = self.master.destroy, bg = "#282A36", fg = "#FFFFFF")
        self.finish_button.place(x = 115, y = 30)
        self.console = tk.LabelFrame(self, text = "Console", height = 140, width = 300, bg = "#282A36", fg = "#FFFFFF")
        self.console.place(x = 0, y =60)
        self.console_life_label = tk.Label(self.console, text = "Life:", bg = "#282A36", fg = "#FFFFFF")
        self.console_life_label.place(x = 0, y = 20)
        self.console_life = tk.Label(self.console, text = "300", bg = "#282A36", fg = "#FFFFFF")
        self.console_life.place(x = 30, y = 20)
        self.console_points_label = tk.Label(self.console, text = "Point:", bg = "#282A36", fg = "#FFFFFF")
        self.console_points_label.place(x = 0, y = 40)
        self.console_points = tk.Label(self.console, text = "0", bg = "#282A36", fg = "#FFFFFF")
        self.console_points.place(x = 35, y = 40)
        self.collide_label = tk.Label(self.console, text = " ", bg = "#282A36", fg = "#FFFFFF")
        self.collide_label.place(x = 0, y =60)
        self.name_label = tk.Label(self.console, text = "Please, enter your name", bg = "#282A36", fg = "#FFFFFF")
        self.name_label.place(x = 0, y = 0)

    def str_name(self):
        self.name = self.entry_name.get()
        self.name_label.config(text = ("Welcome", self.name))

    def Jerry_Game(self):
        #variables de la ventana
        self.screen_width = 600
        self.screen_height = 500
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("The Jerry Game")
        self.background = pygame.image.load("Map_Design/Map.png").convert()
        self.clock = pygame.time.Clock()
        #variables del personaje
        self.Jerry_life = 300
        self.coord_Jerry_x = random.randint(0,550)
        self.coord_Jerry_y = random.randint(0,450)
        self.jerry_Character = Jerry((self.coord_Jerry_x, self.coord_Jerry_y), "Player_Design/Player.png")
        #variables de los enemy_Character
        self.counter_mov_enemy = 0
        self.coord_E1_X = random.randint(0,550)
        self.coord_E1_Y = random.randint(0,450)
        self.enemy_Character_1 = Enemy((self.coord_E1_X, self.coord_E1_Y), "Enemy_Design/Enemy.png")
        if self.enemy_Character_1.rect.colliderect(self.jerry_Character.rect): #si al iniciar el juego el enemigo esta en la posicion de Jerry, cambiar coordenadas
            self.enemy_Character_1.rect.x = random.randint(0,550)
            self.enemy_Character_1.rect.y = random.randint(0,450)
        self.coord_E2_X = random.randint(0,550)
        self.coord_E2_Y = random.randint(0,450)
        self.enemy_Character_2 = Enemy((self.coord_E2_X, self.coord_E2_Y), "Enemy_Design/Enemy.png")
        if self.enemy_Character_2.rect.colliderect(self.jerry_Character.rect): #si al iniciar el juego el enemigo esta en la posicion de Jerry, cambiar coordenadas
            self.enemy_Character_2.rect.x = random.randint(0,550)
            self.enemy_Character_2.rect.y = random.randint(0,450)
        self.coord_E3_X = random.randint(0,550)
        self.coord_E3_Y = random.randint(0,450)
        self.enemy_Character_3 = Enemy((self.coord_E3_X, self.coord_E3_Y), "Enemy_Design/Enemy.png")
        if self.enemy_Character_3.rect.colliderect(self.jerry_Character.rect): #si al iniciar el juego el enemigo esta en la posicion de Jerry, cambiar coordenadas
            self.enemy_Character_3.rect.x = random.randint(0,550)
            self.enemy_Character_3.rect.y = random.randint(0,450)
        #variables de la screw_Character
        self.coord_S_X = random.randint(0,550)
        self.coord_S_Y = random.randint(0,450)
        self.screw_Character = Screw((self.coord_S_X,self.coord_S_Y))
        self.points = 0
        self.life_points = 0
        #variables de la vida
        self.Jerry_heart = Heart((500,10), self.Jerry_life)
        self.game_over = False
        time.sleep(0.5)
        while self.game_over == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.collide_label.config(text = " ")
                    self.game_over = True
            #--------------------------LOGICA DEL VIDEOJUEGO------------------------------------
            self.random_enemy_x = random.randint(0,550)
            self.random_enemy_y = random.randint(0,450)
            self.random_screw_x = self.random_enemy_x
            self.random_screw_y = self.random_enemy_y
            self.counter_mov_enemy +=1 # este counter sirve para hacer que los enemy_Character se muevan (mirar el metodo "update" de la clase "Enemy")

            #refrescando los sprites
            self.enemy_Character_1.update(self.counter_mov_enemy,1) #para entender esto mirar el metodo "update" de la clase "Enemy"
            self.enemy_Character_2.update(self.counter_mov_enemy,2) #para entender esto mirar el metodo "update" de la clase "Enemy"
            self.enemy_Character_3.update(self.counter_mov_enemy,3) #para entender esto mirar el metodo "update" de la clase "Enemy"
            self.Jerry_heart.update(True) #para entender esto mirar el metodo "update" de la clase "Heart"
            self.screw_Character.update(True) #para entender esto mirar el metodo "update" de la clase "Bag"
            self.update_idletasks()
            self.update()

            #-PARA UTILIZAR ARDUINO
            if self.left_button.read() == True: 
                    self.jerry_Character.update("left") #para entender esto mirar el metodo "update" de la clase "Jerry"
            if self.up_button.read() == True:
                    self.jerry_Character.update("up") #para entender esto mirar el metodo "update" de la clase "Jerry"
            if self.right_button.read() == True:
                    self.jerry_Character.update("right") #para entender esto mirar el metodo "update" de la clase "Jerry"
            if self.down_button.read() == True:
                    self.jerry_Character.update("down") #para entender esto mirar el metodo "update" de la clase "Jerry"
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.jerry_Character.update("right")
                if event.key == pygame.K_LEFT:
                    self.jerry_Character.update("left")
                if event.key == pygame.K_UP:
                    self.jerry_Character.update("up")
                if event.key == pygame.K_DOWN:
                    self.jerry_Character.update("down")

            self.screen.blit(self.background, [0,0])    
            self.screen.blit(self.screw_Character.image, self.screw_Character.rect)
            self.screen.blit(self.Jerry_heart.image, self.Jerry_heart.rect)
            self.screen.blit(self.jerry_Character.image, self.jerry_Character.rect)
            self.screen.blit(self.enemy_Character_1.image, self.enemy_Character_1.rect)
            self.screen.blit(self.enemy_Character_2.image, self.enemy_Character_2.rect)
            self.screen.blit(self.enemy_Character_3.image, self.enemy_Character_3.rect)

            #detectando colisiones del Jerry_character con los enemy_Character/screw_Character
            if pygame.sprite.collide_mask(self.jerry_Character, self.enemy_Character_1):
                self.Jerry_heart.life -= 100
                self.Jerry_life -= 100
                self.console_life.config(text = str(self.Jerry_life))
                self.collide_label.config(text = "You have collided with Alpha")
                self.enemy_Character_1.rect.x = self.random_enemy_x 
                self.enemy_Character_1.rect.y = self.random_enemy_y
            if pygame.sprite.collide_mask(self.jerry_Character, self.enemy_Character_2):
                self.Jerry_heart.life -= 100
                self.Jerry_life -= 100
                self.console_life.config(text = str(self.Jerry_life))
                self.collide_label.config(text = "You have collided with Beta")
                self.enemy_Character_2.rect.x = self.random_enemy_x 
                self.enemy_Character_2.rect.y = self.random_enemy_y
            if pygame.sprite.collide_mask(self.jerry_Character, self.enemy_Character_3):
                self.Jerry_heart.life -= 100
                self.Jerry_life -= 100
                self.console_life.config(text = str(self.Jerry_life))
                self.collide_label.config(text = "You have collided with Gamma")
                self.enemy_Character_3.rect.x = self.random_enemy_x 
                self.enemy_Character_3.rect.y = self.random_enemy_y
            if pygame.sprite.collide_mask(self.jerry_Character, self.screw_Character):
                self.screw_Character.rect.x = self.random_screw_y
                self.screw_Character.rect.y = self.random_screw_y
                self.points += 1 #sumando puntos con la bolsita
                self.life_points +=1
                self.console_points.config(text = str(self.points))
            #recuperando vida al tener 3 bolsita
            if self.life_points == 3:
                self.Jerry_heart.life +=100
                self.Jerry_life += 100
                self.console_life.config(text = str(self.Jerry_life))
                self.life_points = 0
            if self.Jerry_life <= 0: #ACA SE CIERRA EL JUEGO
                nameList.append(self.name)
                pointsList.append(self.points)
                self.collide_label.config(text = " ")
                self.console_points.config(text = "0")
                self.console_life.config(text = "300")
                self.name_label.config(text = "Please, enter your name")
                self.game_over = True
            #reiniciando el counter enemy_Character
            if self.counter_mov_enemy == 400:
                self.counter_mov_enemy = 0

            pygame.display.flip()
            self.clock.tick_busy_loop(27)
        pygame.quit ()
            #--------------------------LOGICA DEL VIDEOJUEGO------------------------------------
if __name__ == "__main__":
    main()
