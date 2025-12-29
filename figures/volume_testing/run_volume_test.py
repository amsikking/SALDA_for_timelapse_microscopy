# Imports from the python standard library:
import csv
import time
from datetime import datetime

# Third party imports, installable via pip:
import numpy as np

# Our code, one .py file per module, copy files to your local directory:
import kds_legato110 # github.com/amsikking/kds_legato110
import ohaus_EX225DAD # github.com/amsikking/ohaus_EX225DAD

# Initialize devices:
balance = ohaus_EX225DAD.Controller(
    which_port='COM9', verbose=True, very_verbose=False)
sy_pump = kds_legato110.Controller(
    which_port='COM10', verbose=True, very_verbose=False)

# Configure syringe:
syringe_volume_ul = 2500
dispensed_volume_ul = 0

# Configure syringe pump:
flow_rate_ulps = 110 # max ~110 ul/sec for 2.5ml glass syringe (6.62764 ml/min)
sy_pump.set_flow_rate('withdraw', 'max', None)
sy_pump.set_flow_rate('infuse', flow_rate_ulps, 'ul/sec')
sy_pump.set_run_direction('infuse')

# Configure:
target_volume_ul = 10   # 10-100 typical
random_volumes = False
random_volume_range = (10, 100)
iterations = 100 # how many iterations?
shots_on_target = 1 # how many shots are needed for high trueness? prefer 1

# Get unique filename and start weight:
dt = datetime.strftime(datetime.now(),'%Y-%m-%d_%H-%M-%S')
filename = dt + '_volume_vs_weight.csv'
previous_weight_mg = float(balance.get_immediate_weight()[0])
for i in range(iterations):
    print('\niteration = %i (dispensed_volume_ul=%s)'%(i, dispensed_volume_ul))
    if random_volumes: # change target volume if random:
        target_volume_ul = np.random.randint(low=random_volume_range[0],
                                             high=random_volume_range[1])
    # update total dispsensed volume and exit if syringe is empty:
    dispensed_volume_ul += target_volume_ul * shots_on_target
    if dispensed_volume_ul >= syringe_volume_ul:
        break
    sy_pump.set_target_volume(target_volume_ul, 'ul')
    # get data:
    for shot in range(shots_on_target):
        print('\nshot = %i'%shot)
        sy_pump.set_run_direction('infuse')# forces volume update? device error?
        sy_pump.run()
        time.sleep(5) # wait for fluidics and balance to stablize
        immediate_weight_mg = float(balance.get_immediate_weight()[0])
        net_weight_mg = round(immediate_weight_mg - previous_weight_mg, 2)
        previous_weight_mg = immediate_weight_mg
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            if i == 0 and shot == 0:
                writer.writerow([ # write headers
                    'shot','flow_rate_ulps','target_volume_ul','net_weight_mg'])
            writer.writerow([ # write data:
                shot, flow_rate_ulps, target_volume_ul, net_weight_mg])

balance.close()
sy_pump.close()
