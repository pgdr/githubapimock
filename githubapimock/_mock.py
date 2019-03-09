from . import _dao as dao


def create_issue(org, repo, username, token, title, body) -> int:
    id_ = dao.new_issue(title, body)
    return id_


def get_state(org, repo, username, token, issue_id):
    return dao.get_state(issue_id)


def set_state(org, repo, username, token, issue_id, state):
    dao.set_state(issue_id, state)


def close_issue(org, repo, username, token, issue_id):
    set_state(org, repo, username, token, issue_id, 'closed')


def get_issue(org, repo, username, token, issue_id) -> dict:
    return dao.get_issue(issue_id)


def get_issues(org, repo, username, token):
    return dao.get_issues()


def get_labels(org, repo, username, token, issue_id):
    return dao.get_labels(issue_id)


def set_labels(org, repo, username, token, issue_id, labels:list):
    dao.drop_labels(issue_id)
    for label in labels:
        dao.add_label(label, issue_id)
