from pyroute2 import IPDB, IPRoute
import os


def create_veth_path(fd):
    ip = IPDB()
    # create interface pair
    ip.create(ifname='pycoz0', kind='veth', peer='pycoz1').commit()
    ip.release()
    setup_ip('pycoz0', '10.0.0.1/24')
    # move peer to netns

    ip = IPDB()
    with ip.interfaces.pycoz1 as veth:
        veth.net_ns_fd = os.open(fd, os.O_RDONLY)
        # don't forget to release before exit

    return ip


def setup_ip(interface, ip):
    with IPDB() as ipdb:
        with ipdb.interfaces[interface] as i:
            i.add_ip(ip)
            i.up()
