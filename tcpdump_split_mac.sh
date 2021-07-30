 #!/bin/bash

 #Name of PCAP file to analyse
 pcap_file="tcpdump_2019-06-21_213044.pcap"

 #MAC address to filter 
 mac="00:17:88:48:89:21"

 mkdir /2019-06-21/

 for steam in $pcap_file;
 do
 /usr/bin/tshark -r $pcap_file  -Y "eth.addr eq 00:17:88:48:89:21" -w $mac.pcap    
 done


 #!/bin/bash

  pcap_file=(tcpdump_2019-07-01_000001.pcap tcpdump_2019-06-26_120301.pcap)

  macs=(  00:17:88:71:78:72 )

  devices=(phillips_1 phillips_2)

  for pcf in ${pcap_file[*]}
  do
    echo "$pcap_file" >&2
         /usr/bin/tshark -r "$pcf" -Y "eth.addr eq $macs" -w "$devices.pcap"        
  done
#!/bin/bash

# usage "$0" pcap_file1 pcap_file2 ...

#macs=(  00:17:88:48:89:21  00:17:88:48:89:22  00:17:88:48:89:23 )
ips=( 192.168.202.68 192.168.202.79 192.168.229.153 192.168.23.253 )

for pcf in "$@"
do
    dir="`basename "$pcf" | sed -r 's/(tcpdump_)(.*)(_[0-6]{6}.pcap)/\2/'`"
    mkdir "$dir"
    cd "$dir" || exit  # into the newly created child dir
    pcf="`realpath -e "$pcf"`"  # make sure the file can be found from the new directory

    #for mac in ${macs[*]}
    for ip in ${ips[*]}
    do
        #echo "$mac" >&2
        echo "$ip" >&2
        #/usr/bin/tshark -r "$pcf" -Y "eth.addr eq $mac" -w "$mac.pcap"
        /usr/bin/tshark -r "$pcf" -Y "ip.addr == $ip" -w "$ip.pcap"
    done

    cd ..  # back to the parent dir
done

#eth.addr == d4:5e:ec:6f:76:6c