import datetime

class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


def timestamp():
    now = datetime.datetime.now()
    return int(round(now.timestamp()))
