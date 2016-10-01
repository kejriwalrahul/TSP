#!/usr/bin/env python
from random import random
import math

def sa(sNode, sTemp, fTemp, iters, random_neighbour, deltaE, nextTemp):
    cNode = sNode
    cTemp = sTemp
    while cTemp > fTemp:
        for i in range(iters):
            nNode = random_neighbour(cNode)
            dE = deltaE(nNode, cNode)
            p=random()
            pcn = 1/(1+pow(math.e, -dE/cTemp))
            if p < pcn:
                cNode = nNode
        cTemp = nextTemp(cTemp)
    return cNode
    
