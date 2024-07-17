import pyodbc
import time
import numpy as np
#import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import json
import requests

def InserirBD(sinal):
    server = ''
    database = 'ProjetoFinalIOT'
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')
    cursor = cnxn.cursor()
    cursor.execute(f"INSERT into Torno (Sensor_Gas, Sensor_RPM, Sensor_Corrente, Sensor_Temp, Sensor_Nivel) VALUES ({sinal[0]},{sinal[1]},{sinal[2]},{sinal[3]},{sinal[4]})")
    cursor.commit()
    print("Inserido com sucesso!")


proxies = {'https': "http://"}

while True:
    url = 'https://'
    info = json.loads(requests.get(url,proxies=proxies).content)

    gas = json.loads(requests.get(url,proxies=proxies).content)['Sensor_Gas']
    rpm = json.loads(requests.get(url,proxies=proxies).content)['Sensor_RPM']
    corrente = json.loads(requests.get(url,proxies=proxies).content)['Sensor_Corrente']
    temperatura = json.loads(requests.get(url,proxies=proxies).content)['Sensor_Temp']
    nivel = json.loads(requests.get(url,proxies=proxies).content)['Sensor_Nivel']

    valores = (gas,rpm,corrente,temperatura,nivel)
    print(valores)
    InserirBD(valores)
    time.sleep(1)