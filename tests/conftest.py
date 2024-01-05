import logging
import os
import subprocess


def pytest_runtest_setup(item: "Item") -> None:
    the_environment = os.getenv('ENV_FOR_DYNACONF')
    logging.info("Env for dynaconf: %s" % the_environment)
    if "satellite" in the_environment:
        logging.info("Start to configure the rhel for satellite")
        #satellite hostname will be gotton from dynaconf or CI job parameter, not decide the final solution
        satellite_hostname = "ci-vm-10-0-96-150.hosted.upshift.rdu2.redhat.com"
        cmd = 'rpm -qa | grep kate | xargs rpm -e;rpm -Uvh http://%s/pub/katello-ca-consumer-%s-1.0-1.noarch.rpm' % (satellite_hostname, satellite_hostname)
        ret, _ = subprocess.getstatusoutput(cmd)
        assert ret == 0
