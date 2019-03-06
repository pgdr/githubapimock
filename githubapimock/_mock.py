from . import _dao as dao


def create_issue(repo, username, token, title, body) -> int:
    id_ = dao.new_issue(title, body)
    return id_


def get_status(repo, username, token, issue_id):
    return dao.get_status(issue_id)


def set_status(repo, username, token, issue_id, status):
    dao.set_status(issue_id, status)


def close_issue(repo, username, token, issue_id):
    set_status(repo, username, token, issue_id, 'closed')


def get_issue(repo, username, token, issue_id) -> dict:
    return dao.get_issue(issue_id)


def get_issues(repo, username, token):
    return dao.get_issues()


def get_labels(repo, username, token, issue_id):
    return dao.get_labels(issue_id)


def set_labels(repo, username, token, issue_id, labels:list):
    dao.drop_labels(issue_id)
    for label in labels:
        dao.add_label(label, issue_id)
