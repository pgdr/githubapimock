from . import _mock as mock

org = ''
repo = ''
username = ''
token = ''

PROGRESSION = ['backlog', 'todo', 'in progress', 'in review', 'done']
TICKET_TYPES = ['bug', 'feature', 'epic', 'duplicate', 'enhancement',
                'good first issue', 'help wanted', 'invalid',
                'question', 'wontfix']

def _get_labels(num):
    return mock.get_labels(org, repo, username, token, num)


def _create_issue_with_labels(title, body, labels):
    num = mock.create_issue(org, repo, username, token, title, body)
    mock.set_labels(org, repo, username, token, num, labels)
    return num


def create_issue(title, body):
    return _create_issue_with_labels(title, body, [])


def create_bug_report(title, body):
    return _create_issue_with_labels(title, body, ['bug'])


def create_feature_request(title, body):
    return _create_issue_with_labels(title, body, ['feature'])


def get_column(label):
    issues = mock.get_issues(org, repo, username, token)
    for issue in issues:
        num = issue['number']
        labs = _get_labels(num)
        if label in labs:
            yield issue


def get_state(number):
    return mock.get_state(org, repo, username, token, number)


def set_state(number, state):
    mock.set_state(org, repo, username, token, number, state)


def close_issue(number):
    mock.close_issue(org, repo, username, token, number)


def get_labels(number):
    return mock.get_labels(org, repo, username, token, number)


def _progress_to(number, progress_label):
    labs = _get_labels(number)
    new_labs = [progress_label] + [lab for lab in labs if lab not in PROGRESSION]
    mock.set_labels(org, repo, username, token, number, new_labs)


def reset_issue(number):
    _progress_to(number, 'backlog')


def start_issue(number):
    _progress_to(number, 'in progress')


def advance(number):
    labs = [lab for lab in _get_labels(number) if lab in PROGRESSION]
    if not labs:
        raise Exception(f'Issue {number} not labeled with progress')
    if labs[0] == 'done':
        raise Exception(f'Issue {number} completed, cannot progress further')
    idx = PROGRESSION.index(labs[0])
    _progress_to(number, PROGRESSION[idx+1])
