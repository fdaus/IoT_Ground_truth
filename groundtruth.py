import pyshark

stream = pyshark.FileCapture("16-09-25.pcap")
print(stream[0])