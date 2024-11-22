import time

s = 2

def impulso(v_i, v_f, delta_t, m):
    # Esta es la fórmula de impulso
    # F = m(vf-vi)/t

    fuerza = (m*v_f - m*v_i)
    fuerza = fuerza/delta_t
    print("Ha mandado la pelota con una fuerza de:", fuerza, "N")
    time.sleep(1)

def momentum(v_f, peso_vaso, m):
    # Aqui se usa la formula de momentums que es
    # m1u1 + m2u2 = m1v + m2v    (Como la pelota y el vaso van juntos, la v es la misma)
    # Despejando la ecuacion queda    (m1 * u1) / (m1 + m2)

    v_impacto = (m * v_f)
    v_impacto = v_impacto/(m + peso_vaso)
    print("El vaso le ha caído a la persona de atras a una velocidad de", v_impacto, "m/s")

print("Eres un jugador de baseball!")
time.sleep(s)
print("Viene una pelota hacia ti a 50m/s!")
time.sleep(s)
print("Tienes 10 milisegundos para pegarle a la pelota!")
time.sleep(s)

v_i = -50        # Velocidad Inicial
delta_t = 0.01   # Diferencia del tiempo
m = 0.14         # Peso en KG

v_f = int(input("Con que a que velocidad quiere regresar la pelota?\n"))
impulso(v_i, v_f, delta_t, m)

print("\nOH NO! Le has pegado a un vaso!")
time.sleep(s)
print(" *pero este vaso es muy resistente y no se rompe* ")
time.sleep(s)
print("Los vasos se van unidos y le pegan a alguien atras! \n")
time.sleep(s)

peso_vaso = 5 # Peso en KG

momentum(v_f, peso_vaso, m)