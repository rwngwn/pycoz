import os

import click
import time
from functools import partial

from pycoz.unshare import spawn
from pycoz.network import create_veth_path, setup_ip
from pycoz import cgroups, seccomp


@click.group()
def cli():
    pass


@cli.command()
@click.option('--cmd', default='/bin/bash')
@click.option('--process', default=True)
@click.option('--net', default=True)
@click.option('--ipc', default=True)
@click.option('--mnt', default=True)
@click.option('--limit-cpu', default=None)
@click.option('--limit-mem', default=None)
@click.option('--block-syscall', multiple=True, default=[])
def run(cmd, process, net, ipc, mnt, limit_cpu, limit_mem,
        block_syscall):
    exec_cmd = partial(command, cmd, block_syscall)
    p = spawn(exec_cmd, process, net, ipc, mnt)
    cgroups.create_cgroups('pycoz')
    cgroups.assing_cgroups('pycoz', p.pid)
    if limit_cpu:
        cgroups.set_cpu_shares('pycoz', limit_cpu)
    if limit_mem:
        cgroups.set_memory_limit('pycoz', limit_mem)
    ip = create_veth_path('/proc/%s/ns/net' % p.pid)
    # we need to wait here for containers to finish so we can cleanup
    p.join()
    print('exiting container')
    ip.release()


def command(cmd, syscalls):
    time.sleep(2)
    seccomp.load(syscalls)
    setup_ip('pycoz1', '10.0.0.2/24')
    os.execve(cmd, [cmd], {'PS1': 'cont# '})
