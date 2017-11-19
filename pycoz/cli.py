import os

import click

from functools import partial

from pycoz.unshare import spawn
from pycoz import cgroups, seccomp


@click.group()
def cli():
    pass


@cli.command()
@click.option('--cmd', default='/bin/sh')
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


def command(cmd, syscalls):
    seccomp.load(syscalls)
    os.execve(cmd, [cmd], {'PS1': 'cont# '})
