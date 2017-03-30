import sys
import os
import subprocess

def read_metrics(l):
    #Ex:
    #  10:36:13.453805|17       76277248|IN|[METRIC] Event type FEED mark in 4024 ns, from orig 16412 ns

    evt = l[l.find("Event") : ].split()
    return {int(evt[5]), int(evt[9])}

#
# get_cancel_metrics
# read the meterics from the file
#
def read_cancel_metrics(infile_name, mi_list, fo_list, cnt_list):
    try:
        in_metric = False
        metrics=()
        cnt=0

        with open(infile_name,'r') as infile:
            for l in infile:
                if in_metric:
                    if 'CANCEL:' in l:
                        cnt += 1;   #A cancel for the current metric
                    elif cnt > 0:
                        in_metric = False     #No more cancels. Save the metric and cancel count
                        mi_list.append(metrics[0])
                        fo_list.append(metrics[1])
                        cnt_list.append(cnt)
                        cnt=0;
                    else:
                        in_metric = False    #This was not a cancel metric
                else:
                    if '[METRIC]' in l:
                        metrics = read_metrics(l)
                        if(metrics[0]>0 and metrics[1]>0):
                            in_metric = True

    except:
        ('main Exc:', sys.exc_info()[0], ', ', sys.exc_info()[1], ', ', sys.exc_info()[2])
        print ("exc2=")


try:
    argcnt = len(sys.argv)
    if argcnt < 2:
        print ("Usage arg is AQ log file")
        sys.exit()

    tool_list=[]
    orig_list=[]
    cnt_list=[]
    read_cancel_metrics(sys.argv[1], tool_list, orig_list, cnt_list)
    #for m in metric_list:
        #print m


except:
    ('main Exc:', sys.exc_info()[0], ', ', sys.exc_info()[1], ', ', sys.exc_info()[2])
    print ("exc=1")
