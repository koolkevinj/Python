import sys
import os
import subprocess

def read_metrics(l, metrics_tup):
    #Ex:
    #  10:36:13.453805|1776277248|IN|[METRIC] Event type FEED mark in 4024 ns, from orig 16412 ns

    evt = l[find("Event") : ]
    metrics_tup[0] = evt[5]
    metrics_tup[1] = evt[9]

#
# get_cancel_metrics
# read the meterics from the file
#
def read_cancel_metrics(infile_name, ret_list):
    try:
        in_metric = False
        metrics = (0,0,0)

        with open(infile_name,'r') as infile:
            for l in infile:
                if in_metric == True:
                    if 'CANCEL:' in l:
                        metrics[2] += 1;   #A cancel for the current metric
                    elif metrics[2] > 0:
                        in_metric = False     #No more cancels. Save the metric and cancel count
                        ret_list.insert(metrics)
                        metrics[2] = 0
                    else:
                        in_metric = False    #This was not a cancel metric
                else:
                    if '[METRIC]' in l:
                        read_metrics(l, metrics)
                        print ("m1="+metrics[0]+" m2="+metrics[1])
                        in_metric = True

    except:
        ('main Exc:', sys.exc_info()[0], ', ', sys.exc_info()[1], ', ', sys.exc_info()[2])


try:
    argcnt = len(sys.argv)
    if argcnt < 2:
        print ("Usage arg is AQ log file")
        sys.exit()

    metric_list = []
    read_cancel_metrics(sys.argv[1], metric_list)


except:
    ('main Exc:', sys.exc_info()[0], ', ', sys.exc_info()[1], ', ', sys.exc_info()[2])