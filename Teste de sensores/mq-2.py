from machine import ADC, Pin
import time

# Define o pino ao qual o sensor está conectado (por exemplo, GPIO 34)
pino_sensor = 33

# Configuração do ADC
sensor_gas = ADC(Pin(pino_sensor))
sensor_gas.width(ADC.WIDTH_10BIT)   # Resolução de 10 bits (0-1023)
sensor_gas.atten(ADC.ATTN_11DB)     # Faixa de tensão de entrada de 0-3.6V

# Função para ler e calcular a concentração de gás com base no valor ADC
def ler_concentracao_gas():
    valor_sensor = sensor_gas.read()
    tensao = (valor_sensor / 1023.0) * 2.7  # Converter para tensão (em volts)
    print(valor_sensor)
    
    # Calibração para diferentes gases (valores típicos, pode variar com a calibração específica)
    # Ajuste os valores abaixo conforme a calibração do seu sensor MQ-2
    if tensao < 1.0:
        concentracao = 0.0
    elif tensao < 2.0:
        concentracao = (tensao - 1.0) * 50.0
    else:
        concentracao = (tensao - 2.0) * 100.0 + 50.0
    
    return concentracao

# Loop principal para leitura contínua
while True:
    concentracao = ler_concentracao_gas()
    print("Concentração de gás:", concentracao, "ppm")
    time.sleep(1)  # Aguarda 1 segundo entre as leituras
