import turtle

# Crie uma tartaruga
t = turtle.Turtle()

# Defina a cor de preenchimento
t.fillcolor("gray")

# Defina a velocidade da tartaruga
t.speed(1)

# Desenhe um círculo maior
t.begin_fill()
t.circle(100, 180)  # Desenha meio círculo
t.end_fill()

# Movimente a tartaruga para a posição do círculo menor
t.penup()
t.goto(-50, 0)
t.pendown()

# Defina a cor de preenchimento para o círculo menor
t.fillcolor("white")

# Desenhe um círculo menor
t.begin_fill()
t.circle(50, 180)  # Desenha meio círculo
t.end_fill()

# Mantenha a janela aberta até clique
turtle.done()

