import os
if os.getenv('MOCK'):
    from ._mock import *
else:
    from ._github import *
from ._dao import new, close
from . import _client as client



__version__ = '0.0.4'
