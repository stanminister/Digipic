from time import sleep

import pygame
pygame.init()

import pifacedigitalio as p
p.init()

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

RE1 = True
RE2 = True
RE3 = True
RE4 = True
RE5 = True
RE6 = True
RE7 = True
RE8 = True

Pulse1 = False

Stopper = 0
Stop = False

Run = True

while Run:

    if not LesDI:
        sleep(0.2)
        LesDI = True
    if LesDI:
        Key1 = p.digital_read(4) #(Nokkel pos 1)
        Key2 = p.digital_read(5) #(Nokkel pos 2)
        Knapp = p.digital_read(6) #(Rod knapp)
        LesDI = False

    if Rele and ReleTON:
        p.digital_write(0,1)
        sleep(0.25)
        ReleTOF = True
        ReleTON = False
    if not Rele and ReleTOF:
        p.digital_write(0,0)
        sleep(0.25)
        ReleTON = True
        ReleTOF = False

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
        
    
    if Key1 and not Pulse1:
        VifteHalv = False
        VifteHel = False
        Pumper = False
        VifterAl = False
        FilterAl = False
        FrostAl = False
        
        Rele = True
        ReimAl = False
        
        sleep(1.0)
        ReimAl = True
        sleep(1.0)
        Pulse1 = True

    if Pulse1:
        sleep(1.0)
        Pulse1 = False
        

    if Key2 and RE8:
        
        sleep(0.2)
        
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

        sleep(3.0)
        
        VifteHalv = False

        sleep(0.5)

        VifteHel = True

        RE8 = False

    if not Key2:
        RE8 = True
        
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

    if Knapp:
        Stopper = Stopper + 1
        sleep(0.1)

        if Stopper >= 5:
            Stop = True
    if not Knapp:
        Stopper = 0
        
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
        Stopper = 0
        Run = 0
        
