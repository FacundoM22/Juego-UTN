import pygame
from auxiliar import *
from settings import *
from bullet import Bullet


class BulletManager():
    def __init__(self,cantidad_balas_player,cantidad_balas_enemigo):
        self.balas_player = [Bullet() for _ in range(cantidad_balas_player)]
        self.balas_enemy =  [Bullet() for _ in range(cantidad_balas_enemigo)]
        self.balas_disparadas = []
        self.cantidad_balas = cantidad_balas_player

        

    def create_bullet(self,cantidad):
           return [Bullet() for _ in range(cantidad)] 

    def shoot(self,x_player, y_player,direction,controllable):
        if controllable == False:
            bala_actual_enemigo = self.balas_enemy.pop(0)
            bala_actual_enemigo.bullet_rect.x = x_player
            bala_actual_enemigo.bullet_rect.y = y_player
            bala_actual_enemigo.shoot_direction = direction
            bala_actual_enemigo.is_shooting = True
            self.balas_disparadas.append(bala_actual_enemigo)
        else:
            if self.balas_player: 
             bala_actual = self.balas_player.pop(0)
             bala_actual.player_bullet = True
             bala_actual.bullet_rect.x = x_player
             bala_actual.bullet_rect.y = y_player
             bala_actual.shoot_direction = direction
             bala_actual.is_shooting = True
             bala_actual.player_bullet = True
             self.balas_disparadas.append(bala_actual)
           
        
    def reload(self):
             self.balas_player.clear()
             self.balas_player = self.create_bullet(self.cantidad_balas) 
             


