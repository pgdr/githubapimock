import os
import sqlite3

__FNAME = '/tmp/mock.sqlite'
__CONN = None


def _to_issue(issue):
    return {
        'title' : issue[0],
        'body':   issue[1],
        'user':   issue[2],
        'status': issue[3],
        'number': issue[4]
    }



def _create_github(fname):
    conn = sqlite3.connect(fname)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE issues (title, body, user, status, number)")
    cursor.execute("CREATE TABLE labels (label, number)")
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


def new_issue(title, body, user='', status='open', number=1):
    q = f'INSERT INTO issues VALUES(?, ?, ?, ?, ?)'
    __execute(q, (title, body, user, status, number), commit=True)
    return number


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
    q = 'SELECT * FROM labels WHERE number == ?'
    cursor = __execute(q, params=str(issue_id))
    return cursor.fetchall()


def drop_labels(issue_id):
    q = 'DROP FROM labels WHERE number == ?'
    __execute(q, params=str(issue_id), commit=True)


def add_label(label, issue_id):
    q = 'INSERT INTO labels VALUES (?,?)'
    cursor = __execute(q, params=str(label, issue_id))
    return cursor.fetchall()
