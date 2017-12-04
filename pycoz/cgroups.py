import os

groups_types = {'cpu': '/sys/fs/cgroup/cpu/system.slice/',
                'memory': '/sys/fs/cgroup/memory/system.slice/'}


def create_cgroups(name):
    for group, path in groups_types.items():
        if os.path.exists(path):
            target = os.path.join(path, name)
            if not os.path.exists(target):
                os.makedirs(target)
        else:
            print('%s cgroup is not mounted' % group)


def assing_cgroups(name, pid):
    for _, path in groups_types.items():
        path = os.path.join(path, name, 'cgroup.procs')
        _write_data(path, pid)


def set_cpu_shares(name, shares):
    path = os.path.join(groups_types['cpu'], name, 'cpu.shares')
    _write_data(path, shares)


def set_memory_limit(name, limit):
    path = os.path.join(groups_types['memory'], name, 'cpu.shares')
    _write_data(path, limit)


def _write_data(path, data):
    if not os.path.exists(path):
        return
    with open(path, 'w') as fd:
        fd.write('%d\n' % int(data))
