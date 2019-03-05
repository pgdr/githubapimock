import os

from contextlib import contextmanager
from tempfile import NamedTemporaryFile as ntf

from ._dao import DAO
from ._rest import rest



@contextmanager
def mock(ip, port):
    db_path = ntf(delete=False).name
    github = DAO(db_path, ip, port)
    with rest(ip, port):

        yield

    del github

    os.unlink(db_path)
