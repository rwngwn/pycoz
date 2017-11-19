%module mount
%{
#include <sys/mount.h>
%}

extern int mount (const char *__special_file, const char *__dir,
                  const char *__fstype, unsigned long int __rwflag,
                  const void *__data);

#define MS_PRIVATE 0x40000
#define MS_REC 0x4000
#define MS_NODEV 0x4
#define MS_NOEXEC 0x8
#define MS_NOSUID 0x2
