import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_installed_packages(host):
    assert host.package('nginx').is_installed
    assert host.package('nginx-common').is_installed
    assert host.package('nginx-extras').is_installed


def test_files(host):
    assert host.file('/etc/nginx/includes/').is_directory
    assert host.file('/etc/nginx/nginx.conf').exists
    assert not host.file('/etc/nginx/sites-enabled/default').exists
    assert host.file('/etc/nginx/includes/nginx_status').exists


def test_logrotate(host):
    with host.sudo():
        if host.file('/etc/logrotate.d/nginx').is_file:
            assert 'invoke-rc.d nginx rotate >/dev/null 2>&1' not in host.file(
                '/etc/logrotate.d/nginx'
            ).content_string
