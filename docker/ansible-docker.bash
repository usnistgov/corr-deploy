#!/bin/bash

export PATH=/usr/bin:$PATH
ansible-playbook $@ playbook.yaml
