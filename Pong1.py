#Pong simple en Python 3
# by SerSalas

import turtle

ventana = turtle.Screen()

ventana.title("Pong by @SerSalas")
ventana.bgcolor("black")
ventana.setup(width=800, height=600)
ventana.tracer(0)

#Paleta A
paleta_a = turtle.Turtle()
paleta_a.speed(0)
paleta_a.shape("square")
paleta_a.color("white")
paleta_a.penup()
paleta_a.goto(-350, 0)

#Paleta B

#Pelota

#Bucle principal del juego
while True:
    ventana.update()

