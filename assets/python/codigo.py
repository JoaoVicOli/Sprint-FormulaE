#Conceitos de entrada e saída
#Uso de fstrings
#Armazenar dados em variáveis e listas
#Usar estrutura condicional e de repetição
#Uso de funções

import random
import matplotlib.pyplot as plt

# Função para gerar dados aleatórios com 3 pilotos
def gerar_dados():
    pilotos = ['Piloto A', 'Piloto B', 'Piloto C']  
    
    dados = []
    for piloto in pilotos:
        # Tempo de volta aleatório entre 55 e 65 segundos
        tempo_volta = round(random.uniform(55, 65), 2)  
        dados.append((piloto, tempo_volta))
    return dados

# Função para criar gráfico de barras
def plotar_grafico(dados):
    pilotos = [item[0] for item in dados]
    tempos = [item[1] for item in dados]
    
    plt.figure(figsize=(10, 6))
    plt.bar(pilotos, tempos, color=['blue', 'green', 'red'])
    plt.xlabel('Pilotos')
    plt.ylabel('Tempo de Volta (s)')
    plt.title('Tempo de Volta dos Pilotos')
    plt.show()

# Função principal
def main():
    dados = gerar_dados()
    
    # Mostrar os dados gerados
    for piloto, tempo in dados:
        print(f"{piloto} - Tempo de Volta: {tempo}s")
    
    # Plotar gráfico de barras
    plotar_grafico(dados)

if __name__ == "__main__":
    main()