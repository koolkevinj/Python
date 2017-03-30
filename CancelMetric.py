import sys
import os
import subprocess

#
# get_cancel_metrics
# read the meterics from teh file
def read_cancel_metrics(infile_name):
    try:
        in_metric = False
        metric_cancel_cnt = 0

        with open(infile_name,'r') as infile_name:
            for l in infile:
                if in_metric == True:
                    if 'CANCEL:' in l:
                        metric_cancel_cnt += 1;   #A cancel for the current metric
                    elif metric_cancel_cnt > 0:
                        in_metric = False     #No more cancels. Save the metric and cancel count
                        #TODO: same metric and cancel count
                        metric_cancel_cnt = 0
                    else:
                        in_metric = False    #This was not a cancel metric
                else:
                    if '[METRIC]' in l:
                        # TODO: read the 2 metrics
                        in_metric = True

    except:
        ('main Exc:', sys.exc_info()[0], ', ', sys.exc_info()[1], ', ', sys.exc_info()[2])




try:
    argcnt = len(sys.argv)
    if argcnt < 1:
        print ("Usage arg is AQ log file")
        sys.exit()

    get_cancel_metrics(sys.argv[1])


except:
    ('main Exc:', sys.exc_info()[0], ', ', sys.exc_info()[1], ', ', sys.exc_info()[2])