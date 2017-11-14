#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 13:11:25 2017

@author: stan
"""
from utils import ruta
class BS:
    @staticmethod
    def search(origen,destino):
        expandidos = set()
        if origen==destino:
            return ruta(origen)
        f_adelante = {origen:origen}
        f_atras = {destino:destino}
        while f_adelante and f_atras:
            #exp en frontera adelante
            temp_adelante = {}
            for n in f_adelante:
                expandidos.add(n)
                if n in f_atras:
                    r = ruta(f_atras[n])[:-1]
                    r.reverse()
                    return ruta(n)+r
                for hijo in n.expand():
                    if hijo not in expandidos:
                        temp_adelante[hijo]=hijo
            f_adelante = temp_adelante
            # exp en frontera atras
            temp_atras = {}
            for n in f_atras:
                expandidos.add(n)
                if n in f_adelante:
                    r = ruta(n)[:-1]
                    r.reverse()
                    return ruta(f_adelante[n])+r
                for hijo in n.expand():
                    if hijo not in expandidos:
                        temp_atras[hijo]=hijo
            f_atras = temp_atras
        return None