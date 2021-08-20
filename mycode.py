#!/usr/bin/env python
'''

    Iot device isolation
    Author: firdaus <fdaus.isa@gmail.com>

    This program is an implementation of groundtruth https://github.com/fdaus/IoT_Ground_truth
    
    Device isolated, it takes input pcaps and split each packets according to its mac address.

Usage: device_isolation.py <inputdir> <outputdir>

Example:python device_isolation.py data pcap-isolated
'''
#device_isolation.py -d <inputdir> [or] -i <inputpcap> -l <label> [and] -o <outputdir>
import subprocess

import os

#files = os.listdir("data")

#cmd="echo {}".format(files)
#subprocess.run(cmd)
#os.system(cmd)

exit_code = subprocess.call('tshark.sh',shell=True, input="2")
print("done")