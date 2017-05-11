<p align="center">
    <img src="https://rawgit.com/usnistgov/corr/master/corr-view/frontend/images/logo.svg"
         height="240"
         alt="CoRR logo"
         class="inline">
</p>

<h1> <p align="center"><sup><strong>
CoRR &ndash; The Cloud of Reproducible Records
</strong></sup></p>
</h1>

<p align="center"><sup><strong>
See the live instance at <a href="http://corr-root.org/">corr-root.org</a>.
</strong></sup></p>

<p align="center">
<a href="https://travis-ci.org/faical-yannick-congo/corr-deploy" target="_blank">
<img src="https://travis-ci.org/faical-yannick-congo/corr-deploy.svg?branch=master"
alt="Travis CI">
</a>
<a href="https://github.com/faical-yannick-congo/corr-deploy/issues" target="_blank">
<img src="http://githubbadges.herokuapp.com/faical-yannick-congo/corr-deploy/issues.svg?style=flat-square"
alt="Github Issues">
</a>
<a href="https://github.com/faical-yannick-congo/corr-deploy/pulls" target="_blank">
<img src="http://githubbadges.herokuapp.com/faical-yannick-congo/corr-deploy/pulls.svg?style=flat-square"
alt="Github Issues">
</a>
<!-- <a href="https://github.com/faical-yannick-congo/corr-deploy/issues" target="_blank">
<img src="http://githubbadges.herokuapp.com/faical-yannick-congo/corr-deploy/issues.svg?style=flat-square"
alt="Python Version">
</a> -->
<a href="http://mybinder.org/repo/faical-yannick/corr-deploy" target="_blank">
<img src="http://mybinder.org/badge.svg"
alt="Binder">
</a>
<a href="http://corr-deploy.readthedocs.io/en/latest/?badge=latest" target="_blank">
<img src="https://readthedocs.org/projects/corr-deploy/badge/?version=latest"
alt="Reathedocs">
</a>
<a href="https://gitter.im/usnistgov/corr">
<img src="https://img.shields.io/gitter/room/gitterHQ/gitter.svg" alt="Gitter Chat" height="18">
</a>
<a href="https://github.com/faical-yannick-congo/corr-deploy/blob/master/LICENSE">
<img src="https://img.shields.io/badge/license-mit-blue.svg" alt="License" height="18">
</a>
</p>

## Platform Provisioning

The Cloud of Reproducible Records (CoRR) is a web  app for storing,
viewing and managing metadata associated with scientific code execution records.

This repository is the toolkit required to manage a development and production
instance of the CoRR platform.

This toolkit allows a granular deployment of the different components of CoRR:
db, api, cloud and frontend.
The components can be deployed in the same host or in four different hosts.

Note: Before selecting your path of installation, please go to setup to make
the appropriate [Setup README](setup/README.md) needed for your option.

## Native Linux Management

This management is based on a linux ready configuration with ansible.
For none linux systems report to the next section with docker.
This setup was tested on Ubuntu systems: 14.04 to 16.04 and has proven
to work.
When using this native setup, your CoRR platform components (db, api, cloud
, frontend) will be system services. They will all be addressable through
the linux service API interface except for the frontend:

    $ sudo service mongodb start/stop/restart
    $ sudo service corrapi start/stop/restart
    $ sudo service corrcloud start/stop/restart
Also these services except for mongodb are all wrapped behind nginx and moreover 
behind gunicorn for corrapi and corrcloud and behind jekyll for the frontend.
The CoRR platform instance also handles the ufw firewall configurations.

To learn the specifics please refer to the [Native README](native/README.md)

## Docker based Management

This management setup depends on ansible and docker.
It will most likely work on any systems supporting ansible and docker-compose
version 2.0.
On a non native linux system you would want this setup. For linux systems
you would still want this version for two reasons. Firstly because the native
one did not work for your specific linux system and that your system support 
docker and ansible. Secondly because you are more of a container geek.
When using this setup, your CoRR platform components (db, api, cloud, frontend)
will be docker containers.
Differently from the native setup, the docker based one does not come with nginx
and ufw and will have to be managed separetly after the deployment in a production
environment.

To learn the specifics please refer to the [Docker README](docker/README.md)
