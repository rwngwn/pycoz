import logging
import _sched as sched

from multiprocessing import Process
from pycoz.mounting import mount_proc

logger = logging.getLogger(__name__)


def _prepare_proc(func, mproc):
    if mproc:
        mount_proc()
    func()


def _unshare(flags, func):
    rc = sched.unshare(flags)
    if rc:
        raise Exception("Cannot unshare %d" % rc)

    process = Process(target=_prepare_proc, args=(func, True))
    process.start()
    process.join()


def spawn(func, process=False, net=False, ipc=False, mnt=False):
    """Spawns function func as a new process in a usnhared environment"""
    flags = 0x00000000
    if process:
        flags = flags ^ 0x20000000
    if net:
        flags = flags ^ 0x40000000
    if ipc:
        flags = flags ^ 0x08000000
    if mnt:
        flags = flags ^ 0x00020000

    process = Process(target=_unshare, args=(flags, func))
    process.start()
    return process
