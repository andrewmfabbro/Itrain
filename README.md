# Itrain
A High intensity interval training web application meant to record exercise timing data in spreadsheets and a graphical dashboard.

###
REQUIRES AN AMAZON DASH BUTTON
###
python packages

import time
import sys
import requests
import xlwt
from scapy.all import *
from scapy.layers.l2 import ARP

###Notes###
Scapy is used to obtain the mac address of the dash button on a local wifi network.

##
In order for spreads to function use of the cloudstitch api magic form is required like in the line below.
I intend to find a way to do this with excel and google docs eventually.

MAGIC_FORM_URL = 'https://api.cloudstitch.com/afab/itrain-spreadsheet/datasources/sheet'
##
