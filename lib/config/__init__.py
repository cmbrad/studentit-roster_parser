import os
import logging
	
from lib.parser.helper.cell import Cell

####################
# General Settings #
####################
SIT_HOME = os.path.join(os.path.expanduser('~'), '.sit')
LOG_DIR = os.path.join(SIT_HOME, 'logs')

##########################
# People database config #
##########################


#######################
# XLS Parser Settings $
#######################


########################
# XLSX Parser Settings $
########################
PEOPLE_START_CELL = Cell('C6')
PEOPLE_END_CELL = Cell('XFD6')

TIMES_START_CELL = Cell('A7')
TIMES_END_CELL = Cell('A1000')

SHIFT_ROW_LIMIT = 1000

#####################################
# Google Calendar Uploader Settings $
#####################################

