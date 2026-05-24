import time

# Mide el tiempo de ejecucion
inicio = time.time()

# Busca los numeros del 1 al 100,000
limite = 100000
primos = []

for num in range(1, limite + 1):
    # Determina si num es primo
    if num < 2:
        continue 
    
    es_primo = True
    # Verifica los divisores desde dos hasta raiz cuadrada
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            es_primo = False
            break
    
    if es_primo:
        primos.append(num)

fin = time.time()
tiempo_ejecucion = fin - inicio

# Muestra los resultados
print(f"Busqueda de numeros primos del 1 al {limite:,}")
print(f"Cantidad de primos encontrados: {len(primos)}")
print(f"Tiempo de ejecucion: {tiempo_ejecucion:.4f} segundos")
print(f"\nPrimeros 10 primos: {primos[:10]}")
print(f"Ultimos 10 primos: {primos[-10:]}")
