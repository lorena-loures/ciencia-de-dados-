import matplotlib.pyplot as plt
import numpy as np 

alturas = np.random.randint(150,200,30)
pesos= np.random.randint(50,100,30)

plt.scatter(alturas,pesos, color='green')
plt.title('Relação entre Altura e Peso dos Jogadores de Futebol')
plt.xlabel('Altura (cm)')
plt.ylabel('peso (kg)')
plt.grid(True)
plt.show()
