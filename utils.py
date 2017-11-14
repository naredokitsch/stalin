#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 10:49:00 2017

@author: stan
"""
from collections import deque
def ruta(end):
    secuencia = deque()
    secuencia.append(end)
    while end.parent:
        end = end.parent
        secuencia.append(end)
    secuencia.reverse()
    return list(secuencia)

