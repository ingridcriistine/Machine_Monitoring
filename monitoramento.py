from machine import Pin
import time
import sensor_gas
import lm393_rpm
import giroscopio
import sensor_corrente
import sensor_temperatura
import sensor_nivel
import wifi
import motorPH

botao = Pin(18, Pin.IN)
buzzer = Pin(19, Pin.OUT)

giroscopio.init_giroscopio()
giro_inicial = giroscopio.read_gyro()

def verificar_giro(data_giro):
    for cord in range(3):
        if (data_giro[cord] > (giro_inicial[cord] + 600)) or (data_giro[cord] < (giro_inicial[cord] - 600)):
            return 0
    return 1

def verificar_sensores(data):
    
    valid = True
    
    if data["Sensor_Gas"] > 600:
        valid = False
        
    if data["Sensor_RPM"] > 600:
        valid = False
        
    if data["Sensor_Temp"] > 80:
       valid = False
        
    if not data["Sensor_Nivel"]:
        valid = False
        
    if not data["Sensor_Giro"]:
        valid = False
    
    return valid
        

while True:
    
    torno_gas = sensor_gas.read_gas()
    torno_rpm = lm393_rpm.read_rpm()
    torno_giro = verificar_giro(giroscopio.read_gyro())
    torno_temp = sensor_temperatura.read_dht11()
    torno_nivel = sensor_nivel.read_nivel()
    
    data = wifi.readFB()
    
    print(botao.value())
    
    if botao.value():
        data["Status"] = 0 if data["Status"] else 1

    motorPH.motor(data["Status"])

    data["Sensor_Gas"] = torno_gas
    data["Sensor_RPM"] = torno_rpm
    data["Sensor_Giro"] = torno_giro
    data["Sensor_Temp"] = torno_temp
    data["Sensor_Nivel"] = torno_nivel
    
    if not verificar_sensores(data) and data["Status"]:
        buzzer.on()
        data["Status"] = 0
        motorPH.motor(0)
        time.sleep(0.2)
        buzzer.off()
    
    wifi.enviarFire(data)
    time.sleep(1)