%module sched
%{
#define _GNU_SOURCE
#include <sched.h>
%}
int setns(int fd, int nstype);
int unshare(int nstype);
