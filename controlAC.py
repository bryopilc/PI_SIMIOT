#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : PI Integracion de sistemas IoT (Pilco - García)
# Created Date: 30/7/22
# version ='1.0'

import sys
import requests
import broadlink
import time
import kaiTemp as kaiterra
#from .API.main import *

macRM=bytes(b'$\xdf\xa7P\x12\x14')
temp=0.0
#stateAPI=estadoActual()
#Señales IR

on = b'&\x00\xca\x00\x90\x90\x125\x12\x11\x124\x134\x12\x11\x13\x11\x124\x13\x10\x13\x11\x124\x13\x11\x12\x11\x124\x134\x13\x10\x134\x124\x13\x11\x124\x134\x124\x134\x133\x134\x13\x10\x134\x13\x10\x13\x11\x12\x11\x12\x11\x13\x10\x13\x11\x12\x11\x13\x10\x13\x10\x13\x11\x12\x11\x13\x10\x13\x11\x12\x11\x133\x134\x134\x124\x134\x133\x134\x134\x12\xaa\x92\x8f\x124\x13\x11\x124\x132\x15\x10\x13\x11\x124\x13\x10\x13\x11\x124\x13\x11\x12\x11\x134\x124\x13\x11\x124\x134\x12\x11\x134\x124\x134\x134\x124\x134\x13\x10\x134\x13\x10\x13\x11\x12\x11\x13\x10\x13\x10\x13\x11\x12\x11\x13\x10\x13\x11\x12\x11\x13\x10\x13\x11\x12\x11\x13\x10\x134\x133\x134\x134\x124\x134\x134\x124\x13\x00\r\x05'

'''b'&\x00\xbc\x01q9\x0f\r\x0f*\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e+\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f*\x0f*\x0f*\x0f\x0e\x0e\x0e\x0f*\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f*\x0f*\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x00\x01Tr9\x0f\r\x0f*\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f*\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f*\x0f*\x0f*\x0f\x0e\x0e\x0e\x0f*\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e+\x0e\x0e\x0f\x0e\x0e+\x0e+\x0e+\x0e\x0e\x0f\x0e\x0e\x0e\x0f*\x0f\x0e\x0e\x0e\x0f*\x0f*\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e*\x0f*\x0f*\x0f*\x0f*\x0f*\x0f\x0e\x0f*\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\x0e\x0e\x0e\x0f\r\x0f\x0e\x0f\x0e\x0e\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f*\x0f*\x0f*\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x12\x0b\x0f\r\x0f*\x0f*\x0f*\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0e\x0e\x0f*\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f*\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f*\x0f*\x0f*\x0f*\x0f*\x0f*\x0f\x0e\x0e*\x0f\x00\r\x05'
'''

off =b'&\x00\xca\x00\x91\x8f\x133\x13\x11\x124\x134\x13\x10\x13\x11\x124\x13\x11\x12\x11\x124\x13\x11\x12\x11\x134\x124\x13\x10\x134\x13\x10\x134\x134\x124\x134\x12\x11\x134\x124\x134\x13\x10\x13\x11\x12\x11\x13\x10\x134\x13\x10\x13\x10\x134\x134\x124\x13\x11\x12\x11\x13\x10\x13\x11\x12\x11\x13\x10\x13\x10\x13\x11\x124\x134\x134\x124\x134\x13\xaa\x91\x8f\x134\x13\x10\x134\x133\x13\x11\x13\x10\x134\x12\x11\x13\x11\x124\x13\x10\x13\x11\x124\x134\x13\x10\x134\x13\x10\x134\x134\x124\x134\x13\x10\x134\x134\x124\x13\x11\x12\x11\x13\x10\x13\x11\x124\x13\x11\x12\x11\x134\x124\x134\x13\x10\x13\x11\x12\x11\x13\x10\x13\x11\x12\x11\x13\x10\x13\x11\x124\x134\x134\x123\x144\x12\x00\r\x05' 

'''b'&\x00\xbc\x01r8\x0f\x0e\x0f*\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f*\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f*\x0f*\x0e+\x0f\r\x0f\x0e\x0e+\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e+\x0e+\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x00\x01Rt8\x0f\x0e\x0f*\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e*\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f*\x0f*\x0f*\x0f\r\x0f\x0e\x0f*\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f*\x0f*\x0f*\x0e\x0e\x0f\x0e\x0f\r\x0f*\x0f\x0e\x0f\r\x0f*\x0f*\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e+\x0e+\x0e+\x0e+\x0e+\x0e+\x0e\x0e\x0f*\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f*\x0f*\x0f*\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f*\x0f*\x0e+\x0f\x0e\x0f\r\x0f\x0e\x0e\x0e\x0f\x0e\x0f\r\x0f\x0e\x0e\x0e\x0e\x0f\x0f\r\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0e\x0f\x0e\x0e\x0f*\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0f\x0e\x0e\x0e\x0f*\x0e\x0f\r\x0f\x0e\x0f\x0e\x0e\x0f\x0e\r\x0f\x0e\x0f\x0e\x0e\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0f\x0e\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r,\r,\x0e+\r,\r,\x0e\x0e\x0e+\x0e\x00\r\x05'
'''

