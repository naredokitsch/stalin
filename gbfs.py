#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 12:39:57 2017

@author: stan
"""
import heapq
from utils import ruta

class GBFS:
    def search(origen,stop,heuristica):
        agenda = []
        expandidos = set()
        if stop(origen):
            return ruta(origen)
        heapq.heappush(agenda,(0,origen))
        while agenda:
            nodo = heapq.heappop(agenda)[1]
            expandidos.add(nodo)
            if stop(nodo):
                return ruta(nodo)
            for hijo in nodo.expand():
                if hijo not in expandidos:
                    heapq.heappush(agenda,\
                                   (heuristica(hijo),hijo))