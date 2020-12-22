import pygame

class Player(pygame.sprite.Sprite): #CLASE PADRE
    def __init__(self, position, imagen):
        super().__init__()
        self.sheet = pygame.image.load(imagen)
        self.sheet.set_clip(pygame.Rect(0, 0, 80, 67))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
     #POSICIONES
        self.left_states = { 0: (0, 134, 80, 67), 1: (80, 134, 80, 67), 2: (160, 134, 80, 67),
                             3: (80, 134, 80, 67) }
        self.right_states = { 0: (0, 201, 80, 67), 1: (80, 201, 80, 67), 2: (160, 201, 80, 67),
                             3: (80, 201, 80, 67) }
        self.up_states = { 0: (0, 67, 80, 67), 1: (80, 67, 80, 67), 2: (160, 67, 80, 67),
                             3: (80, 67, 80, 67) }
        self.down_states = { 0: (0, 0, 80, 67), 1: (80, 0, 80, 67), 2: (160, 0, 80, 67),
                            3: (80, 0, 80, 67) }
     #ANIMACION
    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]
    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

class Enemy(Player): #ESTA CLASE DERIVA DE LA CLASE "Player"
    def update(self,counter_mov_enemy, state):
        mov_enemy = 5
        if state == 1: #Si el contador se encuentra entre 0 y 100 y el state es igual a 1 el personaje se movera de forma diferente al state 2 y 3
            if counter_mov_enemy >= 0 and counter_mov_enemy <= 100:
                self.clip(self.left_states)
                self.rect.x -= mov_enemy
            if counter_mov_enemy >= 101 and counter_mov_enemy <= 200:
                self.clip(self.right_states)
                self.rect.x += mov_enemy
            if counter_mov_enemy >= 201 and counter_mov_enemy <= 300:
                self.clip(self.up_states)
                self.rect.y -= mov_enemy
            if counter_mov_enemy >= 301 and counter_mov_enemy <= 400:
                self.clip(self.down_states)
                self.rect.y += mov_enemy 
        if state == 2: #Si el contador se encuentra entre 0 y 100 y el state es igual a 2 el personaje se movera de forma diferente al state 3 y 1
            if counter_mov_enemy >= 0 and counter_mov_enemy <= 100:
                self.clip(self.up_states)
                self.rect.y -= mov_enemy
            if counter_mov_enemy >= 101 and counter_mov_enemy <= 200:
                self.clip(self.down_states)
                self.rect.y += mov_enemy 
            if counter_mov_enemy >= 201 and counter_mov_enemy <= 300:
                self.clip(self.left_states)
                self.rect.x -= mov_enemy
            if counter_mov_enemy >= 301 and counter_mov_enemy <= 400:
                self.clip(self.right_states)
                self.rect.x += mov_enemy
        if state == 3: #Si el contador se encuentra entre 0 y 100 y el state es igual a 3 el personaje se movera de forma diferente al state 2 y 1
            if counter_mov_enemy >= 0 and counter_mov_enemy <= 100:
                self.clip(self.down_states)
                self.rect.y += mov_enemy 
            if counter_mov_enemy >= 101 and counter_mov_enemy <= 200:
                self.clip(self.up_states)
                self.rect.y -= mov_enemy
            if counter_mov_enemy >= 201 and counter_mov_enemy <= 300:
                self.clip(self.right_states)
                self.rect.x += mov_enemy
            if counter_mov_enemy >= 301 and counter_mov_enemy <= 400:
                self.clip(self.left_states)
                self.rect.x -= mov_enemy
     #ACA SE CREA EL EFECTO DE TRANSPORTACION POR LOS BORDES DE LA PANTALLA
        #Derecha
        if self.rect.x > 620:
            self.rect.x = -60
        #Izquierda
        if self.rect.x < -60:
            self.rect.x = 620
        #Arriba
        if self.rect.y > 520:
            self.rect.y = -60
        #Abajo
        if self.rect.y < -60:
            self.rect.y = 520
     #ACA SE CREA EL EFECTO DE TRANSPORTACION POR LOS BORDES DE LA PANTALLA
        self.image = self.sheet.subsurface(self.sheet.get_clip())

class Jerry(Player): #ESTA CLASE DERIVA DE LA CLASE "Player"
    def update(self, direction):
        if direction == "left":
            self.clip(self.left_states)
            self.rect.x -= 5
        if direction == "right":
            self.clip(self.right_states)
            self.rect.x += 5
        if direction == "up":
            self.clip(self.up_states)
            self.rect.y -= 5
        if direction == "down":
            self.clip(self.down_states)
            self.rect.y += 5

        if direction == "stand_left":
            self.clip(self.left_states[0])
        if direction == "stand_right":
            self.clip(self.right_states[0])
        if direction == "stand_up":
            self.clip(self.up_states[0])
        if direction == "stand_down":
            self.clip(self.down_states[0])
     #ACA SE CREA EL EFECTO DE TRANSPORTACION POR LOS BORDES DE LA PANTALLA
        #Derecha
        if self.rect.x > 620:
            self.rect.x = -60
        #Izquierda
        if self.rect.x < -60:
            self.rect.x = 620
        #Arriba
        if self.rect.y > 520:
            self.rect.y = -60
        #Abajo
        if self.rect.y < -60:
            self.rect.y = 520
     #ACA SE CREA EL EFECTO DE TRANSPORTACION POR LOS BORDES DE LA PANTALLA
        self.image = self.sheet.subsurface(self.sheet.get_clip())

class Screw(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.sheet = pygame.image.load("Screw_Design/Screw.png")
        self.sheet.set_clip(pygame.Rect(0, 0, 42, 42))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        #MOVIMIENTOS
        self.movement = { 0: (0, 0, 42, 42), 1: (0, 42 , 42, 42), 2: (0, 84, 42, 42),
                            3: (42, 0, 42, 42), 4: (42, 42, 42, 42), 5: (42, 84, 42, 42),
                            6: (84, 0, 42, 42), 7: (84, 42, 42, 42)}
    def get_frame(self, frame_set): #Este metodo es el encargado de hacer que la bolsa se sacuda sin parar
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]
    def clip(self,  clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect
    def update(self, direction):
        if direction == True:
            self.clip(self.movement)
        self.image = self.sheet.subsurface(self.sheet.get_clip())

class Heart(pygame.sprite.Sprite):
    def __init__(self, position, player_life):
        super().__init__()
        self.sheet = pygame.image.load("Life_Design/Life.png")
        self.sheet.set_clip(pygame.Rect(0, 0, 90, 30))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.life = player_life
        self.movement = { 0: (0, 0, 90, 30), 1: (30, 0, 90, 30), 2: (60, 0, 90, 30) }
    def get_frame(self, frame_set): #Este metodo es el encargado de vaciar/llenar los corazones de Jerry
        if self.frame == 0 and self.life == 200:
            self.frame = 1
        if self.frame == 1 and self.life == 300:
            self.frame = 0
        if self.frame == 1 and self.life == 100:
            self.frame = 2
        if self.frame == 2 and self.life == 200:
            self.frame = 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]
    def clip(self,  clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect
    def update(self, direction):
        if direction == True:
            if self.life <= 300:
                self.clip(self.movement)
        self.image = self.sheet.subsurface(self.sheet.get_clip())

