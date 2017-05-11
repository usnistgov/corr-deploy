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
See the live instance at <a href="http://corr-root.org/">corr-root.org:5000</a>.
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

## Platform setup before execution

To start a fresh new CoRR instance, the admin/developer is required to do a minimal
setup involving unzipping these folders and placing them in the system.

## Admin setup

For the admin setup depending on the system in which the platform is being installed
few variations exists.
You will have to unzip all the compressed folders and place them in a location that
you will easily recall during these setup.
If you are using the native installation, you will have to replace the paths in the 
right variables in the hosts.local file or its copy in builds.

    $ corr_location=path/to/corr-src
    $ ssl_location=path/to/corr-ssl
    $ storage_location=parent/path/to/corr-storage

Unzip tmp and copy the values in the json file inside into the following variables:

    $ admin_email=congo@corr-root.org
    $ admin_password=Palin1987
    $ admin_fname=Faical Yannick
    $ admin_lname=Congo

In the mongodb.conf.j2 you will be able to put the path of data/db instead of the 
default dbpath, /var/lib/mongodb.
Finally if you would like to enforce account moderation by admin and content
inspection through anti-virus, please change the values of the following variables
to True

    $ account_moderation=False
    $ content_inspection=True

From this point you can perform the install and serve instructions in native.
If you ar using the docker installation, depending on the operating system you will
need to follow different directions.
For Mac OSX/Linux, you can proceed first as what was done in native but with the hosts.docker
file. You will have to make sure you have docker and docker-compose installed.
Also make sure docker is running:

    $ sudo service docker start

In this first case for OSX you can follow the docker installation steps.
The other alternative with OSX/Linux systems is to use the docker images right away
from docker hub. In this can You will have to follow the native setup example by placing
the files in an easy to recall location. Then you will have to open hub/docker-compose.yml
and provide the right VOLUME paths:

    $ /path/to/data/db:/data/db
    $ /path/to/corr-storage:/home/corradmin/corr-storage

Once this is done you will have to invoke docker-compose in the following order.
First you will need to pull the images:
    $ docker-compose pull
Then you will be able to run the containers:

    $ docker-compose up -d corrdb
    $ docker-compose up -d corrapi
    $ docker-compose up -d corrcloud
    $ docker-compose up -d corrview

You will have to give enough time to corrdb to start before carrying on with
corrapi and corrcloud. Also you will have to give enough time to corrcloud
to startup before starting corrview.
To follow the status of the running corrdb container:
   $ docker-compose logs corrdb
Your containers will be serving on 0.0.0.0. Go to http://0.0.0.0:5000 to
check the view status and link with the cloud.
In a non linux/OSX system like windows we recommend pulling the images
from docker hub. Secondly place the unziped files in an accessible location on
your computer. We recommend that you download and install docker-toolbox.
Use Kitematic to manage your containers. To download your images look for:

    $ palingwende/win_corrdb
    $ palingwende/win_corrapi
    $ palingwende/win_corrcloud
    $ palingwende/win_corrview

Then for each of them provide the right VOLUME path:

    $ /path/to/data/db:/data/db for corrdb
    $ /path/to/corr-storage:/home/corradmin/corr-storage for corrcloud and corrapi
    $ /path/to/tmp/tmp_admin.json:/tmp/tmp_admin.json

Also make sure the containers are on the right port in this order:

    $ corrdb: 27017
    $ corrapi: 5100
    $ corrcloud: 5200
    $ corrview: 5000

Finally verify that the docker deamon is running on the IP Address: 192.168.99.100
To check the status of the palftorm go to: http://192.168.99.100:5000.


## Developer setup

As a developer you will be able to change the deployment content and install corr
with more constum features to your use case. CoRR can only be development properly
 at least for the deployment mechanism only within a Linux/OSX environment.
This is due to facts like issues with ansible and docker in other systems to manage
this dynamic devops setup.
That being said, follow the same model for native and docker without the hub as
explained with the admin scope and you will be fine. You will be spending your time
installing and serving CoRR instances again and again until you reach your best
requirements.