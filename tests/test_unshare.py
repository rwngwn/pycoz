import os
import socket

from functools import partial
from multiprocessing import Pipe

from pycoz.unshare import spawn


def _get_pid(pipe):
    pipe.send(os.getpid())


def _get_net(pipe):
    pipe.send(socket.if_nameindex())


def test_spawn_pid():
    par_pipe, child_pipe = Pipe()
    func = partial(_get_pid, child_pipe)
    p = spawn(func, process=True, ipc=True)
    p.join()
    assert par_pipe.recv() == 1


def atest_spawn_net():
    rq, p = spawn(_get_net, net=True)
    assert rq.recv() == [(1, 'lo')]
    p.join()

