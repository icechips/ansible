# pizza-Ansible

Repository for the ansible code to manage the Pizza application. 


###Setup ansible connection with AWS, to pull from Secrets Manager
```
export AWS_PROFILE=pizza-$env
aws sso login --profile pizza-$env
```

###Current environments available
```
pizza_dev
pizza_uat
pizza_production
```

###Role Commands
```
ansible-playbook -i pizza_inventory pizza_build.yml -l 'pizza_$env' --become --diff --tags common --check #dependency installs
ansible-playbook -i pizza_inventory pizza_build.yml -l 'pizza_$env' --become --diff --tags backend --check #python backend installs
ansible-playbook -i pizza_inventory pizza_build.yml -l 'pizza_$env' --become --diff --tags frontend --check #npm/django frontend installs
ansible-playbook -i pizza_inventory pizza_build.yml -l 'pizza_$env' --become --diff --tags web --check #nginx/gunicorn web installs
```

###Shortcut plays to update conf files
```
ansible-playbook -i pizza_inventory pizza_build.yml -l 'pizza_$env' --become --diff --tags gunicorn --check #this is for the gunicorn frontend files (settings.py and/or gunicorn_start)
ansible-playbook -i pizza_inventory pizza_build.yml -l 'pizza_$env' --become --diff --tags nginx --check #this is for the nginx-ebc-py3.conf
ansible-playbook -i pizza_inventory pizza_build.yml -l 'pizza_$env' --become --diff --tags logrotate --check #this is for lorgotate related configs
```

###Running shell commands from ansible
```
ansible -i pizza_inventory 'pizza_$env' -m shell --become -a '$COMMAND'
```