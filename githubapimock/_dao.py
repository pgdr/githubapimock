import os
from peewee import *
import sqlite3

__FNAME = '/tmp/mock.sqlite'
db = SqliteDatabase(__FNAME)

# an issue has keys
#
# * active_lock_reason : one of off-topic, too heated, resolved, spam)
# * assignees : list of users
# * assignee : user
# * body : body
# * closed_at : timestamp
# * closed_by : user
# * comments : number of comments
# * comments_url : url
# * created_at : timestamp
# * events_url : url
# * html_url : url
# * id : id
# * labels : list of dicts with key name
# * labels_url : url
# * locked : bool
# * milestone : milestone
# * node_id : str
# * number : the id
# * pull_request : dict of urls
# * repository_url : url
# * state : open or closed
# * title : title
# * updated_at : timestamp
# * url : url
# * user : user


def _to_issue(issue, labs=tuple()):
    return {
        'number': issue.id,
        'title':  issue.title,
        'body':   issue.body,
        'user':   issue.user,
        'state':  issue.state,
        'labels': [ {'name': lab.name} for lab in labs ]
    }


class Issue(Model):
    title = CharField()
    body = CharField()
    user = CharField()
    state = CharField()

    class Meta:
        database = db

class Label(Model):
    name = CharField()
    issue = ForeignKeyField(Issue)

    class Meta:
        database = db


def new():
    global db
    try:
        if not db:
            db = SqliteDatabase(__FNAME)
        db.connect()
        db.create_tables([Issue, Label])
    except Exception as e:
        print(e)

def close():
    global db
    db.close()
    db = None
    os.unlink(__FNAME)

def new_issue(title, body, user='', state='open'):
    issue = Issue(
        title=title,
        body=body,
        user=user,
        state=state,
    )
    issue.save()
    return issue.id


def get_state(issue_id):
    return Issue.get(id=issue_id).state


def set_state(issue_id, state):
    issue = Issue.get(id=issue_id)
    issue.state = state
    issue.save()


def get_issue(issue_id):
    issue = Issue.get(Issue.id == issue_id)
    labs = Label.select().where(Label.issue == issue_id)
    return _to_issue(issue, labs=labs)


def get_issues(state='open'):
    return [_to_issue(issue) for issue in Issue.select()]


def get_labels(issue_id):
    labs = Label.select().where(Label.issue == issue_id)
    return [lab.name for lab in labs]


def drop_labels(issue_id):
    labs = Label.select().where(Label.issue == issue_id)
    for lab in labs:
        lab.delete_instance()


def add_label(label, issue_id):
    issue = Issue.get(id=issue_id)
    lab = Label(
        name=label,
        issue=issue)
    lab.save()