subirTemp = b'&\x00\xca\x00\x91\x8f\x134\x13\x10\x134\x124\x13\x11\x12\x11\x124\x13\x11\x12\x11\x133\x13\x11\x12\x11\x133\x134\x13\x10\x134\x133\x13\x11\x124\x134\x124\x134\x133\x134\x13\x10\x134\x12\x11\x13\x10\x13\x11\x12\x11\x13\x10\x13\x10\x13\x11\x12\x11\x13\x10\x134\x12\x11\x13\x10\x13\x11\x12\x11\x124\x134\x133\x13\x11\x124\x134\x133\x134\x13\xa9\x91\x90\x124\x13\x10\x134\x133\x13\x11\x12\x11\x134\x12\x11\x12\x11\x134\x12\x11\x13\x10\x134\x124\x13\x11\x124\x134\x12\x11\x124\x134\x134\x124\x134\x124\x13\x11\x124\x13\x10\x13\x11\x12\x11\x12\x11\x13\x10\x12\x12\x12\x11\x12\x11\x13\x11\x124\x12\x11\x13\x11\x12\x11\x11\x12\x125\x115\x125\x12\x11\x125\x115\x125\x115\x12\x00\r\x05'

'''b'&\x00\xbc\x01q9\x0e\x0f\r,\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e+\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r,\r,\r,\r\x0f\x0e\x0f\r,\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\r\x10\r\x0f\r\x10\r\x0f\r\x10\r\x0f\x0e\x0f\r\x0f\r\x10\r\x0f\r\x10\r+\x0e+\x0e\x0f\r\x10\r\x0f\x0e\x0f\r\x0f\r\x00\x01Ur9\x0f\x0e\r,\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e+\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r,\r,\r,\r\x0f\x0e\x0f\r,\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e+\x0e\x0f\r\x0f\x0e+\x0e+\x0e+\x0e\x0f\r\x0f\r\x10\r,\r\x0f\r\x10\r+\x0e+\x0e\x0f\r\x10\r\x0f\r\x10\r\x0f\r\x10\r\x0f\r\x10\r\x0f\r,\r,\r,\r,\r,\r,\r\x0f\x0e+\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e+\x0e+\x0e+\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r,\r,\r,\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\x0e\x0e\x0e\x0f\r\x0f\x0e\x0f\r,\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r,\r\x0f\x0e\x0f\r\x0f\r\x10\r\x0f\x0e\x0f\r\x0f\r\x10\r\x0f\r\x10\r\x0f\r\x10\r\x0f\x0e\x0f\r\x0f\x0e\x0f\r+\x0e+\x0e+\x0e+\x0e+\x0e+\x0e\x0f\r,\r\x00\r\x05'
'''

bajarTemp = b'&\x00\xca\x00\x91\x8f\x134\x12\x11\x124\x134\x13\x10\x13\x11\x124\x13\x10\x13\x11\x124\x13\x10\x13\x11\x124\x134\x12\x11\x134\x124\x13\x10\x134\x124\x134\x134\x124\x134\x12\x11\x124\x13\x11\x12\x11\x13\x10\x13\x11\x12\x11\x12\x11\x13\x10\x13\x11\x12\x11\x12\x11\x13\x10\x13\x11\x12\x11\x12\x11\x134\x124\x134\x124\x134\x133\x134\x134\x12\xaa\x91\x8f\x134\x12\x11\x134\x124\x13\x10\x13\x11\x124\x13\x11\x12\x11\x124\x13\x11\x12\x11\x124\x134\x13\x10\x134\x124\x13\x11\x124\x134\x124\x134\x124\x134\x13\x10\x134\x12\x11\x13\x10\x13\x11\x12\x11\x12\x11\x13\x10\x13\x11\x12\x11\x12\x11\x13\x10\x13\x11\x12\x11\x13\x10\x13\x11\x124\x134\x124\x134\x124\x134\x124\x134\x12\x00\r\x05'

