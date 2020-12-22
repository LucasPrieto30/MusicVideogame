#! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *
from configuracion import *
from extras import *

from funcionesVACIAS import *


#Funcion principal
def main():

        
        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        #pygame.mixer.init()

        

        #Preparar la ventana
        pygame.display.set_caption("Cancionero")
        icon = pygame.image.load("icono.jpg")
        pygame.display.set_icon(icon)
        screen = pygame.display.set_mode((ANCHO, ALTO))
        #definimos funciones

        play_reloj=False

        #tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial
        artistaYcancion=[]
        puntos = 0
        palabraUsuario = ""
        letra=[]
        correctas=0
        elegidos= []
        masDeUnaVuelta = False


        #elige una cancion de todas las disponibles
        azar=random.randrange(1,N+1)
        elegidos.append(azar) #la agrega a la lista de los ya elegidos
        archivo= open(".\\letras\\"+str(azar)+".txt","r", encoding='utf-8') # abre el archivo elegido con unicode.


        #lectura del archivo y filtrado de caracteres especiales, la primer linea es el artista y cancion
        lectura(archivo, letra, artistaYcancion)

        #elige una linea al azar y su siguiente
        lista=seleccion(letra)

##        print(lista)

        ayuda = "Cancionero"
        dibujar(screen, palabraUsuario, lista, puntos, segundos, ayuda)

        while segundos > fps/1000:
        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()

            if True:
            	fps = 30

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letraApretada = dameLetraApretada(e.key)
                    palabraUsuario += letraApretada
                    if e.key == K_BACKSPACE:
                        palabraUsuario = palabraUsuario[0:len(palabraUsuario)-1]
                    if e.key == K_RETURN:
                        #chequea si es correcta y suma o resta puntos
                        sumar=esCorrecta(palabraUsuario, artistaYcancion, correctas)
                        puntos+=sumar

                        if sumar>0:
                            sonido_correcto=pygame.mixer.Sound("correcto.wav") #sonido para cuando acierta el jugador
                            sonido_correcto.play()
                            correctas=correctas+1
                        else:
                            sonido_error=pygame.mixer.Sound("chicharra-error-incorrecto-.mp3") #sonido de error para cuando no acierta
                            sonido_error.play() #reproduce el sunido guardado en esa variable
                            correctas=0
                        if len(elegidos)==N:
                                elegidos=[]
                                masDeUnaVuelta = True

                        azar=random.randrange(1,N+1)
                        while(azar in elegidos):
                            azar=random.randrange(1,N+1)

                        elegidos.append(azar)


                        if masDeUnaVuelta == True:
                            ayuda = "La anterior era "+artistaYcancion[0]

                        archivo= open(".\\letras\\"+str(azar)+".txt","r", encoding='utf-8')
                        palabraUsuario = ""
                        #lectura del archivo y filtrado de caracteres especiales
                        artistaYcancion=[]
                        letra = []
                        lectura(archivo, letra, artistaYcancion)



                        #elige una linea al azar y su siguiente
                        lista=seleccion(letra)


            segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000
            
            #reproduce sonido de reloj cuando restan 15 seg de juego
            if segundos<15 and play_reloj==False:
                sonido_reloj=pygame.mixer.Sound("clock.mp3")
                sonido_reloj.play()
                play_reloj=True

            #Limpiar pantalla anterior
            screen.fill(COLOR_FONDO)

            #Dibujar de nuevo todo
            dibujar(screen, palabraUsuario, lista, puntos, segundos, ayuda)
            pygame.display.flip()


        #MUESTRA GAME OVER Y LOS PUNTOS CUANDO SE TERMINA EL JUEGO
        def gameOver():
            pygame.init()
            sonido_reloj=pygame.mixer.Sound("gameover.mp3")
            sonido_reloj.play()
            screen = pygame.display.set_mode((ANCHO, ALTO))
            pygame.display.set_caption("Cancionero")
            icon = pygame.image.load("icono.jpg")
            pygame.display.set_icon(icon)
            texto = "GAME OVER"
            defaultFontGameOver= pygame.font.Font("Montserrat-ExtraBoldItalic.ttf",130)
            defaultFontGameOverPuntos = pygame.font.Font("Montserrat-ExtraBoldItalic.ttf",30)
            mensaje = defaultFontGameOver.render(texto, 1, (255,0,0))
            dibujar(screen, palabraUsuario, lista, puntos, segundos, ayuda)
            screen.blit(mensaje, (100, 200))
            screen.blit(defaultFontGameOverPuntos.render("Puntos Totales: " + str(puntos), 1, (255,0,0)), (340, 400))
            pygame.display.flip()
        gameOver()

        while 1:
            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return


        archivo.close()

#Programa Principal ejecuta Main
if __name__ == "__main__":
    main()
