- Criar um script start.py que automatize o processo manual de execução dos comandos abaixo:

```bash
vagrant up minikube - concluído
docker container run -it -v $PWD:/iac -w /iac --entrypoint "" lucascarmo/iac:latest bash
ansible-playbook -i hosts playbook.yaml --ssh-common-args='-o StrictHostKeyChecking=no'
vagrant ssh minikube
minikube start
```

- Sugestão na parte do **docker** criar um Dockerfile com a imagem oficial do ansible passando no entrypoint o comando do ansible-playbook 

- Seguir depois com o fluxo de melhorias