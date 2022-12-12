import pygame

ANCHO_VENTANA = 1600
ALTO_VENTANA = 900
FPS = 60

DIRECTION_L = 0
DIRECTION_R = 1

pausa = False

DEBUG = False

RUNNING = True

USERNAME = ""

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

GROUND_RECT_H = 7
GROUND_LEVEL = 600

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))

class Auxiliar:
    @staticmethod
    def getSurfaceFromSpriteSheet(path,columnas,filas,flip=False, step = 1):
        lista = []
        surface_imagen = pygame.image.load(path)
        fotograma_ancho = int(surface_imagen.get_width()/columnas)
        fotograma_alto = int(surface_imagen.get_height()/filas)
        x = 0
        
        for fila in range(filas):
            for columna in range(0,columnas,step):
                x = columna * fotograma_ancho
                y = fila * fotograma_alto
                surface_fotograma = surface_imagen.subsurface(x,y,fotograma_ancho,fotograma_alto)
                if(flip):
                    surface_fotograma = pygame.transform.flip(surface_fotograma,True,False)
                lista.append(surface_fotograma)
        return lista