import os
import subprocess
import shutil

my_path = input("Enter directory path")
path = my_path.strip()
os.chdir(path)
try:
    os.chmod(f'{path}',0o777)
except:
    pass
os.mkdir('logs', exist_ok = True)
manual_path = os.path.join(path, 'logs' )
def identify_logs(activity = 'copy'):
    dir_list = os.listdir(path)
    for item in dir_list:
        if( item.endswith(".log") and item != 'logs' ):
            if activity == 'copy':  
                with open(item,'r') as log_file:
                    for line in log_file:
                        if "ERROR" in line:
                            shutil.copy(item,manual_path)
                            break
            elif activity == 'delete':
                with open(item,'r') as log_file:
                    for line in log_file:
                        if "ERROR" in line:
                            os.remove(f'{item}')
                            break
                             
identify_logs() 
            
shutil.make_archive('compressed_log', 'zip', manual_path)

identify_logs('delete')