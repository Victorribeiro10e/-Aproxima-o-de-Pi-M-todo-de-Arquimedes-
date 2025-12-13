import math

def arquimedes_pi(iteracoes=10):
    """Calcula Pi usando o método poligonal de Arquimedes"""
    # Começa com hexágono (6 lados)
    lados = 6
    lado = 1.0  # Lado do polígono inscrito
    for i in range(iteracoes):
        # Calcula perímetro do polígono inscrito
        perimetro_inscrito = lados * lado
        pi_aproximado = perimetro_inscrito / 2
        
        print(f"Iteração {i+1}: {lados} lados, π ≈ {pi_aproximado:.10f}")
        
        # Prepara próxima iteração (dobra número de lados)
        lado = math.sqrt(2 - math.sqrt(4 - lado**2))
        lados *= 2
    
    return pi_aproximado

# Teste
pi_arquimedes = arquimedes_pi(iteracoes=5)
print(f"\nPi real: {math.pi:.10f}")