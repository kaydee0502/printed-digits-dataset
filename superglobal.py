#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 21:39:44 2021

@author: kaydee
"""
import pickle
counter = {x:0 for x in range(0,10)}





with open("counter.pickle", 'wb') as f:
    pickle.dump(counter, f)
    
    
    
