# wget https://github.com/layou233/NeverIdle/releases/download/0.1/NeverIdle-linux-arm64 -O NeverIdle

# CPU (4 Cores for 5 Seconds)
    # stress-ng --cpu <number_of_cpu_cores> --timeout <duration_in_seconds>
    # stress-ng --cpu 1 --timeout 60

# Memory (3GB)
    # stress-ng --vm <number_of_processes> --vm-bytes <memory_size_in_bytes>
    # stress-ng --vm 3 --vm-bytes 1G

# Network
    # speedtest-cli --list
    # speedtest-cli --server <server_id>

# for OCI(4CPU 24GB) we need to: 
    # Run CPU at more than 10%, for 5% of the time (run every 15min for 1min at 10%)
    # Keep memory utilization at 10% (~3GB)
    # Keep network utilization at 10% (run every 10min)

import os
import time    
import datetime
import threading

def memoryAndNetwork():
    os.system('chmod 777 NeverIdle')
    os.system('./NeverIdle -m 3 -n 0h10m0s')

# def memory():
#     os.system('stress-ng --vm 3 --vm-bytes 1G')
    
# def network():
#     nextRunEpoch = 0
#     while True:
#         epoch_time = int(time.time())
        
#         if epoch_time > nextRunEpoch:
#             dt = datetime.datetime.fromtimestamp(epoch_time)
#             new_dt = dt + datetime.timedelta(minutes=10)
#             new_epoch_time = int(new_dt.timestamp())

#             nextRunEpoch = new_epoch_time
            
#             i = 10
#             o = 0
#             while o < i:
#                 os.system('speedtest-cli --server 50463')
#                 o += 1

def cpu():
    nextRunEpoch = 0
    while True:
        epoch_time = int(time.time())
        
        if epoch_time > nextRunEpoch:
            dt = datetime.datetime.fromtimestamp(epoch_time)
            new_dt = dt + datetime.timedelta(minutes=15)
            new_epoch_time = int(new_dt.timestamp())

            nextRunEpoch = new_epoch_time
            
            # os.system('stress-ng --cpu 1 --timeout 60')
            os.system('stress-ng --cpu 1 --cpu-load 20 --timeout 60')


if __name__ =="__main__":
    thread1 = threading.Thread(target=cpu)
    # thread2 = threading.Thread(target=network)
    # thread3 = threading.Thread(target=memory)
    thread4 = threading.Thread(target=memoryAndNetwork)
    
    thread1.start()
    # thread2.start()
    # thread3.start()
    thread4.start()
    

# os.system('stress-ng --cpu 1 --timeout 60')

# os.system('stress-ng --vm 3 --vm-bytes 1G')

# os.system('speedtest-cli --list')
# os.system('speedtest-cli --server <server_id>')
