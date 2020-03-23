#! /usr/bin/python

#
# Description:
# ================================================================
# Time-stamp: "2020-03-23 11:38:56 trottar"
# ================================================================
#
# Author:  Richard L. Trotta III <trotta@cua.edu>
#
# Copyright (c) trottar
#

import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

from feynman import Diagram


fig = matplotlib.pyplot.figure(figsize=(1.,1.))
ax = fig.add_axes([0,0,10,10], frameon=False)
diagram = Diagram(ax)
diagram.text(.5,0.9,"Vector Boson Fusion (VBF)",fontsize=40)
in1 = diagram.verticle(xy=(.1,.8), marker='')
in2= diagram.verticle(xy=(.1,.2), marker='')
v1 = diagram.verticle(xy=(.4,.7))
v2 = diagram.verticle(xy=(.4,.3))
v3 = diagram.verticle(xy=(.6,.5))
out1 = diagram.verticle(xy=(.9,.8), marker='')
out2 = diagram.verticle(xy=(.9,.2), marker='')
higgsout = diagram.verticle(xy=(.9,.5))

q1 = diagram.line(in1, v1, arrow=False)
q2 = diagram.line(in2, v2, arrow=False)
wz1 = diagram.line(v1, v3, style='wiggly')
wz2 = diagram.line(v2, v3, style='wiggly')
higgs = diagram.line(v3, higgsout, style='double', arrow=False)
q3 = diagram.line(v1, out1, arrow=False)
q4 = diagram.line(v2, out2, arrow=False)

q1.text("$q_1$",fontsize=30)
q2.text("$q_2$",fontsize=30)
diagram.text(v3.xy[0], v3.xy[1]+0.11, "$Z/W^\pm$",fontsize=35)
wz2.text("$Z/W^\pm$",fontsize=35)
q3.text("$q_3$",fontsize=30)
q4.text("$q_4$",fontsize=30)
higgs.text("$H$",fontsize=30)

diagram.plot()
fig.savefig('OUTPUTS/VBF-feyn.pdf',bbox_inches='tight')
