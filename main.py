import numpy as np
from numpy import random
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

amostra = 20

hoje = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
periodo = pd.date_range(start=hoje, periods=amostra, freq='min')

#np.random.normal
temperatura = np.random.normal(loc=15, scale=10, size=amostra).round(2)
#np.random.uniform
luminosidade = np.random.uniform(low=0, high=1000, size=amostra).round(2)
#0 = sem movimento, 1 = movimento detectado. p=[0.8, 0.2] => 80% das vezes sem movimento, 20% com movimento
movimento = np.random.choice([0, 1], size=amostra, p=[0.8, 0.2])
dt = {
    "registro": periodo,
    "temperatura": temperatura,
    "luminosidade": luminosidade,
    "movimento": movimento
}

data_frame = pd.DataFrame(dt)
#print(data_frame)
#pd.DataFrame(data_frame).to_csv(f'registro_{datetime.now().strftime("%d_%m_%y")}', index=False)

titulo = {'family': 'serif', 'size': '13', 'color': 'black'}
label = {'family': 'serif', 'size': '11', 'color': 'gray'}
x = dt["registro"]
t = dt["temperatura"]
l = dt["luminosidade"]
m = dt["movimento"]
'''
#Temperatura
plt.figure(figsize=(13, 8))
plt.title("Variação de Temperatura", fontdict = titulo, loc='left')

plt.plot(x, t, label='temperatura', color='green')
plt.xlabel('registros', fontdict=label)
plt.ylabel('temperatura(°C)', fontdict=label)

plt.grid(axis = 'y', color = 'gray', linestyle = '--', linewidth = 0.7)
plt.legend()
plt.show()


#Luminosidade
plt.figure(figsize=(13, 8))
plt.title("Luminosidade", fontdict = titulo, loc='left')

plt.plot(x, l, label='luminosidade', color='orange')
plt.xlabel('registros', fontdict=label)
plt.ylabel('luminosidade(lux)', fontdict=label)

plt.grid(axis = 'y', color = 'gray', linestyle = '--', linewidth = 0.7)
plt.legend()
plt.show()


#Movimento
plt.title("Movimento")
#plt.grid(axis = 'y', color = 'gray', linestyle = '--', linewidth = 0.7)
#plt.legend()
plt.hist(m)
#plt.plot(x, m, label='movimento', color='blue', marker='o')
plt.show()
'''
