import cProfile
import pstats
import io
import time
import matplotlib.pyplot as plt
import numpy as np

# CODIGO ORIGINAL
def original_primos(limite):
    primos = []
    for num in range(1, limite + 1):
        if num < 2:
            continue
        es_primo = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(num)
    return primos

# CODIGO OPTIMIZADO
def optimizado_primos(limite):
    if limite < 2:
        return []
    es_primo = np.ones(limite + 1, dtype=bool)
    es_primo[0:2] = False
    for i in range(2, int(np.sqrt(limite)) + 1):
        if es_primo[i]:
            es_primo[i*i:limite+1:i] = False
    return np.where(es_primo)[0].tolist()

# MEDICION DE LOS TIEMPOS
limite = 100000

# Medir codigo original
inicio = time.time()
primos_original = original_primos(limite)
tiempo_original = time.time() - inicio

# Medir codigo optimizado
inicio = time.time()
primos_optimizado = optimizado_primos(limite)
tiempo_optimizado = time.time() - inicio

print(f"Tiempo original: {tiempo_original:.4f} segundos")
print(f"Tiempo optimizado: {tiempo_optimizado:.4f} segundos")
print(f"Mejora: {tiempo_original/tiempo_optimizado:.1f}x mas rapido")

# cPROFILE
print("\nFUNCIONES CRÍTICAS (Original)")
profiler = cProfile.Profile()
profiler.enable()
original_primos(limite)
profiler.disable()

stream = io.StringIO()
stats = pstats.Stats(profiler, stream=stream)
stats.sort_stats('cumulative')
stats.print_stats(5)
print(stream.getvalue())

# Guardar profiling en archivo
with open('profiling_optimizado.txt', 'w') as f:
    f.write(stream.getvalue())

# GRAFICOS
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Grafico 1: Comparativa de tiempos
versiones = ['Original', 'Optimizado']
tiempos = [tiempo_original, tiempo_optimizado]
colores = ['#FF6B6B', '#4ECDC4']

barras = ax1.bar(versiones, tiempos, color=colores, edgecolor='black', linewidth=1.5)
ax1.set_ylabel('Tiempo (segundos)')
ax1.set_title('Comparativa de Tiempos de Ejecución')
ax1.grid(axis='y', alpha=0.3)

# Añadir valores en las barras
for barra, tiempo in zip(barras, tiempos):
    ax1.text(barra.get_x() + barra.get_width()/2, barra.get_height() + 0.02,
             f'{tiempo:.3f}s', ha='center', va='bottom', fontweight='bold')

# Grafico 2: Distribucion de tiempos
tiempos_original_dist = []
tiempos_optimizado_dist = []

for _ in range(30):  # 30 repeticiones
    inicio = time.time()
    original_primos(10000)  # Limite mas pequeño para que sea rapido
    tiempos_original_dist.append(time.time() - inicio)
    
    inicio = time.time()
    optimizado_primos(10000)
    tiempos_optimizado_dist.append(time.time() - inicio)

ax2.hist(tiempos_original_dist, bins=10, alpha=0.5, label='Original', color='#FF6B6B')
ax2.hist(tiempos_optimizado_dist, bins=10, alpha=0.5, label='Optimizado', color='#4ECDC4')
ax2.set_xlabel('Tiempo (segundos)')
ax2.set_ylabel('Frecuencia')
ax2.set_title('Distribución de Tiempos de Ejecución')
ax2.legend()
ax2.grid(alpha=0.3)

plt.tight_layout()
plt.savefig('comparativa_rendimiento.png', dpi=300)
plt.show()

print("\nGrafico guardado como 'comparativa_rendimiento.png'")
print("Profiling guardado como 'profiling_optimizado.txt'")