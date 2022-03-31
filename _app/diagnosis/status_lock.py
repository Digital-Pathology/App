
import contextlib
import threading

from . import config


class StatusLock(contextlib.AbstractContextManager):
    """ 
        A wrapper on threading.Lock that implements a context manager

        Example:
            with status_lock as permission:
                # do things
    """

    def __init__(self):
        self.lock = threading.Lock()

    def __enter__(self, *args, **kwargs):
        while not self.lock.acquire(timeout=config.DIAGNOSIS_RUNNER_STATUS_LOCK_TIMEOUT):
            pass  # wait for my turn
        return True

    def __exit__(self, *args, **kwargs):
        self.lock.release()
