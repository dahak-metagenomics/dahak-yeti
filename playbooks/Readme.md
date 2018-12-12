# Ansible Playbooks

This directory contains ansible playbooks and related files.

## Quick Start

### Using Vagrant For Local Testing

The following quick start will run the Ansible playbook and deploy
the specified steps to Vagrant virtual machines on the local host.
This assumes you already have Vagrant installed locally.

**Using Vagrant:**

Use the Vagrantfile in this directory to bring the Vagrant
host(s) up:

```
vagrant up
```

Note that this will run the `provision.yml` Ansible playbook
against each virtual host, as per the Vagrantfile, so you
do not need to run any plays from `provision.yml`.

To check that the machines are running:

```
vagrant status
```

To force all the machines to stop:

```
vagrant halt --force
```

**Using Ansible:**

To run Ansible, specify the inventory file with the -i flag,
then specify the nam of the playbook:

```
ansible-playbook -i hosts main.yml
```

As mentioned, the `provision.yml` playbook is automatically
run by Vagrant when each host is created, so it does not need
to be run on Vagrant machines.

## Playbooks

* `provision.yml` - this is the initial playbook that is run
  when servers are being provisioned; this uses aptitude to 
  install Python 2 on the remote machine so that Ansible is
  usable on the remote machine.

* `main.yml` - this is the principal playbook for preparing 
  compute nodes to run dahak-yeti workflows.

## Roles

* `lfit.python-install` - system Python and Pyenv Python installation

## Hosts

Most typically, dahak-yeti will be working with 
remote hosts on AWS.


