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
    d = pd.read_csv('C:\\Kevin\\src\\Python\\samplemd.csv')
    d['time'] = pd.to_datetime(d['time'], format='%Y.%m.%dD%H:%M:%S.%f')
    d = d.set_index('time')
    return d


if __name__ == '__main__':
    # create connection object
    
    data = get_csv_data()
    #print(data.head(10))
    #print(data.dtypes)
    
    grouped = data.groupby('ISIN')
    print (grouped.head(10))
    #tensec_freq = data.asfreq('10S')
    #print (tensec_freq.head(100))
   

