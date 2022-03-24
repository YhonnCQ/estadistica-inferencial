from scipy.stats import norm


def main():
    n = int(input("Ingrese tamaño de la poblacion (N): "))
    z = int(input("Ingrese nivel de confianza (Z): "))
    z = z * (1 / 100)
    p = int(input("Ingrese prevalencia del evento (p): "))
    p = p * (1 / 100)
    q = 1 - p
    e = int(input("Ingrese presicion (E): "))
    e = e * (1 / 100)
    z = round(norm.ppf(z + ((1 - z) / 2)), 3)
    r = (n * pow(z, 2) * p * q) / (pow(e, 2) * (n - 1) + pow(z, 2) * p * q)
    print(f'Respuesta {r}')


if __name__ == '__main__':
    main()
