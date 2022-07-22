from contextlib import contextmanager

@contextmanager
def processor():
    print('--> start processing')
    yield
    print('<-- stop processing')


with processor():
    print(':: processing')