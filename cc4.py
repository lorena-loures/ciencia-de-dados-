import matplotlib.pyplot as plt

meses = ['Janeiro','fevereiro', 'março', 'abril', 'maio', 'junho',]
vendas = [15250.80, 30862.65, 35520.60, 17526.98, 25264.87, 45235.63]

plt.plot(meses,vendas)
plt.title('vendas no primeiro semestre')
plt.xlabel('meses')
plt.ylabel('vendas')
plt.show()

