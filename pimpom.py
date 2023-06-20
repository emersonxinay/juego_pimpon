import turtle

# Configuración de la ventana
window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Raqueta izquierda
raqueta_izquierda = turtle.Turtle()
raqueta_izquierda.speed(0)
raqueta_izquierda.shape("square")
raqueta_izquierda.color("white")
raqueta_izquierda.shapesize(stretch_wid=6, stretch_len=1)
raqueta_izquierda.penup()
raqueta_izquierda.goto(-350, 0)

# Raqueta derecha
raqueta_derecha = turtle.Turtle()
raqueta_derecha.speed(0)
raqueta_derecha.shape("square")
raqueta_derecha.color("white")
raqueta_derecha.shapesize(stretch_wid=6, stretch_len=1)
raqueta_derecha.penup()
raqueta_derecha.goto(350, 0)

# Pelota
pelota = turtle.Turtle()
pelota.speed(40)
pelota.shape("square")
pelota.color("white")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 2
pelota.dy = -2

# Funciones de movimiento de las raquetas
def mover_raqueta_izquierda_up():
    y = raqueta_izquierda.ycor()
    if y < 250:
        y += 20
    raqueta_izquierda.sety(y)

def mover_raqueta_izquierda_down():
    y = raqueta_izquierda.ycor()
    if y > -240:
        y -= 20
    raqueta_izquierda.sety(y)

def mover_raqueta_derecha_up():
    y = raqueta_derecha.ycor()
    if y < 250:
        y += 20
    raqueta_derecha.sety(y)

def mover_raqueta_derecha_down():
    y = raqueta_derecha.ycor()
    if y > -240:
        y -= 20
    raqueta_derecha.sety(y)

# Asociar teclas a funciones de movimiento
window.listen()
window.onkeypress(mover_raqueta_izquierda_up, "w")
window.onkeypress(mover_raqueta_izquierda_down, "s")
window.onkeypress(mover_raqueta_derecha_up, "Up")
window.onkeypress(mover_raqueta_derecha_down, "Down")

# Bucle principal del juego
while True:
    window.update()

    # Mover la pelota
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    # Rebotar en los bordes superiores e inferiores
    if pelota.ycor() > 290 or pelota.ycor() < -290:
        pelota.dy *= -1

    # Rebotar en las raquetas
    if (pelota.dx > 0) and (340 < pelota.xcor() < 350) and (raqueta_derecha.ycor() + 50 > pelota.ycor() > raqueta_derecha.ycor() - 50):
        pelota.color("green")
        pelota.dx *= -1
    elif (pelota.dx < 0) and (-340 > pelota.xcor() > -350) and (raqueta_izquierda.ycor() + 50 > pelota.ycor() > raqueta_izquierda.ycor() - 50):
        pelota.color("green")
        pelota.dx *= -1
    else:
        pelota.color("white")

    # Reiniciar la pelota si sale de los límites laterales
    if pelota.xcor() > 390:
        pelota.goto(0, 0)
        pelota.dx *= -1
    elif pelota.xcor() < -390:
        pelota.goto(0, 0)
        pelota.dx *= -1
