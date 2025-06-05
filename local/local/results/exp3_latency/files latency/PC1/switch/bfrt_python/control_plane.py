import threading
import subprocess
import os
import time


p4 = bfrt.Per_Flow_Collector.pipe
os.system("rm /home/P4-perfSONAR-clean/processing\ delays/Sergio_OVS_HW*")
# file = open("/home/P4-perfSONAR-clean/bfrt_python/ucli_temp_cmds","w")
# file.write("ucli\n")
# # file.write("pm port-add 1/- 40G NONE\n")
# file.write("pm show\n")
# file.write("exit\nexit\n\n")
# file.close()

command_init = ['cd /root/bf-sde-9.6.0/ ; ./run_bfshell.sh --no-status-srv -f /home/P4-perfSONAR-clean/ucli_cmds'] 

def del_ports(port_list, file):
    for port_number in port_list:
        cmd = "pm port-del "+str(port_number)+"/- \n" 
        file.write(cmd)

def add_ports(port_list, file):
    for port_number in port_list:
        cmd = "pm port-add "+ str(port_number) + "/- 40G NONE \n"
        file.write(cmd)

def enb_ports(port_list, file):
    for port_number in port_list:
        cmd = "pm port-enb "+ str(port_number) + "/- \n"
        file.write(cmd)


def get_port_lsit(output):
    port_list = []
    lines = output.strip().split('\n')
    for line in lines:
        items = line.strip().split()
        if(len(items) > 3):
            try:
                if(int(items[0][0]) == 1):
                    status = items[3].strip().split("|")
                    if ("DWN" in status):
                        port_number = int(items[0][0])
                        port_list.append(port_number)
                else:
                    status = items[2].strip().split("|")
                    if ("DWN" in status):
                        port_number = int(items[0][0])
                        port_list.append(port_number)
            except Exception as e:
                pass
    return port_list

def check_ports(file):
    file.truncate(0)
    file.write("ucli\n")
    file.write("pm show\n")
    file.write("exit\nexit\n\n")


try:
    process = subprocess.Popen(command_init, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True,shell=True)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print("Command failed with exit code",process.returncode)

except Exception as e:
    print('An error occurred:', e)

time.sleep(10)

all_ports_up = False

command_check_ports = ['cd /root/bf-sde-9.6.0/ ; ./run_bfshell.sh --no-status-srv -f /home/P4-perfSONAR-clean/bfrt_python/ucli_check_ports']
command_update_config = ['cd /root/bf-sde-9.6.0/ ; ./run_bfshell.sh --no-status-srv -f /home/P4-perfSONAR-clean/bfrt_python/ucli_temp_cmds']

while (not all_ports_up):
    try:
        process = subprocess.Popen(command_check_ports, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True,shell=True)
        stdout, stderr = process.communicate()
        port_list = get_port_lsit(stdout)
        if(len(port_list)==0):
            all_ports_up = True
            print("All ports are up")
        else:
            print("Re-enabling ports: ",port_list)
            file = open("/home/P4-perfSONAR-clean/bfrt_python/ucli_temp_cmds","w")
            file.write("ucli\n")
            
            del_ports(port_list,file)
            add_ports(port_list,file)
            enb_ports(port_list,file)

            file.write("pm show \n")
            file.write("exit\nexit\n\n")
            file.close()
            process = subprocess.Popen(command_update_config, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True,shell=True)
            stdout, stderr = process.communicate()
            time.sleep(10)
        if process.returncode != 0:
            print("Command failed with exit code",process.returncode)
        

    except Exception as e:
        print('An error occurred:', e)
    
    


def queue_delay_thread():

    import time
    from datetime import datetime
    global p4
    import math
    file_path = "/home/P4-perfSONAR-clean/processing delays/Sandia"
    counter=0
    extention = ".txt"
    file_name = file_path+"_"+str(counter)+extention
    f = open(file_name,"w")
 
    metric_name = "queue_occupancy"
    prev_queue_delay = 0
    data = []
    last_update_time = datetime.now().timestamp()
    statistic_printed = False

    def calculate_percentile(data, percentile):
        data_sorted = sorted(data)
        index = (percentile / 100.0) * (len(data_sorted) - 1)
        lower = int(math.floor(index))
        upper = int(math.ceil(index))
        if lower == upper:
            return data_sorted[int(index)]
        else:
            return data_sorted[lower] * (upper - index) + data_sorted[upper] * (index - lower)
    
    while (1):
        try:
            queue_delay = p4.Egress.queue_delays.get(REGISTER_INDEX=0, from_hw=True, print_ents=False).data[b'Egress.queue_delays.f1'][1]
            metric_value = queue_delay
            queue_delay *= 4
            if(queue_delay > 0 and queue_delay != prev_queue_delay):
                last_update_time = datetime.now().timestamp()
                # print("Processing Time is: ", queue_delay, " microseconds")
                data.append(queue_delay)
                statistic_printed = False
                prev_queue_delay = queue_delay
                f.write(str(queue_delay)+"\n")
            # time.sleep(0.005)
            if((len(data) > 1)  and (datetime.now().timestamp() - last_update_time > 2) and not statistic_printed):
                mean = sum(data) / float(len(data))
                mean = mean / 1000
                std = sum((x - mean) ** 2 for x in data) / float(len(data) - 1)
                std = math.sqrt(std)
                std = std / 1000
                mean = str(mean)[:4]
                std= str(std)[:4]
                _99percentile = calculate_percentile(data,99.9)
                print("\n number of measurements: ",len(data),"mean:",mean," us, std: ",std," us "," _99percentile ",_99percentile)
                statistic_printed = True
                data = []
                f.close()
                counter+=1
                file_name = file_path+"_"+str(counter)+extention
                f = open(file_name,"w")

        except KeyError:
            pass
        except Exception as e:
            print("An error occurred in queue_delay_thread :", str(e))
            break
    f.close()
    return 0

# queue_delay_thread()

th_queue_delay_thread = threading.Thread(target=queue_delay_thread, name="queue_delay_thread")

th_queue_delay_thread.start()
