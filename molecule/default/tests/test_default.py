import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_default_backports(host):
    p = host.file('/etc/apt/sources.list.d/backports.list')

    assert p.contains(
        'deb http://deb.debian.org/debian ' +
        host.system_info.codename +
        '-backports main contrib'
    )
