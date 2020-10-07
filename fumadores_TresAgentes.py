import random
import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

papelEnMesa = False
fosforosEnMesa = False
tabacoEnMesa = False

def agente():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        
        with monitor:
            
            while not (papelEnMesa == False and fosforosEnMesa == False and tabacoEnMesa == False):
                monitor.wait()
            logging.info(f'El agente esta apunto de sortear')
            time.sleep(4)
            caso = random.choice([0,1,2]) #al azar pone dos cosas en la mesa
            if caso == 0:
                papelEnMesa = True
                tabacoEnMesa = True 
                logging.info(f'Listo, papel y tabaco en la mesa')
                time.sleep(2)
            if caso == 1:
                papelEnMesa = True
                fosforosEnMesa = True
                logging.info(f'Ah bueno, hay papel y fosforos en la mesa')
                time.sleep(2)
            if caso == 2:
                fosforosEnMesa = True
                tabacoEnMesa = True
                logging.info(f'Ok... fosforos y tabaco en la mesa')
                time.sleep(2)
            # esperar a reponer las cosas una vez que alguien haya tomado las dos anteriores

def fumadorConPapel():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        with monitor:
            while not (papelEnMesa == False and fosforosEnMesa == True and tabacoEnMesa == True) :
                monitor.wait()
            logging.info(f'Fumador armandose el pucho con su papel')
            logging.info(f'Fumando como loco...')
            time.sleep(2)
            valoresParaVolverASortear()

        # si hay fósforos y tabaco en la mesa
            # tomarlos
            # armar cigarrillo y fumar: se puede simular con un sleep
            # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar


def fumadorConFosforos():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        with monitor:
            while not (papelEnMesa == True and fosforosEnMesa == False and tabacoEnMesa == True):
                monitor.wait()
            logging.info(f'Fumador prendiento el pucho con sus fosforos')
            logging.info(f'Fumando como loco...')
            time.sleep(2)
            valoresParaVolverASortear()

        # si hay papel y tabaco en la mesa
            # tomarlos
            # armar cigarrillo y fumar: se puede simular con un sleep
            # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar

def fumadorConTabaco():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        with monitor:
            while not (papelEnMesa == True and fosforosEnMesa == True and tabacoEnMesa == False):
                monitor.wait()
            logging.info(f'Fumador armando el pucho con su tabaco')
            logging.info(f'Fumando como loco...')
            time.sleep(2)
            valoresParaVolverASortear()
 
        # si hay fósforos y papel en la mesa
            # tomarlos
            # armar cigarrillo y fumar: se puede simular con un sleep
            # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar

def valoresParaVolverASortear():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    papelEnMesa = False
    fosforosEnMesa = False
    tabacoEnMesa = False

def mesaDeFumadores(monitor):
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True: 
        
        with monitor: 
            
            monitor.notify()
            
        time.sleep(5)
            


monitor = threading.Condition()
agenteHilo = threading.Thread(target=agente)
fumadorConPapelHilo = threading.Thread(target=fumadorConPapel)
fumadorConFosforosHilo = threading.Thread(target=fumadorConFosforos)
fumadorConTabacoHilo = threading.Thread(target=fumadorConTabaco)

agenteHilo.start()
fumadorConPapelHilo.start()
fumadorConFosforosHilo.start()
fumadorConTabacoHilo.start()

mesaDeFumadores(monitor)