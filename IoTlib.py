#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Celsius to Fahrenheit conversion 
def c2f(c):
    try:
        f = round((float(c)*9/5)+32,1)
    except:
        f = "C2F Error"
    return f