#!/bin/bash
newgrp microk8s
microk8s enable metallb:10.64.140.43-10.64.140.49
microk8s kubectl apply -f deployment-db.yml
microk8s kubectl apply -f deployment-api.yml

