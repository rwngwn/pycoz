import _mount


def mount(special_file, target, fs_type,
          flags=_mount.MS_PRIVATE ^ _mount.MS_REC,
          data=None):
    rc = _mount.mount(special_file, target, fs_type, flags, data)
    print(rc)


def mount_proc(target='/proc'):
    mount('proc', target, 'proc',
          _mount.MS_NODEV ^ _mount.MS_NOEXEC ^ _mount.MS_NOSUID)
