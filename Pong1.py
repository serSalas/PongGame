#Pong simple en Python 3
# by SerSalas

import turtle

ventana = turtle.Screen()

ventana.title("Pong by @SerSalas")
ventana.bgcolor("black")
ventana.setup(width=800, height=600)
ventana.tracer(0)


#Bucle principal del juego
while True:
    ventana.update()