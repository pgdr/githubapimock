import os
import sqlite3

__FNAME = '/tmp/mock.sqlite'
__CONN = None


def _to_issue(issue):
    return {
        'number': issue[0],
        'title':  issue[1],
        'body':   issue[2],
        'user':   issue[3],
        'status': issue[4],
    }



def _create_github(fname):
    conn = sqlite3.connect(fname)
    cursor = conn.cursor()

    issues = ', '.join(['number INTEGER PRIMARY KEY ASC',
                        'title TEXT',
                        'body TEXT',
                        'user TEXT',
                        'status TEXT'])
    q = f"CREATE TABLE issues ({issues});"
    cursor.execute(q)

    labels = 'label, number'
    cursor.execute(f"CREATE TABLE labels ({labels})")
    conn.commit()

    return conn


def new():
    global __CONN
    close()
    __CONN = _create_github(__FNAME)
    return __CONN


def close():
    global __CONN
    if __CONN is not None:
        __CONN.close()
    try:
        os.unlink(__FNAME)
    except FileNotFoundError:
        pass


def __execute(query, params=None, commit=False):
    global __CONN
    assert __CONN is not None
    if params is not None:
        assert type(params) == tuple, f'type of params was {type(params)}'
    if params is None:
        cursor = __CONN.execute(query)
    else:
        cursor = __CONN.execute(query, params)
    if commit:
        __CONN.commit()
    return cursor


def new_issue(title, body, user='', status='open'):
    q = 'INSERT INTO issues (title, body, user, status) VALUES (?, ?, ?, ?)'
    __execute(q, (title, body, user, status), commit=True)
    last = 'SELECT last_insert_rowid()'
    cursor = __execute(last)
    return cursor.fetchone()[0]



def set_status(issue_id, status):
    q = f'UPDATE issues SET status = ? WHERE number == ?'
    __execute(q, params=(status, issue_id), commit=True)


def get_issue(issue_id):
    assert type(issue_id) == int, f'was {type(issue_id)}'
    q = 'SELECT * FROM issues WHERE number == ?'
    cursor = __execute(q, params=(issue_id,))
    issue = cursor.fetchone()
    return _to_issue(issue)


def get_issues():
    q = 'SELECT * FROM issues'
    cursor = __execute(q)
    return [_to_issue(issue) for issue in cursor.fetchall()]


def get_labels(issue_id):
    q = 'SELECT label FROM labels WHERE number == ?'
    cursor = __execute(q, params=(issue_id,))
    return [e[0] for e in cursor.fetchall()]


def drop_labels(issue_id):
    q = 'DELETE FROM labels WHERE number == ?'
    __execute(q, params=(issue_id,), commit=True)


def add_label(label, issue_id):
    q = 'INSERT INTO labels (label, number) VALUES (?,?)'
    cursor = __execute(q, params=(label, issue_id), commit=True)
    return cursor.fetchall()
