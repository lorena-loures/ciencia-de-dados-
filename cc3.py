import matplotlib.pyplot as plt
import numpy as np 

pontuacoes = np.random.randint(0,10,30)

plt.boxplot (pontuacoes,vert=False, patch_artist=True,
notch=True, boxprops=dict(facecolor='pink'))


plt.title('Ditribuição das pontuações dos Jogadores')
plt.xlabel('pontuacao')
plt.show()
