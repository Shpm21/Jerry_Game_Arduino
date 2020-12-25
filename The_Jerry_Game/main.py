import random
import pyfirmata
import tkinter as tk
from classes import*
import csv

pygame.init()
nameList = []
pointsList = []

def saveList(nameList, pointsList):
    with open("Dates.csv", "w") as csvfile:
        write = csv.writer(csvfile)
        write.writerow(["Name","Point"])
        i = 0
        while i < len(nameList):
            row = [nameList[i], pointsList[i]]
            write.writerow(row)
            i +=1

def main():
    raiz = Windows()
    raiz.master.title("The Jerry Game")
    raiz.master.minsize(300,200)
    raiz.mainloop()
    saveList(nameList,pointsList)

class Windows(tk.Frame):
    #-------------CONSTRUCTOR----------------------
    def __init__(self, master=None):
        super().__init__(master)
        self.config(bg = "#282A36")
        self.place(relwidth = 1, relheight = 1)
        self.initializer()
        self.widget()  
    #------------METODOS--------------------------
    def initializer(self): #ACA INICIALIZAMOS EL ARDUINO  
        self.arduino = pyfirmata.Arduino("COM3") #DEBEN CAMBIAR EL PUERTO A SU PUERTO CORRESPONDIENTE
        self.it = pyfirmata.util.Iterator(self.arduino)
        self.it.start()
        self.left_button = self.arduino.get_pin("d:9:i")
        self.up_button = self.arduino.get_pin("d:10:i")
        self.down_button = self.arduino.get_pin("d:11:i")
        self.right_button = self.arduino.get_pin("d:12:i")
    #---------------------------------VENTANA TKINTER-----------------------------------------------------------
    def widget(self):   
        background_color = "#282A36"
        font_color = "#FFFFFF"
        self.entry_name_label = tk.Label(self, text = "Name:", bg = background_color, fg = font_color)
        self.entry_name_label.place(x = 0, y = 0)
        self.entry_name = tk.Entry(self)
        self.entry_name.place(x = 50, y = 3)
        self.start_button = tk.Button(self, text = "Start", width = 7, command = lambda: (self.str_name(), self.Jerry_Game()), bg = background_color, fg = font_color)
        self.start_button.place(x = 50, y = 30)
        self.finish_button = tk.Button(self, text = "Finish", width = 7, command = self.master.destroy, bg = background_color, fg = font_color)
        self.finish_button.place(x = 115, y = 30)
        self.console = tk.LabelFrame(self, text = "Console", height = 140, width = 300, bg = background_color, fg = font_color)
        self.console.place(x = 0, y =60)
        self.console_life_label = tk.Label(self.console, text = "Life:", bg = background_color, fg = font_color)
        self.console_life_label.place(x = 0, y = 20)
        self.console_life = tk.Label(self.console, text = "300", bg = background_color, fg = font_color)
        self.console_life.place(x = 30, y = 20)
        self.console_points_label = tk.Label(self.console, text = "Point:", bg = background_color, fg = font_color)
        self.console_points_label.place(x = 0, y = 40)
        self.console_points = tk.Label(self.console, text = "0", bg = background_color, fg = font_color)
        self.console_points.place(x = 35, y = 40)
        self.collide_label = tk.Label(self.console, text = " ", bg = background_color, fg = font_color)
        self.collide_label.place(x = 0, y =60)
        self.name_label = tk.Label(self.console, text = "Please, enter your name", bg = background_color, fg = font_color)
        self.name_label.place(x = 0, y = 0)

    def str_name(self):
        self.name = self.entry_name.get()
        self.name_label.config(text = ("Welcome", self.name))

    def Jerry_Game(self):
        #variables de la ventana
        self.screen_width = 600
        self.screen_height = 500
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.title = pygame.display.set_caption("The Jerry Game")
        self.background = pygame.image.load("Map_Design/Map.png").convert()
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.game_over = False
        #variables de jerry_Character
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
        #variables de la screw_Character y Jerry_heart
        self.coord_S_X = random.randint(0,550)
        self.coord_S_Y = random.randint(0,450)
        self.screw_Character = Screw((self.coord_S_X,self.coord_S_Y))
        self.Jerry_heart = Heart((500,10), self.Jerry_life)
        self.points = 0
        self.life_points = 0
        pygame.time.delay(300)
        while self.game_over == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.collide_label.config(text = " ")
                    self.console_points.config(text = "0")
                    self.console_life.config(text = "300")
                    self.name_label.config(text = "Please, enter your name")
                    self.game_over = True
            #Logica del juego
            self.random_enemy_x = random.randint(0,550)
            self.random_enemy_y = random.randint(0,450)
            self.random_screw_x = self.random_enemy_x
            self.random_screw_y = self.random_enemy_y
            self.counter_mov_enemy +=1 # este counter sirve para hacer que los enemy_Character se muevan (mirar el metodo "update" de la clase "Enemy")
            #Creando el movimiento de los sprites
            self.enemy_Character_1.update(self.counter_mov_enemy,1) #para entender esto mirar el metodo "update" de la clase "Enemy"
            self.enemy_Character_2.update(self.counter_mov_enemy,2) #para entender esto mirar el metodo "update" de la clase "Enemy"
            self.enemy_Character_3.update(self.counter_mov_enemy,3) #para entender esto mirar el metodo "update" de la clase "Enemy"
            self.Jerry_heart.update(True) #para entender esto mirar el metodo "update" de la clase "Heart"
            self.screw_Character.update(True) #para entender esto mirar el metodo "update" de la clase "Screw"
            #Para utilizar Arduino
            if self.left_button.read() == True: 
                    self.jerry_Character.update("left") #para entender esto mirar el metodo "update" de la clase "Jerry"
            if self.up_button.read() == True:
                    self.jerry_Character.update("up") #para entender esto mirar el metodo "update" de la clase "Jerry"
            if self.right_button.read() == True:
                    self.jerry_Character.update("right") #para entender esto mirar el metodo "update" de la clase "Jerry"
            if self.down_button.read() == True:
                    self.jerry_Character.update("down") #para entender esto mirar el metodo "update" de la clase "Jerry"
            #Para utlizar el teclado
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.jerry_Character.update("right")
                if event.key == pygame.K_LEFT:
                    self.jerry_Character.update("left")
                if event.key == pygame.K_UP:
                    self.jerry_Character.update("up")
                if event.key == pygame.K_DOWN:
                    self.jerry_Character.update("down")
            #Actualizando la imagen de los sprite en la pantalla
            self.screen.blit(self.background, [0,0])    
            self.screen.blit(self.screw_Character.image, self.screw_Character.rect)
            self.screen.blit(self.Jerry_heart.image, self.Jerry_heart.rect)
            self.screen.blit(self.jerry_Character.image, self.jerry_Character.rect)
            self.screen.blit(self.enemy_Character_1.image, self.enemy_Character_1.rect)
            self.screen.blit(self.enemy_Character_2.image, self.enemy_Character_2.rect)
            self.screen.blit(self.enemy_Character_3.image, self.enemy_Character_3.rect)
            #Detectando colisiones del Jerry_character con los enemy_Character/screw_Character
            if pygame.sprite.collide_mask(self.jerry_Character, self.enemy_Character_1):
                self.Jerry_heart.life -= 100 #SIRVE PARA QUE EL SPRITE DEL CORAZON SE ACTUALICE
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
                self.screw_Character.rect.x = self.random_screw_x
                self.screw_Character.rect.y = self.random_screw_y
                self.points += 1 #sumando puntos con la tuerca
                self.life_points +=1
                self.console_points.config(text = str(self.points))
            #recuperando vida al tener 3 tuercas
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
            self.update()
            pygame.display.flip()
            self.clock.tick_busy_loop(self.FPS)
        pygame.quit()
if __name__ == "__main__":
    main()
