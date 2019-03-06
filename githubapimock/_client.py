from . import _mock as mock

repo = ''
username = ''
token = ''

PROGRESSION = ['backlog', 'todo', 'in progress', 'in review', 'done']
TICKET_TYPES = ['bug', 'feature', 'epic']

def _get_labels(num):
    return mock.get_labels(repo, username, token, num)

def create_bug_report(title, body):
    num = mock.create_issue(repo, username, token, title, body)
    mock.set_labels(repo, username, token, num, ['bug'])
    return num

def get_column(label):
    issues = mock.get_issues(repo, username, token)
    for issue in issues:
        num = issue['number']
        labs = _get_labels(num)
        if label in labs:
            yield issue

def get_labels(number):
    return mock.get_labels(repo, username, token, number)

def _progress_to(number, progress_label):
    labs = _get_labels(number)
    new_labs = [progress_label] + [lab for lab in labs if lab not in PROGRESSION]
    mock.set_labels(repo, username, token, number, new_labs)

def reset_issue(number):
    _progress_to(number, 'backlog')

def start_issue(number):
    _progress_to(number, 'in progress')
