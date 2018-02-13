<p align="center">
    <img src="https://rawgit.com/usnistgov/corr/master/corr-view/frontend/images/logo.svg"
         height="240"
         alt="CoRR logo"
         class="inline">
</p>

<h1> <p align="center"><sup><strong>
Docker Based Deployment
</strong></sup></p>
</h1>

This management setup is most effective for non Linux systems that support
ansible and docker. Neither the remote nor the host environment have
to be Linux based.

# Docker Based Installation
The deployment setup is run by executing a bash script: [ansible-docker.bash](https://github.com/usnistgov/corr-deploy/blob/master/docker/ansible-docker.bash).
Before starting the installation, you should have a environment ready to avoid issues with your
root system environment. Install anaconda if not already done.
In this setup, the scripts will expected the environment corr-local. To create this environment:

	$ conda create -n corr-local python=3.4 anaconda

The installation requires sudo priviledges and due to networking constraints when building docker containers for native use or vbox based use, we provide two playbooks.
The build is done as following for native use:

    $ sudo ./ansible-docker.bash playbook-native.yaml --ask-sudo --tags install --inventory-file hosts.docker

The build is done as following for vbox use:

    $ sudo ./ansible-docker.bash playbook-vbox.yaml --ask-sudo --tags install --inventory-file hosts.docker

The networking fields in folders virtualbox and native display the constraints. In fact, when using docker in Kitematic, the IP addresses are set for 192.168.99.100. Which is what we use for the vbox build. For native build, the developer has the freedom to chose whatever IP.

The hosts.docker file contains the general configuration variables.
The installation step produces a builds folder that contains the corr source code (corr),
the aws config folder (aws), the database storage folder (data), the corr storage folder
(corr-storage), the requirements file and all the platform components generated Dockerfile
(Dockerfile-db, Dockerfile-api, Dockerfile-cloud, Dockerfile-frontend).
The data and corr-storage folders have to be moved to a specific location on the host machine.
We recommand moving it to the root path to have /data and /corr-storage.
On non linux platforms these folders have to be shared through Docker.
For example on Mac OSX: [sharing-folders-docker.jpeg](https://github.com/usnistgov/corr-deploy/blob/master/docker/sharing-folders-docker.jpeg).
During the installation process ansible will ssh into the hosts and produce the appropriate
builds content for the right platform component location (specified in the hosts.docker).
The installation setup also allows specific components installations. For example in a native build use case:

	$ sudo ./ansible-docker.bash playbook-native.yaml --ask-sudo --tags install --limit db --inventory-file hosts.docker
	$ sudo ./ansible-docker.bash playbook-native.yaml --ask-sudo --tags install --limit api --inventory-file hosts.docker
	$ sudo ./ansible-docker.bash playbook-native.yaml --ask-sudo --tags install --limit cloud --inventory-file hosts.docker
	$ sudo ./ansible-docker.bash playbook-native.yaml --ask-sudo --tags install --limit frontend --inventory-file hosts.docker

# Docker Based Deployment
On the advent of the data and corr-storage not being moved to the root path.
The exact path have to be overwritten in the docker-compose.yaml file in the volumes
section for corrdb, corrapi and corrcloud.
The platform (native build) can be deployed through the following command:

	$ sudo ./ansible-docker.bash   playbook-native.yaml --ask-sudo --tags serve --inventory-file hosts.docker

There is also the possibility to deploy each component (native docker) separately by using the --limit
parameter:

	$ sudo ./ansible-docker.bash  playbook-native.yaml --ask-sudo --tags serve --limit db --inventory-file hosts.docker
	$ sudo ./ansible-docker.bash  playbook-native.yaml --ask-sudo --tags serve --limit api --inventory-file hosts.docker
	$ sudo ./ansible-docker.bash  playbook-native.yaml --ask-sudo --tags serve --limit cloud --inventory-file hosts.docker
	$ sudo ./ansible-docker.bash  playbook-native.yaml --ask-sudo --tags serve --limit frontend --inventory-file hosts.docker

In case of the platform deployed with the file system as a storage medium, There is a requirement that
constraint corrapi and corrcloud to be deployed on the same host. This is due to the fact that both
component have to access the storage. Running them separately will result on inconsistencies. Further
work has to be done to have a secured ftp access to the storage which will make this remark obsolete
as sftp will be prefered over the current capability.

## Docker Based Development
The current [hosts.docker](https://github.com/usnistgov/corr-deploy/blob/master/docker/hosts.docker) file contains the development configuration for the platform to
be installed and deployed locally.

## Docker Based Production
For production deployment and installation, a modified version of the [hosts.docker](https://github.com/usnistgov/corr-deploy/blob/master/docker/hosts.docker) file
has to be provided. The components (corrdb, corrapi, corrcloud, corrfrontend) hosts have to be provided.
Also the ssh key and user should be updated.

## Docker Based Debugging
Each component in the platform containers produce a log accessible through docker-compose:

	$ sudo docker-compose logs corrdb
	$ sudo docker-compose logs corrapi
	$ sudo docker-compose logs corrcloud
	$ sudo docker-compose logs corrview

## Docker Hub deployment
CoRR can be pulled, configured and launched with the hub folder content. We provide three suported groups of OS: Linux, OSX and Windows. We recommend the instance administrator to first unzip the compressed folders in setup and follow the setup page. Inside tmp, change the admin email, password, first name and last name. Then provide the path to the location of the unziped folders: data, corr-storage and tmp. Note: Create a db folder inside data.
At this point, the admin can pull the images.
After the containers are pulled, the admin must take a look at the docker-compose file to verify that the exposed ports are available on the system. Moreover, the admin can change them by following the docker port mapping documentations. When done, it is time to launch the instance:

  $ sudo docker-compose pull
  $ sudo docker-compose up -d

At this point, the admin can follow anything provided before such as debugging each container, stop them and launching them individually.
