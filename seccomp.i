%module seccomp
%{
#include <seccomp.h>
%}

extern int seccomp_rule_add(scmp_filter_ctx ctx, uint32_t action,
                            int syscall, unsigned int arg_cnt, ...);

extern scmp_filter_ctx seccomp_init(uint32_t def_action);

extern int seccomp_rule_add(scmp_filter_ctx ctx,
			    uint32_t action, int syscall, unsigned int arg_cnt, ...);

extern int seccomp_load(const scmp_filter_ctx ctx);

typedef unsigned uint32_t;

#define SCMP_ACT_KILL           0x00000000
#define SCMP_ACT_ALLOW          0x7fff0000

