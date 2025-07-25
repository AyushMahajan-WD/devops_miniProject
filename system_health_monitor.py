import  psutil,os, datetime,platform, argparse


def cpu_usage():
    try:
          print(f"CPU Usage : {psutil.cpu_percent()}%")
    except Exception as e:
        print(f"Error occured {e}")

def memory_usage():
    try:
        print(f"Memory usage : {psutil.virtual_memory().percent}%")
    except Exception as e:
        print(f"Error occured {e}")

def disk_info():
    try:
        print(f"Disk info : {psutil.disk_usage(os.path.abspath(os.sep)).percent}%")
    except Exception as e:
        print(f"Error occured {e}")

def process_info():
    try:
        for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent','memory_percent']):
            print(f"The running processes are : {proc.info}")
    except Exception as e:
        print(f"Error occured {e}")

def uptime_load_avg():

    try:
        if('windows' in platform.system().lower()):
            boot_time= datetime.datetime.fromtimestamp(psutil.boot_time())
            print(datetime.datetime.now() - boot_time)
        else:
            print(f"Uptime is : {datetime.datetime.fromtimestamp(psutil.boot_time())} ")
            print(f"Load average is : {psutil.getloadavg()}")    
    except Exception as e:
        print(f"Error occured {e}")

def show_help():
    
        print(''' Put below command 
        --> cpu
        --> memory
        --> disk
        --> process
        --> uptime_load
        ''')

def main():
    parser = argparse.ArgumentParser(description="System Health Monitor")
    parser.add_argument("command", help="command to run",choices=['cpu','memory','disk','process','uptime_load'])
    args = parser.parse_args()
    cli_input = args.command
    
    if(cli_input == 'cpu'):
        cpu_usage()
    elif(cli_input == 'memory'):
        memory_usage()  
    elif(cli_input == 'disk'):
        disk_info()
    elif(cli_input == 'process'):
        process_info()
    elif(cli_input == 'uptime_load'):
        uptime_load_avg()
