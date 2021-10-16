#!/bin/bash

if [ $(id -u) -ne 0 ];
  then echo "Pleae run as root"
  exit
fi
if [ -z "$(grep saic.example.com /etc/hosts)" ];
  then echo 'Adding saic.example.com domain to /etc/hosts'
  echo '127.0.0.1 saic.example.com'>>/etc/hosts
else
  echo 'Domain found, no need to re add'
fi
if [ -z "$(grep kp.example.com /etc/hosts)" ];
  then echo 'Adding kp.example.com domain to /etc/hosts'
  echo '127.0.0.1 kp.example.com'>>/etc/hosts
else
  echo 'Domain found, no need to re add'
fi
