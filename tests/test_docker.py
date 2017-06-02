from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_letsencrypt_folder(host):
    # letsencrypt = host.file("/etc/letsencrypt")
    letsencrypt = host.file("/var/log/certbot")
    assert letsencrypt.is_directory
    assert letsencrypt.user == "root"
    assert letsencrypt.group == "root"
    assert letsencrypt.mode == 0o755
