#/bin/bash
make init

cd provisioning
ansible-playbook webapp.yml -i inventory/hosts
ansible-playbook bench.yml -i inventory/hosts

cd ../
curl -XPOST https://isucari.t.isucon.pw/initialize -H 'Content-Type: application/json' -d @initialize.json