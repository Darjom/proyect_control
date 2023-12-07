#!/usr/bin/python

from calendar import weekday
from pickle import TRUE
import time
import threading
from datetime import date, datetime
from datetime import timedelta
from time import sleep
import string
from tkinter import Tk, Label, Entry, Button, END
from PIL import ImageTk, Image
from captcha.image import ImageCaptcha
import importlib


global fecha_inicio
global fecha_actual
global diferencia
# Se crea el objeto cear_Captcha y check
def captcha():
    from Captcha_app import crear_Captcha,check
    time.sleep(0.5)

def ejecucion_horaria(diferencia,fecha_inicio,fecha_actual):
    while TRUE:
        hoy = datetime.now()
        hora1 = datetime(hoy.year, hoy.month, hoy.day, 22,58,0)
        hora2 = datetime(hoy.year, hoy.month, hoy.day, 23,30,0)
        dia=fecha_actual.weekday()
        fecha_actual=datetime.now()
        diferencia=(fecha_actual-fecha_inicio).seconds
        time.sleep(1)
        if dia==4:
            if hoy>hora1:
                if hoy<hora2:
                    time.sleep(1)
                    print(diferencia)
                    if hilo2.is_alive()==True:
                        if diferencia>=30:
                            import correo
                            time.sleep(0.5)
                            hilo2.join()
                            time.sleep(1)                       
                    else:
                        print("estoy en el else")
                        if hilo2.is_alive()==True:
                            hilo2.join()
                        else:
                            fecha_inicio=datetime.now()
                            hilo2.start()
                            time.sleep(1)
                            hilo2.join()
                            time.sleep(0.5)    
    time.sleep(0.5)

# Aqui creamos el thread.
# El primer argumento es el nombre de la funcion que contiene el codigo.
# El segundo argumento es una lista de argumentos para esa funcion.
fecha_inicio=datetime.now()
fecha_actual=datetime.now()
diferencia=(fecha_actual-fecha_inicio).seconds

hilo = threading.Thread(target=ejecucion_horaria, args=(diferencia,fecha_inicio,fecha_actual),daemon=True)
hilo2 = threading.Thread(target=captcha,daemon=False)
hilo.start()   # Iniciamos la ejecución del thread,

time.sleep(1)
# La ejecución sigue de inmediato aqui, mientras el thread 
# ejecuta en paralelo.
while TRUE:
    a=0



    

