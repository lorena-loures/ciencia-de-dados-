import matplotlib.pyplot as plt
import numpy as np 

idades = np.random.randint(18, 40, 5)

plt.hist(idades, bins=5, color='blue', alpha=0.5)
plt.title('Distribuição de Idades dos Jogadores de Futebol')
plt.xlabel('Idades')
plt.ylabel('Números de jogadores')
plt.grid(True)
plt.show()

