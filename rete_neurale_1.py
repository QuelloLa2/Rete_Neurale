import math
import random as rand

cicli = 10000

learning_rate = 0.9
peso_1 = rand.random()
peso_2 = rand.random()
bias = rand.random()
print(f"P1 {peso_1}")
print(f"P2 {peso_2}")
print(f"B {bias}\n\n")

blu_data = [
    [0.5, 1, 0],
    [1, 0.9, 0],
    [0.75, 0.5, 0]
]
red_data = [
    [1.6, 1.4, 1],
    [1.6, 1.8, 1],
    [2, 1.5, 1]
]

data = blu_data + red_data

# Funzioni utili
def sigmoide(x):
    return 1 / (1 + math.exp(-x))

def dev_sigmoide(output):
    return output * (1 - output)

def bellman(x, y):
    return x * peso_1 + y * peso_2 + bias

def cambio_peso(peso, errore, der, z):
    return peso + learning_rate * errore * der * z

#Learning
for i in range(cicli):
    errore_totale = 0
    for punto in data:
        x, y , valore = punto
        # Feedforward
        output_grezzo = bellman(x, y)
        output = sigmoide(output_grezzo)

        # Backpropagation
        errore = valore - output
        derivata = dev_sigmoide(output)
        
        # Aggiornamento pesi
        peso_1 = cambio_peso(peso_1, errore, derivata, x)
        peso_2 = cambio_peso(peso_2, errore, derivata, y)
        bias = cambio_peso(bias, errore, derivata, 1)
        
        errore_totale += abs(errore)
        
#Risultati
print(f"Err: {errore_totale}")
print(f"P1 {peso_1}")
print(f"P2 {peso_2}")
print(f"B {bias}\n")

punto_1 = [2,2,1]

print(f"Previsione {punto_1}:")
x, y , valore = punto_1
previsione = sigmoide(bellman(x, y))
print("Valore: {} - Predict: {:.5f}".format(valore,previsione))

punto_2 = [0.5,0.5,0]

print(f"Previsione {punto_2}:")
x, y , valore = punto_2
previsione = sigmoide(bellman(x, y))
print("Valore: {} - Predict: {:.5f}".format(valore,previsione))

