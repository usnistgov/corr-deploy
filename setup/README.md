<p align="center">
    <img src="https://rawgit.com/usnistgov/corr/master/corr-view/frontend/images/logo.svg"
         height="240"
         alt="CoRR logo"
         class="inline">
</p>

<h1> <p align="center"><sup><strong>
Platform Setup
</strong></sup></p>
</h1>

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
    $ storage_location=path/to/corr-storage

Unzip tmp and copy the values in the json file inside into the following variables:

    $ admin_email=admin@domain.org
    $ admin_password=password
    $ admin_fname=Admin First Name
    $ admin_lname=Admin Last Name

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
For Docker, you can proceed first as what was done in native but with the hosts.docker
file. You will have to make sure you have docker and docker-compose installed.
Also make sure docker is running:

    $ sudo service docker start

The docker section show how to build the containers from the deployment.
The other alternative is to use the docker images right away
from docker hub. In this can You will have to follow the native setup example by placing
the files in an easy to recall location. Then you will have to open docker/hub/os/docker-compose.yml
and provide the right VOLUME paths:

    $ /path/to/data/db:/data
    $ /path/to/corr-storage:/home/corradmin/corr-storage
    $ /path/to/tmp:/tmp

Make sure to select the folder of your operating system. We provide Windows, OsX and Linus    
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
The CoRR instance will be served on 0.0.0.0. Go to http://0.0.0.0:5000 to
check the view status and link with the cloud.
In a non linux/OSX system like windows we recommend pulling the images
from docker hub. Secondly place the unziped files in an accessible location on
your computer. We recommend that you download and install [docker-toolbox](https://docs.docker.com/toolbox/toolbox_install_windows/).
Use [Kitematic](https://kitematic.com/) to manage your containers. To download your images look for:

    $ palingwende/vbox_corrdb
    $ palingwende/vbox_corrapi
    $ palingwende/vbox_corrcloud
    $ palingwende/vbox_corrview

Then for each of them provide the right VOLUME path:

    $ /path/to/data:/data for corrdb
    $ /path/to/corr-storage:/home/corradmin/corr-storage for corrcloud and corrapi
    $ /path/to/tmp:/tmp/

Note: Make sure that the data folder has a db folder and that the tmp folder contains the
first admin credentials in a json file named tmp_admin.json. The content is as following:

    {
      "admin-email":"admin@test.org",
      "admin-password":"Palingwende1987!",
      "admin-fname":"Faical",
      "admin-lname":"Congo"
    }

Also make sure the containers are on the right port in this order:

    $ corrdb: 27017
    $ corrapi: 5100
    $ corrcloud: 5200
    $ corrview: 5000

Finally verify that the docker deamon is running on the IP Address: 192.168.99.100
To check the status of the palftorm go to: http://192.168.99.100:5000.

## Developer setup

As a developer you will be able to change the deployment content and install corr
with more custum features to your use case. CoRR can only be developed properly
 at least for the deployment mechanism only within a Linux/OSX environment.
This is due to facts like issues with [Ansible](https://www.ansible.com/resources/get-started) and docker in other systems to manage
this dynamic devops setup.
That being said, follow the same model for native and docker without the hub as
explained with the admin scope and you will be fine. You will be spending your time
installing and serving CoRR instances again and again until you reach your best
requirements.
