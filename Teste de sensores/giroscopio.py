import machine
import time
import ustruct

# Definições de endereços e registradores do sensor MPU9250
sensor_MPU9250 = 0x68
power = 0x6B
coord_X = 0x43
#coord_Y = 0x45
#coord_Z = 0x47

# Inicialização do I2C
giroscopio = machine.I2C(0, scl=machine.Pin(21), sda=machine.Pin(22))

# Função para escrever bytes nos registradores
def init_giroscopio():
    giroscopio.writeto_mem(sensor_MPU9250, power, bytearray([0x00]))

# Função para ler os dados do giroscópio
def read_gyro():
    gyro_data = giroscopio.readfrom_mem(sensor_MPU9250, coord_X, 6)
    gyro_x, gyro_y, gyro_z = ustruct.unpack('>hhh', gyro_data)
    
    print(f'Giroscópio: X = {gyro_x} | Y = {gyro_y} | Z = {gyro_z}')
    return gyro_x, gyro_y, gyro_z

