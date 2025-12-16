import math
import math

def arquimedes_pi(iteracoes=10):
    """Calcula Pi usando o método poligonal de Arquimedes"""
    # Começa com hexágono inscrito (6 lados)
    lados = 6
    # Para hexágono inscrito em círculo unitário, lado = 1
    lado_inscrito = 1.0
    # Para hexágono circunscrito em círculo unitário
    lado_circunscrito = 2 * math.sqrt(3) / 3
    
    for i in range(iteracoes):
        # Perímetros
        perimetro_inscrito = lados * lado_inscrito
        perimetro_circunscrito = lados * lado_circunscrito
        
        # Aproximações de π (diâmetro = 2 para círculo unitário)
        pi_aproximado_inscrito = perimetro_inscrito / 2
        pi_aproximado_circunscrito = perimetro_circunscrito / 2
        pi_medio = (pi_aproximado_inscrito + pi_aproximado_circunscrito) / 2
        
        print(f"Iteração {i+1}: {lados} lados")
        print(f"  Inscrito:  π ≈ {pi_aproximado_inscrito:.10f}")
        print(f"  Circunscrito: π ≈ {pi_aproximado_circunscrito:.10f}")
        print(f"  Médio:     π ≈ {pi_medio:.10f}")
        print(f"  Erro: ±{(pi_aproximado_circunscrito - pi_aproximado_inscrito)/2:.10f}")
        
        # Prepara próxima iteração (dobra número de lados)
        # Fórmulas corretas para atualizar os lados
        novo_lado_inscrito = math.sqrt(2 - math.sqrt(4 - lado_inscrito**2))
        lado_circunscrito = (2 * lado_inscrito * lado_circunscrito) / (lado_inscrito + lado_circunscrito)
        lado_inscrito = novo_lado_inscrito
        lados *= 2
    
    return pi_medio

# Teste
print("Método de Arquimedes para calcular π")
print("=" * 50)
pi_arquimedes = arquimedes_pi(iteracoes=5)
print(f"\nPi real:       {math.pi:.10f}")
print(f"Diferença:     {abs(pi_arquimedes - math.pi):.10f}")
