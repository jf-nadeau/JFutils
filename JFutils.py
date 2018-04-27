import time
import os

###### Utilities #######
def progress_bar(initial_time, total_count, current_count):
    bar_size=10
    t=time.time()
    m=int((t-initial_time)/60)
    s=int((t-initial_time)%60)
    percent=int((current_count/total_count*100))
    if percent>100:
        return
    progress="{}/{} ({}%) | time: {}:{ss:02d}".format(current_count,total_count,percent,m,ss=s)
    print("...[{}>{}] {}".format("="*int(percent*bar_size/100)," "*(bar_size-int(percent*bar_size/100)),progress), end='\r')


###### Read files #######
def read_config(filename):
    configs={}
    if os.path.isfile(filename):
        with open(filename, 'r') as f:
            lines=f.readlines()
        for line in lines:
            if not line.startswith('#'):
                line=line.rstrip('\n').split('=')
                configs[line[0]]=line[1]
    return configs

def read_tsv(filename):
    if os.path.isfile(filename):
        return read_file(filename,'\t')
    else:
        print(filename, "does not exists")
def read_csv(filename):
    if os.path.isfile(filename):
        return read_file(filename,',')
    else:
        print(filename, "does not exists")

def read_file(filename, separator):
    with open(filename, 'r') as f:
        lines=[line.rstrip('\n').split(separator) for line in f]
    return lines


###### Write files #######
def write_tsv(item_list, filename):
    if type(filename) is list:
        return write_file(item_list, filename, '\t')
    else:
        print("input must be of type list")

def write_csv(item_list, filename):
    if type(filename) is list:
        return write_file(item_list, filename, ',')
    else:
        print("input must be of type list")

def write_file(item_list, filename, separator):
    if item_list:
        with open(filename, 'w') as f:
            f.writelines(separator.join(i) + '\n' for i in item_list)
    else:
        print("The list is empty")