'''b'&\x00\xbc\x01q9\x0e\x0e\x0f*\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0e\x0f\x0e\x0e\x0f\x0e\r,\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0e\x0f\x0e\x0e\x0f*\x0e+\x0f*\x0e\x0f\x0e\x0e\x0e+\x0e\x0f\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0e\x0f\x0e\x0e\x0f\x0e\r\x0f\x0e\x0f\x0e\x0e\x0f\x0e\r\x0f\x0f\x0e\x0e\x0e\x0e\x0f\x0e\x0e\x0f\x0e\x0e\x0e\x0e\x0f\x0e\x0e\x0f\x0e\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e+\x0e+\x0e\x0f\x0e\x0e\x0e\x0e\x0e\x0f\x0e\x0e\x0f\x00\x01Tr9\x0e\x0e\x0f*\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\r\x0f\x0f\x0e\x0e\x0e\x0f\x0e\r\x0f\x0f\x0e\x0e+\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\r\x0f\x0e\x0f\x0e\x0e\x0f*\x0e+\x0f*\x0f\x0e\x0e\x0e\x0f*\x0f\x0e\x0e\x0e\x0e\x0f\x0e\x0e\x0f\x0e\r\x0f\x0f\x0e\x0e\x0e\x0f\x0e\r\x0f\x0f\x0e\r\x0f\x0f\x0e\x0e+\x0e\x0e\x0f\x0e\x0e+\x0e+\x0e+\x0e\x0e\x0f\x0e\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e*\x0f*\x0f\x0e\x0f\x0e\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e+\x0e+\x0e+\x0e+\x0e+\r,\x0e\x0e\x0e+\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\r\x0f\x0f\x0e\x0e\x0e\x0e\x0f\r\x0f\x0f\x0e\x0e\x0e\x0f\x0e\r\x0f\x0f\x0e\r\x0f\x0f*\x0f*\x0f*\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e+\x0e+\x0e+\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\r\x0f\x0f\x0e\x0e\x0e\x0e\x0f\r\x0f\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0e\x0f\x0e+\r\x0f\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e+\r\x0f\x0f\x0e\r\x0f\x0f\x0e\x0e\x0e\x0e\x0f\r\x0f\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0f\x0e*\x0e\x0f\x0e+\x0e+\x0e+\x0e+\x0e\x0f\r,\x0e\x00\r\x05'
'''

def search(rm):
    dev = broadlink.discover() #se descubre la lista de dispositivos Broadlink en red local
    if len(dev)>0:
        for i in range(0,len(dev)):
            if macRM == dev[i].mac: #comparamos la mac de nuestro dispositivo
                rm.append(dev[i]) #redefinimos el divice final con el que se trabajará
                rm[1].auth()
                rm[1].set_name("CONTROL AC LST")
                print("Conectando a red...")
                time.sleep(2)
                print(rm[1].name,"conectado a: Lab. Telemática...", "IP:",rm[1].host[0])
                rm[0] = False
                return rm
            else:
                print("No se encontro su dispositivo","\nVerifique la conexión a la red local \"Lab. Telemática\"")
    else:
        print("Ningún dispositivo encontrado","\nVerificar que su Broadlink esté conectado a la red local \"Lab. Telemática\"")

#verificar estado de AC
def estadoAC(apagado, temp, tempReq,rm):
    if (temp != tempReq):
        if apagado:
            rm[1].send_data(on) #Encender AC
            return False
    else:
        if not apagado:
            rm[1].send_data(off) #Apagar AC
            return True
 
def variarTemp(temp, tempReq, rm):
    variarTemp = abs(temp-tempReq)
    #Control de temperatura
    if temp < tempReq: #se tiene que incrementar la temperatura tempReq-temp veces
        time.sleep(3)
        for i in range(variarTemp):
            rm[1].send_data(subirTemp)
            time.sleep(3)
        print("Se ha subido",variarTemp,"°C la temperatura")
    elif temp > tempReq:  #se tiene que disminuir la temperatura temp-tempReq veces
        time.sleep(3)
        for i in range(variarTemp):
            rm[1].send_data(bajarTemp)
            time.sleep(3)
        print("Se ha disminuido",variarTemp,"°C la temperatura")
    #else:
        #print("Temperatura de LST (IDEAL)")
        #rm[1].send_data(off) #Apagar AC
        #apagado=True
                
if __name__ == "__main__":
    tempReq=20 #Se obtiene por seteo de usuario (desde Interfaz)
    rm=[True] #[boolean de existencia de dispositivo, dispositivo]
    
    while rm[0]:
        rm=search(rm)
        
    apagado=True
    while True:
        #print(stateAPI)
        print("Estado inicial de AC:", apagado)
        temp=kaiterra.summarize_laser_egg("dd85475c-a5ef-4a15-b00f-206e408528b2") #obtener valor de temp <float>
        apagado = estadoAC(apagado, int(temp), int(tempReq),rm)
        print("Estado actual de AC:", apagado)
        variarTemp(int(temp), int(tempReq), rm)
        time.sleep(300)
