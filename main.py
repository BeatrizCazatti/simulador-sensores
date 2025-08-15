import numpy as np
from numpy import random
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

amostra = 20

hoje = datetime.now().strftime("%H:%M:%S")
periodo = pd.date_range(start=hoje, periods=amostra, freq='min')

temperatura = np.random.normal(loc=25, scale=20, size=amostra).round(2)
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
pd.DataFrame(data_frame).to_csv(f'registro_{datetime.now().strftime("%d_%m_%y")}', index=False)

limite_temperatura = 55
limite_luminosidade = 900

filtro_alertas = (data_frame['temperatura'] > limite_temperatura) | (data_frame['luminosidade'] > limite_luminosidade)
alertas = data_frame[filtro_alertas]

if not alertas.empty:
    print(f"[ALERTA] Condições Extremas:")
    print(alertas)

titulo = {'family': 'serif', 'size': '13', 'color': 'black'}
label = {'family': 'serif', 'size': '11', 'color': 'gray'}
x = dt["registro"]
t = dt["temperatura"]
l = dt["luminosidade"]
m = dt["movimento"]

fig, axs = plt.subplots(2, 1, sharex=True) 
fig.subplots_adjust(hspace=0.1)
fig.suptitle("Registro dos Sensores")

#Temperatura
axs[0].plot(x, t, 'o--', color='green')
axs[0].set_ylabel('Temperatura (°C)', fontdict = label, loc='top')
axs[0].grid(axis = 'x', color = 'gray', linestyle = '--', linewidth = 0.7)

#Luminosidade
axs[1].plot(x, l, 'o--', color='gold')
axs[1].set_ylabel('Luminosidade (lux)', fontdict = label, loc='bottom')
axs[1].set_xlabel('Tempo')
axs[1].grid(axis = 'x', color = 'gray', linestyle = '--', linewidth = 0.7)

#Movimento
plt.figure(figsize=(7, 5))
plt.title("Sensor de Movimento")

plt.plot(x, m, 'o', color = 'black', linestyle ='')
plt.grid(axis = 'x', color = 'gray', linestyle = '--', linewidth = 0.7)

plt.show()

