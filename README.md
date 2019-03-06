# Day 1 (Introduction to Python)

In Windows using Jupyter Notebook -- A playground / experimentation lab.

Open Slack!

1. Introduction to programming
 * What is a computer program
 * What is correctness
 * What is maintainability
 * Is there such a thing as "good code"?
2. Methodology
 * What is a programming methodology
 * What is agile, scrum, kanban and XP
 * Who are SCOUT and how do they work?
3. Variables, types, functions, modules, tdd, exceptions
 * Basic types
  * int/float/bool
  * str
  * list
  * dict
 * Loop and control flow
  * for
  * if
 * Functions
  * well defined
  * naming
  * black box
 * modules and encapsulation
  * e.g. `get` from `requests`
4. Make a repository
 * Get to know GitHub
 * What is git?  (more about this Day 2)
5. Create GitHub issues from YAML via API
 * What is an issue
 * What are the properties of an issue?
  * title
  * body
  * user
  * number
 * Use dict to represent an issue
 * Severals issues are contained in a list of dicts


# Day 2 (Introduction to serious Python)

In Linux using gedit and the terminal, as well as git.

1. No more playtime
 * start terminal
 * start editor
 * run program from terminal
2. Running Python on Linux
 * Source `PYTHON_VERSION=3.7.1`
 * Create virtualenvs
3. `git clone`, `status`, `diff`, `add`, `commit`, `push`
4. Implement API (below)
5. Test, `setup.py`, Travis,
6. Implement client (for the rest of your life)


# Appendix



# The YAML for Day 1


```yml
* title: Define an issue
  body:  Use comments in the source code, or better yet, a function (abstraction), which takes title, body and returns a dict
* title: Implement create_issue
  body:  `create_issue` takes input `repo`, `username`, `token`, `title`, `body`, and returns `id`?
* title: Implement close_issue
  body:  `close_issue` takes input `repo`, `username`, `token`, `issue_id`
* title: Implement get_issue
  body:  `get_issue` takes input `repo`, `username`, `token`, `issue_id`
* title: Implement get_issues
  body:  `get_issues` takes input `repo`, `username`, `token`
* title: Advanced: Implement get_labels
  body:  `get_labels` takes input `repo`, `username`, `token`, `issue_id`
* title: Advanced: Implement set_labels
  body:  `set_labels` takes input `repo`, `username`, `token`, `issue_id`, `labels:list`
```

# The API

```python
def create_issue(repo, username, token, title, body) -> int:
    pass

def close_issue(repo, username, issue_id):
    pass

def get_issue(repo, username, token, issue_id) -> dict:
    pass

def get_issues(repo, username, token):
    pass

def get_labels(repo, username, token, issue_id):
    pass

def set_labels(repo, username, token, issue_id, labels:list):
    pass
```

# The Client

```python

progress = ['backlog', 'todo', 'in progress', 'in review', 'done']
categories = ['bug', 'feature']

def advance_issue(issue_id):
    pass

def reset_issue(issue_id):
    pass

def start_issue(issue_id):
    pass

def list_assigned_issues(user):
    pass

def get_column(label):
    pass

def get_todays_change():
    pass

def create_bug_report(title, body):
    pass
```
