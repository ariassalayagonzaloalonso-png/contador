# contador.py

def contar_hasta(n):
    for i in range(1, n + 1):
        print(i)

if __name__ == "__main__":
    print("=== Contador CLI ===")
    numero = int(input("Ingresa un número: "))
    contar_hasta(numero)
