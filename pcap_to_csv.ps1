param ([Parameter(Mandatory)]$path_to_pcap, [Parameter(Mandatory)]$path_to_save)

Write-Output "`r`nThis script extracting traffic features from pcap files using tshark, it takes input pcaps and save to csv."
#Write-Output ".\pcap_to_csv.ps1 'path\to\pcap' 'path\to\csv'"


$time1 = Get-Date

Get-ChildItem $path_to_pcap  -recurse | Where-Object {$_.extension -in ".pcap",".pcapng"} |
    Foreach-Object {
        $pcapfile = $_.FullName
        $csvfile = $path_to_save +'\'+$_.BaseName+'.csv'
        #$csvfile = $_.DirectoryName+"\"+ $_.BaseName+".csv" #save to the same directory
        
        Write-Output "`r`nprocessing $pcapfile" 
        tshark.exe -r $pcapfile -T fields -E header=y -E separator=',' -E quote=d -E occurrence=f `
        -e eth.addr -e eth.src -e eth.dst -e eth.len `
        -e dns.qry.name -e dns.resp.name `
        -e ntp.request_in -e ntp.response_in `
        -e ip.id -e ip.proto -e ip.src -e ip.src_host -e ip.dst -e ip.dst_host -e ip.len -e ip.hdr_len -e ip.flags -e ip.flags.df -e ip.fragment.count -e ip.ttl `
        -e tcp.stream -e tcp.port -e tcp.dstport -e tcp.srcport -e tcp.window_size -e tcp.ack -e tcp.seq -e tcp.hdr_len -e tcp.len -e tcp.pdu.size -e tcp.payload `
        -e tcp.flags -e tcp.analysis.ack_rtt -e tcp.segments -e tcp.segment.count -e tcp.reassembled.length -e tcp.time_relative -e tcp.time_delta `
        -e http.request -e http.response -e http.content_type -e http.content_length `
        -e udp.stream -e udp.port -e udp.dstport -e udp.srcport -e udp.time_delta -e udp.time_relative -e udp.pdu.size -e udp.length -e udp.payload `
        -e frame.time_relative -e frame.time_delta -e frame.time | Out-File -filepath $csvfile -Encoding utf8
        Write-Output "saved to $csvfile"
    }

$time2 = Get-Date
$duration = $time2 - $time1
Write-Output $duration
Write-Output "done"