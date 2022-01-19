# Minikube

Provisionando ambiente de estudos

# ignore ansible ssh authenticity checking
ansible-playbook -i hosts playbook.yaml --ssh-common-args='-o StrictHostKeyChecking=no'

### Faz o aumento do disksize no VMware
vagrant plugin install vagrant-disksize