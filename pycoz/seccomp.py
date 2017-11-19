import _seccomp


def load(syscalls):
    if not syscalls:
        return
    ctx = _seccomp.seccomp_init(_seccomp.SCMP_ACT_ALLOW)
    for syscall in syscalls:
        _seccomp.seccomp_rule_add(ctx, _seccomp.SCMP_ACT_KILL,
                                  int(syscall), 0)
    _seccomp.seccomp_load(ctx)
    ctx = None
