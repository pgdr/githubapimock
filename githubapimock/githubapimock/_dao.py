import sqlite3

def _create_github(fname):
    conn = sqlite3.connect(fname)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE repos (name)")
    cursor.execute("CREATE TABLE issues (title, body)")
    conn.commit()
    return conn


class DAO:
    def __init__(self, fname, ip, port):
        print('create %s' % fname)
        self._conn = _create_github(fname)

    def __del__(self):
        print('closing ...')
        self._conn.close()
        print('removing ...')
        self._conn = None
        del self._conn
