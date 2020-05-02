import qpython
import pandas
from qpython import qconnection


if __name__ == '__main__':
    # create connection object
    q = qconnection.QConnection(host='kdb.genevatrading.com', port=9898, pandas=True)
    # initialize connection
    q.open()

#/ print(q)
   # print('IPC version: %s. Is connected: %s' % (q.protocol_version, q.is_connected()))

    # simple query execution via: QConnection.sendSync
    data = q.sendSync('select distinct symbol,month from bookZNFUT_hist where date=2020.04.30')
    #print('type: %s, numpy.dtype: %s, meta.qtype: %s' % (type(data), data.dtype, data.meta.qtype))
    print('type: %s coltypes: %s' % (type(data), data.dtypes ))
    #print(data.shape)
    print (data)
    print(data.iloc[0,0])
    print (str(data.iloc[0,0]))
   

    # close connection
    q.close()