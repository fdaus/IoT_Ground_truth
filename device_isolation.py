#!/usr/bin/env python
'''

    Iot device isolation
    Author: firdaus <fdaus.isa@gmail.com>

    This program is an implementation of groundtruth https://github.com/fdaus/IoT_Ground_truth
    
    Device isolated, it takes input pcaps and group each packets according to its mac address.

Usage: device_isolation.py <inputdir> <outputdir>

Example:python device_isolation.py data pcap-isolated
python device_isolation.py | Out-File -filepath isolation_log.txt
'''
#device_isolation.py -d <inputdir> [or] -i <inputpcap> -l <label> [and] -o <outputdir>

import pandas as pd
import os
import time


DUMP="data_portion"
ISOLATED="pcap-isolated"
DEVICE="unsw_devicelist.csv"
TSHARK="tshark"
FILENUMBER=1

def ret_pcaps():
    files = os.listdir(DUMP)
    pcap_files = []
    for file in files:
        if '.pcap' in file or '.pcapng' in file:
            pcap_files.append(DUMP+'/'+file)
    return pcap_files

def create_outputdir(outputdir,device_label):

    dirpath=outputdir+'/'+device_label
    if not os.path.isdir(dirpath):
        os.makedirs(dirpath)

def get_time():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return current_time

def main():
    allpcaps = ret_pcaps()
    print(len(allpcaps)," pcap files")

    device = pd.read_csv(DEVICE)
    j=FILENUMBER
    for pcap_file in allpcaps:
        i=0
        
        print("Examining pcap file ",j)
        print("start time ",get_time())
        while i < device.shape[0]:
            
            print("\nfrom {}".format(pcap_file))
            print("\nIsolating address "+device.iloc[i,1]+" for device "+device.iloc[i,0])
            
            create_outputdir(ISOLATED,device.iloc[i,0])

            cmd ='tshark -r {} -Y "eth.addr eq {}" -w "{}/{}/{}.pcap"'.format(pcap_file,device.iloc[i,1],ISOLATED, device.iloc[i,0],j )
            
            os.system(cmd)
            
            print("\nComplete: {}".format(device.iloc[i,0]))
            i+= 1
        
        j+=1
        print("End time",get_time())
        print("\n#############################################################")
        
    print("siap")

start = time.time()
main()
end = time.time()
print("\nProgram execution time is :", end-start)