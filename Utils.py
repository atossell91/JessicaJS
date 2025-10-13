import os

def get_jessica_root():
    return os.path.dirname(os.path.realpath(__file__))

def expand_path(path):
    return os.path.abspath(
        os.path.realpath(path))
