# Definir los puntos de datos (xi, yi)
xi = [1, 2, 9]
yi = [7, 8, 5]

# Definir la función para calcular el polinomio de Lagrange
def polinomio_lagrange(xi, yi):
    n = len(xi)
    def polinomio(x):
        resultado = 0
        for i in range(n):
            termino = yi[i]
            for j in range(n):
                if j != i:
                    termino *= (x - xi[j]) / (xi[i] - xi[j])
            resultado += termino
        return resultado
    return polinomio

# Calcular el polinomio de Lagrange para los puntos dados
p = polinomio_lagrange(xi, yi)

# Imprimir el resultado para algunos valores de x
print("x=2.7, y=", p(2.7))
print("x=5, y=", p(5))
