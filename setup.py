from distutils.core import setup, Extension

setup(name="pycoz",
      version='0.0.1',
      author="David Becvarik",
      license='gpl3',
      ext_modules=[Extension("_sched", sources=["sched.i"]),
                   Extension("_seccomp", sources=["seccomp.i"],
                             libraries=['seccomp']),
                   Extension("_mount", sources=["mount.i"])])
