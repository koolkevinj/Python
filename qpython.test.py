import qpython
from qpython import qconnection


if __name__ == '__main__':
    # create connection object
    q = qconnection.QConnection(host='kdb.genevatrading.com', port=9898)
    # initialize connection
    q.open()

    print(q)
    print('IPC version: %s. Is connected: %s' % (q.protocol_version, q.is_connected()))

    # simple query execution via: QConnection.__call__
   #data = q('{`int$ til x}', 10)
    #print('type: %s, numpy.dtype: %s, meta.qtype: %s, data: %s ' % (type(data), data.dtype, data.meta.qtype, data))

    # simple query execution via: QConnection.sendSync
    data = q.sendSync('{`long$ til x}', 10)
    print('type: %s, numpy.dtype: %s, meta.qtype: %s, data: %s ' % (type(data), data.dtype, data.meta.qtype, data))

    # low-level query and read
    q.query(qconnection.MessageType.SYNC, '{`short$ til x}', 10) # sends a SYNC query
    msg = q.receive(data_only=False, raw=False) # retrieve entire message
    print('type: %s, message type: %s, data size: %s, is_compressed: %s ' % (type(msg), msg.type, msg.size, msg.is_compressed))
    data = msg.data
    print('type: %s, numpy.dtype: %s, meta.qtype: %s, data: %s ' % (type(data), data.dtype, data.meta.qtype, data))
    # close connection
    q.close()