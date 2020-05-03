import qpython
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

def my_asof(gd):
    return gd.asof(pd.DatetimeIndex(['2020-04-30 12:00:019.100']))


if __name__ == '__main__':
    # create connection object
    
    data = get_csv_data()
    gb = data.groupby(['ISIN'])
    time_ints = pd.date_range(start ='2020-04-30 12:00:00.000', 
                            end ='2020-04-30 12:01:00.000',
                            freq ='10S')
    result = gb.apply(my_asof)
    print(result)

