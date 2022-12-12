import pygame
from settings import *
from auxiliar import Auxiliar


class Bullet():
    def __init__(self,x=0,y=0):
        self.bullet =   Auxiliar.getSurfaceFromSpriteSheet("images/assets/onion/onion__x1_iconic_png_1354829938.png",1,1,True)
        self.frame = 0
        self.player_bullet = 0
        self.speed_bullet = 20
        self.move_x = 0
        self.is_shooting = False
        self.visible = False
        self.image_bullet = self.bullet[self.frame]
        self.bullet_rect = self.image_bullet.get_rect()
        self.bullet_rect.x = x
        self.bullet_rect.y = y
        self.shoot_direction = 0
        self.tiempo_transcurrido_bala = 0
        self.rect_bullet_collition = pygame.Rect(self.bullet_rect.left,self.bullet_rect.top,self.bullet_rect.right,self.bullet_rect.bottom)
        self.rect_bullet_collition = self.bullet_rect
       



    def draw(self,screen):
        if (DEBUG):
               # pygame.draw.rect(screen,GREEN,self.bullet_rect)
                pygame.draw.rect(screen,RED,self.rect_bullet_collition)
        screen.blit(self.image_bullet,self.bullet_rect)
        



    def update_bullet(self,delta_ms,lista_characters,lista_balas):
           
            self.tiempo_transcurrido_bala += delta_ms
            for bala in lista_balas:
                if  bala.bullet_rect.x < -50 or bala.bullet_rect.x > 1550:
                    bala.visible = False    
                    bala.is_shooting = False
                    lista_balas.pop(lista_balas.index(bala)) 
          
          
            if self.tiempo_transcurrido_bala > 20: 
                self.tiempo_transcurrido_bala = 0
                if self.is_shooting == True:
                     if   self.shoot_direction == DIRECTION_L:
                            self.bullet_rect.x  -=  self.speed_bullet
                     elif self.shoot_direction == DIRECTION_R: 
                            self.bullet_rect.x += self.speed_bullet
           
        
            
