#! /usr/bin/python

#
# Description:
# ================================================================
# Time-stamp: "2020-03-23 18:57:46 trottar"
# ================================================================
#
# Author:  Richard L. Trotta III <trotta@cua.edu>
#
# Copyright (c) trottar
#

import math, ROOT
import numpy as np
from ROOT import TLorentzVector

class Constants:

    def __new__(*args, **kwargs):
        """Constants cannot be created"""
        raise NotImplementedError('Error')
    '''
    Physical Constants
    '''
    m_e = 0.511e-3 # Electron mass (GeV)
    m_p = 938e-3 # proton mass (GeV)


class Equations:

    def __new__(*args, **kwargs):
        """Constants cannot be created"""
        raise NotImplementedError('Error')
    
    '''
    Equations
    '''

    def scatter(m1,inp_p1,m2,inp_p2,numFinal):
        # Incoming particles
        p1 = TLorentzVector(inp_p1[0],inp_p1[1],inp_p1[2],m1)
        p2 = TLorentzVector(inp_p2[0],inp_p2[1],inp_p2[2],m2)
        inc_part = "Incident particles: p1=[{},{},{},{}] p1=[{},{},{},{}]".format(p1[0],p1[1],p1[2],p1[3],p2[0],p2[1],p2[2],p2[3])
        print(inc_part)
        
        p_inc_tot = p1+p2
        p_inc_inv = p_inc_tot.M2()
        inc_part_tot = "                    p_tot=p1+p2 |p|^2={}".format(p_inc_inv)
        print(inc_part_tot)

        if numFinal > 2:
            p3 = TLorentzVector()
            p4 = TLorentzVector()
            p5 = TLorentzVector()
        else:
            p3 = TLorentzVector()
            p4 = TLorentzVector()

            p1_p3 = p1-p3
            p2_p4 = p2-p4

            inc_part_1 = "Incident particles: p1-p3=p2-p4"
            inc_part_2 = "                    (p1-p3)^2=(p2-p4)^2"
            inc_part_3 = "                    p1^2+p3^2-2(E1E3-)"

            # Outgoing particles
            p_out_tot = p1+p2
            print(p_out_tot.E())
            p_out_inv = p_out_tot.M2()
            print(p_out_inv)
