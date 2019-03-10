import os
import yaml
import githubapimock as api

api.new()  # for mocking

RCFILE = os.path.expanduser('~/.github.yml')

def _settings():
    if not os.path.isfile(RCFILE):
        return None
    with open(RCFILE, 'r') as f:
        return yaml.load(f)

def _q_token():
    token = input(f'Enter GitHub token: ')
    return token

def _q_user():
    default = os.getenv('USER').lower()
    user = input(f'Enter GitHub user name [{default}]: ')
    return user if user else default

def _q_org(user):
    org = input(f'Enter GitHub organization [{user}]: ')
    return org if org else user

def _q_repo():
    repo = input(f'Enter GitHub repo: ')
    return repo

def _q_for_missing(settings, requery=False):
    if 'user' not in settings or requery:
        settings['user'] = _q_user() or settings['user']
    if 'token' not in settings or requery:
        settings['token'] = _q_token() or settings['token']
    if 'org' not in settings or requery:
        settings['org'] = _q_org(settings['user']) or settings['org']
    if 'repo' not in settings or requery:
        settings['repo'] = _q_repo() or settings['repo']

    return settings

def _q_for_save(settings):
    ans = ''
    while ans not in ('y', 'n'):
        ans = input('Would you like to save your settings? y/n: ')
    if ans == 'y':
        with open(RCFILE, 'w') as f:
            yaml.dump(settings, f, default_flow_style=False)


def print_issue(issue):
    msg = f"""Issue {issue['number']}: {issue['title']}

{issue['body']}

Labels: {[lab['name'] for lab in issue['labels']]}"""
    print(msg)



def _menu_change_settings(settings):
    return _q_for_missing(settings, requery=True)


def _menu_get_issue(settings):
    num = input('Enter issue number: ')
    issue = api.get_issue(
        org=settings['org'],
        repo=settings['repo'],
        username=settings['user'],
        token=settings['token'],
        issue_id=num)

    print_issue(issue)

    return issue


def _menu_new_issue(settings):
    title = input('Enter title: ')
    body = input('Enter body: ')
    label = input('Enter labels (comma separated): ')
    labels = label.split(',')
    return api.create_issue(
        org=settings['org'],
        repo=settings['repo'],
        username=settings['user'],
        token=settings['token'],
        title=title,
        body=body)


def _menu_close_issue(settings):
    num = input('Enter issue number to close: ')
    return api.close_issue(
        org=settings['org'],
        repo=settings['repo'],
        username=settings['user'],
        token=settings['token'],
        issue_id=num)


def _menu_quit(settings):
    api.close()
    exit()


def _menu(settings):
    size = 20
    msg = f"""{"Change settings".ljust(size)}[s]
{"Get issue".ljust(size)}[g]
{"New issue".ljust(size)}[n]
{"Close issue".ljust(size)}[c]
{"Quit".ljust(size)}[q]
"""
    choices = {
        's' : _menu_change_settings,
        'g' : _menu_get_issue,
        'n' : _menu_new_issue,
        'c' : _menu_close_issue,
        'q' : _menu_quit,
    }
    ans = ''
    while ans not in choices:
        ans = input(msg)
    return choices[ans](settings)


def _interactive_loop(settings):
    _menu(settings)


def interactive():
    s = _settings()
    had_rc = True
    if s is None:
        print(f'No settingsfile {RCFILE}, you must manually enter token.')
        s = {}
        had_rc = False
    s = _q_for_missing(s)
    if not had_rc:
        _q_for_save(s)
    _interactive_loop(s)

if __name__ == '__main__':
    interactive()
