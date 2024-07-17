import dht
from machine import Pin
import time

# Configura o pino onde o DHT11 está conectado
dht_sensor = dht.DHT11(Pin(27))

# Função principal para ler o sensor DHT11
def read_dht11():
    while True:
        try:
            dht_sensor.measure()
            temp = dht_sensor.temperature()
            hum = dht_sensor.humidity()
            print(f"Temperatura: {temp}°C  Umidade: {hum}%")
            
            
        except OSError as e:
            print("Falha na leitura do sensor:", e)
        
        # Aguarda dois segundos antes de ler novamente
        time.sleep(2)
    
        

# Chama a função principal
read_dht11()