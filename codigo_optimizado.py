# CODIGO OPTIMIZADO
import time
import numpy as np

def encontrar_primos_numpy(limite):
    # Encuentra numeros primos usando NumPy para la optimizacion
    if limite < 2:
        return np.array([])
    
    # Inicializa un array de booleanos 
    es_primo = np.ones(limite + 1, dtype=bool)
    es_primo[0:2] = False  # 0 y 1 no son primos
    
    for i in range(2, int(np.sqrt(limite)) + 1):
        if es_primo[i]:
            # Marcar multiples como no primos usando slicing
            es_primo[i*i:limite+1:i] = False
    
    # Extraer números primos
    primos = np.where(es_primo)[0].tolist()
    
    return primos

def encontrar_primos_optimizado(limite):
    if limite < 2:
        return []
    
    primos = [2] if limite >= 2 else []
    
    # Solo se prueba los numeros impares
    for num in range(3, limite + 1, 2):
        es_primo = True
        # Solo verifica hasta la raíz cuadrada
        raiz = int(num ** 0.5)
        # Verifica solo divisores primos conocidos
        for divisor in primos:
            if divisor > raiz:
                break
            if num % divisor == 0:
                es_primo = False
                break
        
        if es_primo:
            primos.append(num)
    
    return primos

def main():
    limite = 100000
    
    # Prueba de version optimizada 
    print("VERSIÓN NUMPY")
    inicio = time.time()
    primos_numpy = encontrar_primos_numpy(limite)
    tiempo_numpy = time.time() - inicio
    print(f"Cantidad de primos encontrados: {len(primos_numpy)}")
    print(f"Tiempo de ejecucion: {tiempo_numpy:.4f} segundos")
    print(f"Primeros 10 primos: {primos_numpy[:10]}")
    print(f"Ultimos 10 primos: {primos_numpy[-10:]}")
    
    print(f"\n{'='*50}\n")
    
    # Prueba de version optimizada
    print("VERSIÓN OPTIMIZADA (Sin NumPy)")
    inicio = time.time()
    primos_opt = encontrar_primos_optimizado(limite)
    tiempo_opt = time.time() - inicio
    print(f"Cantidad de primos encontrados: {len(primos_opt)}")
    print(f"Tiempo de ejecución: {tiempo_opt:.4f} segundos")
    print(f"Primeros 10 primos: {primos_opt[:10]}")
    print(f"Últimos 10 primos: {primos_opt[-10:]}")
    
    # Comparacion de rendimiento
    print(f"\n{'='*50}")
    print("\nCOMPARACION DE RENDIMIENTO:")
    print(f"Original: ~2.5 segundos")
    print(f"Optimizado (NumPy): {tiempo_numpy:.4f} segundos")
    print(f"Optimizado (Algoritmo): {tiempo_opt:.4f} segundos")
    print(f"Mejora NumPy: {(2.5/tiempo_numpy - 1)*100:.1f}% mas rapido")
    print(f"Mejora Algoritmo: {(2.5/tiempo_opt - 1)*100:.1f}% mas rapido")

if __name__ == "__main__":
    main()
