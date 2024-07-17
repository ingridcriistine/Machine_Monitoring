from machine import Pin, ADC
import time

# Define o pino ao qual o sensor está conectado (por exemplo, GPIO 34)
pino_sensor = 32

# Configura o ADC para ler o pino especificado
adc = ADC(Pin(pino_sensor))
adc.width(ADC.WIDTH_12BIT)   # Resolução de 12 bits (0-4095)
adc.atten(ADC.ATTN_11DB)     # Faixa de tensão de entrada de 0-3.6V

# Função para ler e calcular a corrente com base no valor ADC
def ler_corrente():
    valor_adc = adc.read()
    tensao = (valor_adc / 4095.0) * 3.6  # Converter para tensão (em volts)
    
    # Ajuste necessário dependendo da sensibilidade do ACS712 utilizado
    sensibilidade = 0.185  # Exemplo para ACS712-30A (mV/A)
    corrente = (tensao - 1.65) / sensibilidade
    
    return corrente

# Loop principal para leitura contínua
while True:
    corrente = ler_corrente()
    print("Corrente:", corrente, "A")
    time.sleep(1)  # Aguarda 1 segundo entre as leituras
