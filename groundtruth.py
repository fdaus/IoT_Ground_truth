import pyshark
# import asyncio
# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# asyncio.run(main())
stream = pyshark.FileCapture("16-09-25.pcap")
#print (stream[0])
print(dir(stream))
def get_features(packet):
    header_f = {'src_ip' : str(packet.ip.src), 
        'dst_ip' : str(packet.ip.dst),  
        'frozen' : frozenset((str(packet.ip.src), str(packet.ip.dst))),
        'payload' : int(packet.tcp.len)}
    
    process_row(header_f, 'capture')