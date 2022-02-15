ARG TAG=latest

FROM lucascarmo/iac:$TAG
LABEL dockerfile.mantainer="lucascarmo"
WORKDIR /iac
COPY ansible_minikube/ ./
COPY .vagrant/machines/minikube/virtualbox/private_key ./
CMD ["ansible-playbook", "-i", "hosts", "playbook.yaml", "--ssh-common-args='-o StrictHostKeyChecking=no'"]