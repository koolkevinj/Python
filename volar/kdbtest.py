import qpython
import os
import pandas as pd
from qpython import qconnection

def get_kdb_data():
    q = qconnection.QConnection(host='kdb.genevatrading.com', port=9898, pandas=True)    
    q.open()  # initialize connection    
   # print('IPC version: %s. Is connected: %s' % (q.protocol_version, q.is_connected()))

    # simple query execution via: QConnection.sendSync
    data = q.sendSync('select time,ISIN,bidprice0,askprice0,bidsize0,asksize0 from bookZNOPT_hist where date=2020.04.30, time within 11:00:00.000 12:01:00.000, year=2020, month in (6,7)')
    q.close()      # close connection
    return data

    
def get_csv_data():
    d = pd.read_csv('python/volar/samplemd.csv')
    d['time'] = pd.to_datetime(d['time'], format='%Y.%m.%dD%H:%M:%S.%f')
    d = d.set_index('time')
    return d

def do_grp_at_time_f(grp, tm):
    #Receives pandas group and timestamp string
    r = grp.asof(pd.DatetimeIndex([tm]))    
    #Set ISIN and other valuesto 0 if no record exists "as of" the time idx
    r['ISIN'] = r['ISIN'].fillna(grp['ISIN'][0])  
    r = r.fillna(0)     
    
    r.to_csv(of, header=False, line_terminator='\n')

if __name__ == '__main__':
    # create connection object
    of = open('python/Volar/outfile.csv','w')
    data = get_csv_data()
    groups = data.groupby(['ISIN'])
    time_ints = pd.date_range(start ='2020-04-30 12:00:00.000', 
                            end ='2020-04-30 12:01:00.000',
                            freq ='10S')
    pd.DataFrame(columns=data.columns).to_csv(of, line_terminator='\n', index=False) #print header
    do_a_grp = lambda t : groups.apply(lambda grp : do_grp_at_time_f(grp,tm=t))
    time_ints.to_series().apply(do_a_grp)


