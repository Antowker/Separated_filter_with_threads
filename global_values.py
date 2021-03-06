
from math       import sin, pi 
import numpy as np

import threading

##--------------------------------------------------------
##------------------signal settings-----------------------
##--------------------------------------------------------
f_s_1 = 25
f_s_2 = 50
f_s_3 = 100
f_s_4 = 200
f_s_5 = 400
f_s_6 = 800

A   = 1

##--------------------------------------------------------
##------------------sample settings-----------------------
##--------------------------------------------------------
f_d = 22050
T   = 10.0
dt  = 1/f_d
t   = np.linspace(0.1, T, int(T * f_d), endpoint = False) # time variable

##---buffer for input data------
voltage = []

##----------------------------------------------------------
##-------------coefficient for first stage------------------
##----------------------------------------------------------
##section #1
a_coef_1_1 = [0.525828543039357776,
             -1.99315287833078858,
              0.997244104076249416]
b_coef_1_1 = [1,
             -1.99631885323521785,
              1] 

##section #2
a_coef_1_2 = [0.98514378788174306,
             -1.9665278007775604,
              0.971680540810641924]
b_coef_1_2 = [1,
             -1.99759749798163111,
              1] 

##section #3
a_coef_1_3 = [1.7899432111289777,
             -0.885200010264396653,
              0]
b_coef_1_3 = [1,
             -1,
              0] 

##----------------------------------------------------------
##-------------coefficient for second stage-----------------
##----------------------------------------------------------

##section #1
a_coef_2_1 = [0.780545597983568928,
             -1.98454172327042144,
              0.998468983060898374]
b_coef_2_1 = [1,
             -1.98640637335991888,
              1] 

##section #2
a_coef_2_2 = [0.780545597983568928,
             -1.98653531191395594,
              0.998576070222813805]
b_coef_2_2 = [1,
             -1.98764535316191138,
              1] 

##section #3
a_coef_2_3 = [1.62751709363638364,
             -1.97321776696518358,
              0.986087001680641895]
b_coef_2_3 = [1,
             -1.98704061332200621,
              1] 

##----------------------------------------------------------
##-------------coefficient for third stage------------------
##----------------------------------------------------------

##section #1
a_coef_3_1 = [0.780545597983568817,
             -1.94490255673515455,
              0.998496105813971191]
b_coef_3_1 = [1,
             -1.94703027431694564,
              1] 

##section #2
a_coef_3_2 = [0.780545597983568817,
             -1.94870398482269636,
              0.998548945297613622]
b_coef_3_2 = [1,
             -1.94949292626011861,
              1] 

##section #3
a_coef_3_3 = [1.6275170936363812,
             -1.93472288180304686,
              0.986087001680639008]
b_coef_3_3 = [1,
             -1.94827606259531683,
              1] 

##----------delay line for first stage-----------
##section #1
z_1_1 = 3*[0]
z_1_2 = 3*[0]
z_1_3 = 3*[0]

##----------delay line for second stage-----------
##section #2
z_2_1 = 3*[0]
z_2_2 = 3*[0]
z_2_3 = 3*[0]

##----------delay line for thrid stage-----------
##section #3
z_3_1 = 3*[0]
z_3_2 = 3*[0]
z_3_3 = 3*[0]

##------------general list of delay line----------
Z = [[z_1_1,z_1_2,z_1_3], [z_2_1,z_2_2,z_2_3], [z_3_1,z_3_2,z_3_3]]

##-----------list for filtred voltage--------------
filt_volt = []
X = 0
Y = 0
##-----set events for threads--------
e1 = threading.Event()
e2 = threading.Event()





