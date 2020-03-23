#! /usr/bin/python

#
# Description:
# ================================================================
# Time-stamp: "2020-03-23 18:49:29 trottar"
# ================================================================
#
# Author:  Richard L. Trotta III <trotta@cua.edu>
#
# Copyright (c) trottar
#
import math, sys, ROOT
import numpy as np
from ROOT import TLorentzVector

sys.path.insert(0,'/home/trottar/Programs/my_programs/physics_engine/src/')
import physics_calc

c = physics_calc.Constants
e = physics_calc.Equations

'''
2 body elastic collision
'''

# Incoming particles
p1 = TLorentzVector(0.,0.,275.,c.m_p)
print(p1)
p2 = TLorentzVector(0.,0.,18.,c.m_e)
print(p2)

p_inc_tot = p1+p2
print(p_inc_tot.E())
p_inc_inv = p_inc_tot.M2()
print(p_inc_inv)

# Outgoing particles
p3 = TLorentzVector()
print(p3)
p4 = TLorentzVector()
print(p4)

p_out_tot = p1+p2
print(p_out_tot.E())
p_out_inv = p_out_tot.M2()
print(p_out_inv)

e.scatter(c.m_p,[0,0,275],c.m_e,[0,0,18],2)
