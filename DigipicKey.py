#******************************Import funksjoner******************************
from time import sleep

import pygame
pygame.init()

import pifacedigitalio as p
p.init()



#******************************Variabler******************************
Rele = False
VifteHalv = False
VifteHel = False
Pumper = False
ReimAl = False
VifterAl = False
FilterAl = False
FrostAl = False

ReleTOF = False
ReleTON = True

LesDI = True

Pulse1 = 0 #Pulse for nokkel posisjon 1
Pulse2 = 0 #Pulse for nokkel posisjon 2

Teller1 = 0 #Teller for aktiver knapp

Stop = False

Run = True


#******************************Start program******************************
while Run:

    #*****Leser digitale innganger*****
    if not LesDI:
        sleep(0.05)
        LesDI = True
    if LesDI:
        Key1 = p.digital_read(4) #Nokkel pos 1
        Key2 = p.digital_read(5) #Nokkel pos 2
        Knapp = p.digital_read(6) #Rod knapp
        LesDI = False


    #*****Styrer rele med TimerOn og TimerOff*****
    if Rele and ReleTON:
        p.digital_write(0,1)
        sleep(0.15)
        ReleTOF = True
        ReleTON = False
    if not Rele and ReleTOF:
        p.digital_write(0,0)
        sleep(0.15)
        ReleTON = True
        ReleTOF = False


    #*****Styrer LED av og paa*****
    if VifteHalv:
        p.digital_write(1,1)
    if not VifteHalv:
        p.digital_write(1,0)

    if VifteHel:
        p.digital_write(2,1)
    if not VifteHel:
        p.digital_write(2,0)

    if Pumper:
        p.digital_write(3,1)
    if not Pumper:
        p.digital_write(3,0)

    if ReimAl:
        p.digital_write(4,1)
    if not ReimAl:
        p.digital_write(4,0)

    if VifterAl:
        p.digital_write(5,1)
    if not VifterAl:
        p.digital_write(5,0)

    if FilterAl:
        p.digital_write(6,1)
    if not FilterAl:
        p.digital_write(6,0)

    if FrostAl:
        p.digital_write(7,1)
    if not FrostAl:
        p.digital_write(7,0)
        

    #*****Funksjon ved nokkel posisjon 1*****
    if Key1 and Pulse1 == 0:
        VifteHalv = False
        VifteHel = False
        Pumper = False
        VifterAl = False
        FilterAl = False
        FrostAl = False
        
        Rele = True
        ReimAl = True
        
        sleep(0.5)

    if Key1 and Pulse1 == 1:
        VifteHalv = False
        VifteHel = False
        Pumper = False
        VifterAl = False
        FilterAl = False
        FrostAl = False
        
        Rele = True
        ReimAl = False
        
        sleep(0.5)


    #*****Funksjon ved nokkel posisjon 2*****
    if Key2 and Pulse2 == 2:
        sleep(0.5)
        VifteHel = True

    if Key2 and Pulse2 == 1:
        sleep(3.0)
        VifteHalv = False

        Pulse2 = Pulse2 +1

    if Key2 and Pulse2 == 0:     
        VifteHalv = False
        VifteHel = False
        Pumper = False
        ReimAl = False
        VifterAl = False
        FilterAl = False
        FrostAl = False
        
        Rele = True
        VifteHalv = True
        Pumper = True

        Pulse2 = Pulse2 +1

    if not Key2:
        Pulse2 = 0


   #*****Funksjon ved nokkel posisjon 0*****     
    if not Key1 and not Key2:

        sleep(0.5)
        
        Rele = False
        VifteHalv = False
        VifteHel = False
        Pumper = False
        ReimAl = False
        VifterAl = False
        FilterAl = False
        FrostAl = False


    #*****Teller for knapp inne*****
    if Knapp:
        Teller1 = Teller1 + 1
        sleep(0.1)

        if Teller1 >= 3: #Aktiverer stopp hvis knapp holdes inne i 3 sekunder
            Stop = True #Variabel for stopp av program
    if not Knapp:
        Teller1 = 0


    #*****Pulsfunksjon for nokkel posisjon 1*****
    Pulse1 = Pulse1 + 1
    if Pulse1 >= 2:
        Pulse1 = 0


    #*****Stoppfunksjon*****    
    if Stop:
        sleep(0.2)
        p.digital_write(0,0)
        p.digital_write(1,0)
        p.digital_write(2,0)
        p.digital_write(3,0)
        p.digital_write(4,0)
        p.digital_write(5,0)
        p.digital_write(6,0)
        p.digital_write(7,0)
        Teller = 0

        Run = 0 #Avslutter program
