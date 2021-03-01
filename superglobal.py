#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 21:39:44 2021

@author: kaydee
"""
import pickle
with open('counter.pickle', 'rb') as f:
    counter = pickle.load(f)
    
counter[10] = 0

with open("counter.pickle", 'wb') as f:
    pickle.dump(counter, f)

    
    
