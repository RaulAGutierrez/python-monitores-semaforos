import random
import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

papelEnMesa = False
fosforosEnMesa = False
tabacoEnMesa = False


def agentePapel():
        global papelEnMesa, fosforosEnMesa, tabacoEnMesa
        while True:
            with monitor:
                while (papelEnMesa):
                    monitor.wait()
                logging.info(f'Este agente del ingrediente papel esta apunto de sortear')
                time.sleep(2)
                caso = random.choice([0,1]) #al azar
                if caso == 1:
                    papelEnMesa = True
                    logging.info(f'El ingrediente papel esta en la mesa')
                    time.sleep(3)
            # esperar a reponer las cosas una vez que alguien haya tomado las dos anteriores

def agenteFosforo():
        global papelEnMesa, fosforosEnMesa, tabacoEnMesa
        while True:
            with monitor:
                while (fosforosEnMesa):
                    monitor.wait()
                logging.info(f'Este agente del ingrediente fosforo esta apunto de sortear')
                time.sleep(2)
                caso = random.choice([0,1]) #al azar
                if caso == 1:
                    fosforosEnMesa = True
                    logging.info(f'El ingrediente fosforo esta en la mesa')
                    time.sleep(3)
            # esperar a reponer las cosas una vez que alguien haya tomado las dos anteriores

def agenteTabaco():
        global papelEnMesa, fosforosEnMesa, tabacoEnMesa
        while True:       
            with monitor:         
                while (tabacoEnMesa):
                    monitor.wait()
                logging.info(f'Este agente del ingrediente tabaco esta apunto de sortear')
                time.sleep(2)
                caso = random.choice([0,1]) #al azar
                if caso == 1:
                    tabacoEnMesa = True
                    logging.info(f'El ingrediente tabaco esta en la mesa')
                    time.sleep(3)
            # esperar a reponer las cosas una vez que alguien haya tomado las dos anteriores


def fumadorConPapel():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        with monitor:
            while not (fosforosEnMesa == True and tabacoEnMesa == True) :
                monitor.wait()
            logging.info(f'Fumador armandose el pucho con su papel')
            logging.info(f'Fumando como loco...')
            time.sleep(2)
            papelEnMesa = False
            fosforosEnMesa = False
        # si hay fósforos y tabaco en la mesa
            # tomarlos
            # armar cigarrillo y fumar: se puede simular con un sleep
            # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar


def fumadorConFosforos():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        with monitor:
            while not (papelEnMesa == True  and tabacoEnMesa == True):
                monitor.wait()
            logging.info(f'Fumador prendiento el pucho con sus fosforos')
            logging.info(f'Fumando como loco...')
            time.sleep(2)
            papelEnMesa = False
            tabacoEnMesa = False
        # si hay papel y tabaco en la mesa
            # tomarlos
            # armar cigarrillo y fumar: se puede simular con un sleep
            # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar

def fumadorConTabaco():
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True:
        with monitor:
            #while not (papelEnMesa == True and fosforosEnMesa == True and tabacoEnMesa == False):
            while not (papelEnMesa == True and fosforosEnMesa == True):
                monitor.wait()
            logging.info(f'Fumador armando el pucho con su tabaco')
            logging.info(f'Fumando como loco...')
            time.sleep(2)
            papelEnMesa = False
            fosforosEnMesa = False
        # si hay fósforos y papel en la mesa
            # tomarlos
            # armar cigarrillo y fumar: se puede simular con un sleep
            # llamar de nuevo a agente para que reponga en la mesa dos cosas al azar

def mesaDeFumadores(monitor):
    global papelEnMesa, fosforosEnMesa, tabacoEnMesa
    while True: 
        
        with monitor: 
            
            monitor.notify()

            

monitor = threading.Condition()

#agenteHilo = threading.Thread(target=agente)
agentePapel = threading.Thread(target=agentePapel)
agenteFosforo = threading.Thread(target=agenteFosforo)
agenteTabaco = threading.Thread(target=agenteTabaco)

fumadorConPapelHilo = threading.Thread(target=fumadorConPapel)
fumadorConFosforosHilo = threading.Thread(target=fumadorConFosforos)
fumadorConTabacoHilo = threading.Thread(target=fumadorConTabaco)

#agenteHilo.start()
agentePapel.start()
agenteFosforo.start()
agenteTabaco.start()
fumadorConPapelHilo.start()
fumadorConFosforosHilo.start()
fumadorConTabacoHilo.start()

mesaDeFumadores(monitor)