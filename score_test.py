#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
	Función que incrementa el score de un set en una partida de tenis

>>> get_score()
'El resultado es 0 - 0'

>>> anotacion(1)
'El jugador 1 anotó'

>>> get_score()
'El resultado es 15 - 0'

>>> anotacion(1)
'El jugador 1 anotó'

>>> get_score()
'El resultado es 30 - 0'

>>> anotacion(1)
'El jugador 1 anotó'

>>> get_score()
'El resultado es 40 - 0'

>>> anotacion(2)
'El jugador 2 anotó'

>>> anotacion(2)
'El jugador 2 anotó'

>>> anotacion(2)
'El jugador 2 anotó'

>>> get_score()
'El resultado es deuce'

>>> anotacion(1)
'El jugador 1 anotó'

>>> get_score()
'El resultado es advantage, ____'

>>> anotacion(2)
'El jugador 2 anotó'

>>> get_score()
'El resultado es deuce'

>>> anotacion(2)
'El jugador 2 anotó'

>>> get_score()
'El resultado es ____ , advantage'

>>> anotacion(1)
'El jugador 1 anotó'

>>> get_score()
'El resultado es deuce'


>>> anotacion(1)
'El jugador 1 anotó'

>>> anotacion(1)
'El jugador 1 anotó'

>>> get_score()
'Set para el jugador 1'

# prueba con anotaciones intercaladas ---------------------------------------
>>> clear_score()
'/////////////////////////////////////////////////////////////////////////////////////////////////'



"""
player_1,player_2=0,0
incremento_1,incremento_2=15,15

def anotacion(jugador):
	""" 	Función que realiza una anotación al jugador indicado """
	global player_1, player_2,incremento_1,incremento_2
	
	if player_1>=30:
		incremento_1=10
	if player_2>=30:
		incremento_2=10
	
	if jugador==1:
		player_1+=incremento_1

	else:
		player_2+=incremento_2

	print "'El jugador {0} anotó'".format(jugador)


def get_score():
	global player_1, player_2,incremento_1,incremento_2
	""" 	Función que devuelve el marcador en determinado momento """
	

	if player_1 >= 40 and player_2 >= 40 and player_1 == player_2:
		return "El resultado es deuce"
	elif player_1 > 40 and player_1 - player_2 == 10:
		return "El resultado es advantage, ____"
	elif player_2 > 40 and player_2 - player_1 == 10:
		return "El resultado es ____ , advantage"
	elif player_1 > 40 and player_1 - player_2 > 10:
		return "Set para el jugador 1"
	elif player_2 > 40 and player_2 - player_1 > 10:
		return "Set para el jugador 2"
	else:
		return "El resultado es {0} - {1}".format(player_1,player_2)

def clear_score():
	global player_1, player_2,incremento_1,incremento_2
	player_1,player_2=0,0
	incremento_1,incremento_2=15,15
	return '/////////////////////////////////////////////////////////////////////////////////////////////////'

if __name__=="__main__":
	import doctest
	doctest.testmod()
