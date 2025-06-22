#TRAIN RL AGENT TO NAVIGATE TO CROSS THE ROAD WITH ACTION RIGHT, LEFT, RIGHT

import numpy as np
import random

#ENVIRONMENT setup
road_length = 5  #the rad will have 5 position from position 0 to position 4
actions = ['left', 'right']

#Q_table intialization