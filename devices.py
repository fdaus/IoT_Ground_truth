import pandas as pd
from csv import DictReader
""" devices = pd.DataFrame ({
    "name" : ["Mibox"],
    "eth_addr" : ['d4:5e:ec:6f:76:6c']
})   """ 

devices = pd.DataFrame(columns=['Devices','eth_addr','Connection','Category'])

def add_devices(device_name, mac_addr, conn, category):
    newdev = pd.DataFrame({'Devices':[device_name],'eth_addr':[mac_addr],'Connection':[conn],'Category':[category]})
        
    return devices.append(newdev,ignore_index = True)

#dev_list = add_devices('Mibox','d4:5e:ec:6f:76:6c','wireless','iot')


with open('non-iot_device.csv', 'r') as read_obj:
    csv_dict_reader = DictReader(read_obj)
    for row in csv_dict_reader:
        print(row['Devices'], row['eth_addr'])