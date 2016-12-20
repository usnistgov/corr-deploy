<p align="center">
    <img src="https://rawgit.com/usnistgov/corr/master/corr-view/frontend/images/logo.svg"
         height="240"
         alt="CoRR logo"
         class="inline">
</p>

<h1> <p align="center"><sup><strong>
Native Linux Deployment
</strong></sup></p>
</h1>

This management setup is most effective for Linux systems that support
ansible. The remote and host environment have to both be Linux based.

# Native Linux Installation
The deployment setup is run by executing a bash script: [config.bash](config.bash).
Before starting the installation, you should have a environment ready to avoid issues with your
root system environment. Install anaconda if not already done.
In this setup, the scripts will expected the environment corr-local. To create this environment:

	$ conda create -n corr-local python=3.4 anaconda

The installation requires sudo priviledges as following:

    $ sudo ./config.bash --ask-sudo --tags install --inventory-file builds/hosts.local

The hosts.local file contains the general configuration variables.
Before running the installation script, you should update variables in this file.
The storage_location variable specifies where the corr-storage folder should be placed.

The installation folder that contains the corr storage folder (corr-storage).
The corr-storage folders have to be moved to the provided specific location.
We recommand moving it to the root path to have /corr-storage on the api and cloud
components' instance.
The installation setup also allows specific components installations:

	$ sudo ./config.bash --ask-sudo --tags install --limit db --inventory-file builds/hosts.local
	$ sudo ./config.bash --ask-sudo --tags install --limit api --inventory-file builds/hosts.local
	$ sudo ./config.bash --ask-sudo --tags install --limit cloud --inventory-file builds/hosts.local
	$ sudo ./config.bash --ask-sudo --tags install --limit frontend --inventory-file builds/hosts.local

# Native Linux Deployment
In case of the platform deployed with the file system as a storage medium, There is a requirement that
constraint corrapi and corrcloud to be deployed on the same host. This is due to the fact that both 
component have to access the storage. Running them separately will result on inconsistencies. Further
work has to be done to have a secured ftp access to the storage which will make this remark obsolete
as sftp will be prefered over the current capability.

## Native Linux Development
For development in native mode, you may follow the steps below.
Start the dabatase:

    	$ sudo service mongodb start

Run the api component:

    	$ cd corr-api
	$ python run.py

Run the cloud component:

	$ cd ../corr-cloud
	$ python run.py

Run the frontend component:

	$ cd ../corr-view/frontend
	$ jekyll serve --watch --port 5000 --host 0.0.0.0

The current [hosts.local](builds/hosts.local) file contains the development configuration for the platform to
be installed and deployed locally.

## Native Linux Production
The platform can be deployed through the following command:

	$ sudo ./config.bash --ask-sudo --tags serve --inventory-file builds/hosts.local

There is also the possibility to deploy each component separately by using the --limit
parameter:

	$ sudo ./config.bash --ask-sudo --tags serve --limit db --inventory-file builds/hosts.local
	$ sudo ./aconfig.bash --ask-sudo --tags serve --limit api --inventory-file builds/hosts.local
	$ sudo ./config.bash --ask-sudo --tags serve --limit cloud --inventory-file builds/hosts.local
	$ sudo ./config.bash --ask-sudo --tags serve --limit frontend --inventory-file builds/hosts.local

For remote production deployment and installation, a modified version of the [hosts.local](builds/hosts.local) file
has to be provided. The components (corrdb, corrapi, corrcloud, corrfrontend) hosts have to be provided.
Also the ssh key and user should be updated.

## Native Linux Debugging
In the case of development, you will be able to have direct logs from the components executions. For 
the production version on the other end, all component are system services. As such they all produce
logs stored in /var/log. You will find: mongodb, corrapi, corrcloud. corrfrontend does not currently
persist logs.
