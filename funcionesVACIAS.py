from configuracion import *
import random
import math
import unicodedata

def normalizar(cadena): # Reeemplaza los caracteres extraños de una cadena por caracteres normales
	nueva=""
	for i in cadena:
		if i=="á":
			nueva+="a"
		elif i=="é":
			nueva+="e"
		elif i=="í":
			nueva+="i"
		elif i=="ó":
			nueva+="o"
		elif i=="ú":
			nueva+="u"
		elif i=="ñ":
			nueva+="ni"
		elif i=="ü":
			nueva+="u"
		elif i=="\n":
			nueva+=""
		else:
			nueva+=i
	return nueva

#se queda solo con los oraciones de cierta longitud y filtra tildes por ej
def lectura(archivo, letra, artistaYcancion): 
	nombres_artista=archivo.readline() #GUARDA EN LA VARIABLE LA PRIMERA LINEA DEL TXT
	nombres_artista=normalizar(nombres_artista) #FILTRA CARACTERES ESPECIALES(LOS REEMPLAZA POR COMUNES)
	nombre="" # SE VA GUARDANDO CADA NOMBRE CON EL QUE SE CONOCE A LA BANDA Y LA CANCION
	for i in range(len(nombres_artista)):		
		if nombres_artista[i] ==";":
			artistaYcancion.append(nombre)
			nombre=""
		elif i==len(nombres_artista)-1:
			nombre+=nombres_artista[i]
			artistaYcancion.append(nombre)
		else:
			nombre+=nombres_artista[i]
	for linea in archivo:
		if 1<len(linea)<=45: #SI ENCUENTRA UNA LINEA QUE NO ENTRE COMPLETA EN LA PANTALLA (DE MAS DE 45 CARACTERES) NO LA INCLUYE EN LA LISTA
			linea=normalizar(linea)
			letra.append(linea)

def seleccion(letra):#elige uno al azar, devuelve ese y el siguiente
    seleccionadas = []
    posicionAleatoria = random.randrange(len(letra)-1) 
    linea1 = letra[posicionAleatoria]
    linea2 = letra[posicionAleatoria + 1]
    seleccionadas.append(linea1)
    seleccionadas.append(linea2)
    return seleccionadas 

#devuelve el puntaje, segun seguidilla
def puntos(n):
	puntaje=0
	if n>1:
		puntaje = 2**n #SI HAY UNA SEGUIDILLA DE RESPUESTAS CORRECTAS EL PUNTAJE SE CALCULA DE MANERA EXPONENCIAL 
	elif n==1:
		puntaje=1
	else:
		puntaje=-5
	return puntaje


def esCorrecta(palabraUsuario, artistaYCancion, correctas):
	cantidad_seguidas=correctas
	if palabraUsuario in artistaYCancion:
		if cantidad_seguidas<1:
			cantidad_seguidas+=1
			return puntos(cantidad_seguidas)
		else:
			return puntos(cantidad_seguidas)
	else:
		cantidad_seguidas=0
		return puntos(cantidad_seguidas)
		