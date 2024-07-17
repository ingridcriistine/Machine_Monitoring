import pyodbc
import time
import requests
import json
import matplotlib.pyplot as plt
import pandas as pd

proxies = {"https": "http://"}

url = 'https://'

def InserirBD(sinal):
    server = ''
    database = 'Monitoramento'
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')
    cursor = cnxn.cursor()
    cursor.execute(f"insert into Torno(gas, temperature, rpm, nivel, giro, stat) values({sinal[0]}, {sinal[1]}, {sinal[2]}, {sinal[3]}, {sinal[4]}, {sinal[5]})")
    cursor.commit()
    print("Inserido com sucesso!")


def apresentar(sinal):
    print(f"Gas: {sinal[0]}")
    print(f"Temperatura: {sinal[1]}")
    print(f"RPM: {sinal[2]}")
    print(f"Nivel: {sinal[3]}")
    print(f"Oscilação Giroscópio: {sinal[4]}")
    print(f"Status: {sinal[5]}")

    
def AttBD():
    torno_data = requests.get(url, proxies=proxies).content

    torno_gas = json.loads(torno_data)["Sensor_Gas"]
    torno_temp = json.loads(torno_data)["Sensor_Temp"]
    torno_rpm = json.loads(torno_data)["Sensor_RPM"]
    torno_nivel = json.loads(torno_data)["Sensor_Nivel"]
    torno_giro = json.loads(torno_data)["Sensor_Giro"]
    torno_stat = json.loads(torno_data)["Status"]

    

    apresentar((torno_gas, torno_temp, torno_rpm, torno_nivel, torno_giro, torno_stat))

    InserirBD((torno_gas, torno_temp, torno_rpm, torno_nivel, torno_giro, torno_stat))
    time.sleep(1)


while True:
    AttBD()
    time.sleep(2)
