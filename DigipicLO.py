#******************************Import funksjoner******************************
from time import sleep

import pygame
pygame.init()

import pifacedigitalio as p
p.init()

import random


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

RanNum = 0
RanNumBS = format(RanNum, '07b')
Tid = 0

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
    if Key2:
        Rele = True

        print('Tilfeldig tall: ' + repr(RanNum))
        print('Aktive bit: ' + repr(RanNumBS))
        print('VifteHalv: ' + repr(VifteHalv))
        print('VifteHel: ' + repr(VifteHel))
        print('Pumper: ' + repr(Pumper))
        print('ReimAl: ' + repr(ReimAl))
        print('VifterAl: ' + repr(VifterAl))
        print('FilterAl: ' + repr(FilterAl))
        print('FrostAl: ' + repr(FrostAl))
        print('Tid: ' + repr(Tid) + ' sek')
        
        RanNum = random.randint(1, 127)
        RanNumBS = format(RanNum, '07b')
        
        RanNumB1 = int(RanNumBS[6])
        RanNumB2 = int(RanNumBS[5])
        RanNumB3 = int(RanNumBS[4])
        RanNumB4 = int(RanNumBS[3])
        RanNumB5 = int(RanNumBS[2])
        RanNumB6 = int(RanNumBS[1])
        RanNumB7 = int(RanNumBS[0])
        
        if RanNumB1 == 1:
            VifteHalv = True
        if RanNumB1 == 0:
            VifteHalv = False

        if RanNumB2 == 1:
            VifteHel = True
        if RanNumB2 == 0:
            VifteHel = False

        if RanNumB3 == 1:
            Pumper = True
        if RanNumB3 == 0:
            Pumper = False   

        if RanNumB4 == 1:
            ReimAl = True
        if RanNumB4 == 0:
            ReimAl = False

        if RanNumB5 == 1:
            VifteAl = True
        if RanNumB5 == 0:
            VifteAl = False

        if RanNumB6 == 1:
            FilterAl = True
        if RanNumB6 == 0:
            FilterAl = False

        if RanNumB7 == 1:
            FrostAl = True
        if RanNumB7 == 0:
            FrostAl = False


        TidRan = random.randint(1, 100)
        Tid = TidRan/10 
        sleep(Tid)


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

        if Teller1 >= 2: #Aktiverer stopp hvis knapp holdes inne i 3 sekunder
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
