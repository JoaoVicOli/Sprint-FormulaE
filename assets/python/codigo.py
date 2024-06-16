#Conceitos de entrada e saída
#Uso de fstrings
#Armazenar dados em variáveis e listas
#Usar estrutura condicional e de repetição
#Uso de funções

import random
import matplotlib.pyplot as plt

# Função para gerar dados aleatórios
def gerar_dados():
    dados = []
    for _ in range(10):  # Gerar 10 pontos de dados
        piloto = random.choice(['Piloto A', 'Piloto B', 'Piloto C'])
        tempo_volta = round(random.uniform(55, 65), 2)  # Tempo de volta aleatório entre 55 e 65 segundos
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
    print("Dados gerados:")
    for piloto, tempo in dados:
        print(f"Piloto: {piloto}, Tempo de Volta: {tempo} s")
    
    # Plotar gráfico de barras
    plotar_grafico(dados)

if __name__ == "__main__":
    main()