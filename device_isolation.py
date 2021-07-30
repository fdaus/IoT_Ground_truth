from csv import DictReader
import os
DUMP="./pcap-originals"
ISOLATED="./pcap-isolated"
TSHARK="tshark"
def ret_pcaps():
    files = os.listdir(DUMP)
    pcap_files = []
    for file in files:
        if '.pcap' in file:
            pcap_files.append(DUMP+'/'+file)
    return pcap_files

#allpcaps = ret_pcaps()
#cmd = "mergecap -w merged.pcap /mnt/e/OneDrive/1-Documents/1-PhD/2-Experiment/Ground_truth/*.pcap"
#os.system(cmd)
""" for device in devices:
    if "address" in devices[device]:
         print("Isolating address {} for device {}".format(devices[device]["address"], device))
        cmd = "tcpdump -r merged.pcap -s0 -w {}/{}.pcap 'ether host {}'".format(ISOLATED, device, devices[device]["ether"])
        print(cmd)
        os.system(cmd) """
with open('non-iot_device.csv', 'r') as read_obj:
    csv_dict_reader = DictReader(read_obj,fieldnames=...)
    for device in csv_dict_reader:
    
      
        print("Isolating address {} for device {}".format(device["eth_addr"], device['Devices']))
 
        cmd = "tcpdump -r merged.pcap -s0 -w {}/{}.pcap 'ether host {}'".format(ISOLATED, device, device['eth_addr'])
        print(cmd)
        #os.system(cmd)
        print("here 3 eth:{}",device)
    print("here 4")
# tcpdump -r non-iot.pcapng -s0 -w "./pcap-isolated/device_A.pcap" 'ether host 34:97:f6:59:1c:f9' # tcpdump -r non-iot.pcapng -s0 -w "./pcap-isolated/device_B.pcap" 'ether host d4:5e:ec:6f:76:6c'

# split unidirectional flow
#SplitCap.exe -r device_A.pcap -s flow -o .\pcap-isolated\

#split mac address
# SplitCap.exe -r 16-09-25.pcap -s mac -o .\pcap-mac_addr\