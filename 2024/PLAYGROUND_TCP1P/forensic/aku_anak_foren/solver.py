from scapy.all import *


def filter_http(pcap):
    packets = rdpcap(pcap)
    http_pac = [pkt for pkt in packets if pkt.haslayer('TCP')]
    return http_pac

if __name__ == "__main__":
    file_pcap = 'capture.pcap'
    flag = ''
    real_flag = ''
    file_pcap = filter_http(file_pcap)
    for i in file_pcap:
        if i.haslayer(TCP) and i.haslayer(Raw):
            load = i[Raw].load.decode(errors='ignore')
            if 'POST' in load and 'HTTP/1.1' in load:
                flag += load
    
    for i in flag.split('\n'):
        if ('Method Not Allowed' in i  and 'title' not in i) or (len(i)==17 and 'POST' in i):
            real_flag += i[0].replace('\r', '')
    print(f"here flag : {real_flag[0:-1]}")
