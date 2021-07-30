import pyshark
import time
start_time = time.time()


pcap_file="16-09-25.pcap"
record = pyshark.FileCapture(pcap_file,display_filter="tcp")
list_of_eth =[]
for pkt in record:
    #pkt = record
    if "tcp" in pkt:
        #print(pkt.eth.addr)
        list_of_eth.append(pkt.eth.addr)
#        list_of_eth.append(pkt.ip.dst)

record.close()

unique_eth = list(set(list_of_eth))
#print(list_of_eth)
print(unique_eth)

print("--- %s seconds ---" % (time.time() - start_time))
#pkt.pretty_print()


