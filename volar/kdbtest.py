import qpython
import os
import pandas as pd
from qpython import qconnection

def getkdb_data():
    q = qconnection.QConnection(host='kdb.genevatrading.com', port=9898, pandas=True)    
    q.open()  # initialize connection    
   # print('IPC version: %s. Is connected: %s' % (q.protocol_version, q.is_connected()))

    # simple query execution via: QConnection.sendSync
    data = q.sendSync('select distinct isins:distinct ISIN from bookZNOPT_hist where date=2020.04.30, year=2020, month in (6,7)')
    q.close()      # close connection
    return data

    
def get_csv_data():
    d = pd.read_csv('volar/samplemd.csv')
    d['time'] = pd.to_datetime(d['time'], format='%Y.%m.%dD%H:%M:%S.%f')
    d = d.set_index('time')
    return d

def do_grp_at_time_f(grp, tm):
    r = grp.asof(tm)
    r.to_csv(of, index=False, header=False)

if __name__ == '__main__':
    # create connection object
    of = open('volar/outfile.csv','w')
    data = get_csv_data()
    groups = data.groupby(['ISIN'])
    time_ints = pd.date_range(start ='2020-04-30 12:00:00.100', 
                            end ='2020-04-30 12:01:00.000',
                            freq ='20S')
    #at_time = lambda x,y : x.asof(pd.DatetimeIndex(['2020-04-30 12:00:019.100']))
    hdrs=pd.DataFrame(columns=data.columns).to_csv(of)
    do_grp_at_time = lambda grp,tm : grp.asof(pd.DatetimeIndex([tm])).to_csv(of, header=False)
    do_a_grp = lambda t : groups.apply(lambda grp : do_grp_at_time(grp,tm=t))
    time_ints.to_series().apply(do_a_grp)
    #do_a_grp(pd.DatetimeIndex(['2020-04-30 12:00:30.000']))
    #do_a_grp(time_ints.to_series())
    #print(result)


