# Minikube

Provisionando ambiente de estudos local com as seguintes ferramentas:

Nome                              | Versão          | Link
----------------------------------|-----------------|----------------------------------------------------
`Vagrant`                         | `latest`        | [Documentacao Oficial](https://www.vagrantup.com/)
`VirtualBox`                      | `latest`        | [Documentacao Oficial](https://www.virtualbox.org/)
`Docker`                          | `latest`        | [Documentacao Oficial](https://docs.docker.com/engine/install/)
`Minikube`                        | `latest`        | [Documentacao Oficial](https://minikube.sigs.k8s.io/docs/start/)

Criando servidor **minikube** com as seguintes características do **Vagranfile**:

Configuração                             | Descrição
-----------------------------------------|--------------------
`machine.vm.box`                         | `ubuntu/bionic64`
`ip`                                     | `Checar o range de IP disponível`

## Etapas de execução: 

Criando servidor e verificando status

```bash
vagrant up minikube
vagrant status
```

Após o servidor **minikube** estiver **running**, abrir outra aba do terminar para executar o **container** responsável por configurar o ambiente minikube.

Container que executará o ansible: [Imagem DockerHub](https://hub.docker.com/repository/docker/lucascarmo/iac)

```bash
docker container run -it -v $PWD:/iac -w /iac --entrypoint "" lucascarmo/iac:latest bash
```

No arquivo de inventário **hosts**, utilizar o mesmo **ip** adicionado no **Vagrantfile**.

Configuração                             | Descrição
-----------------------------------------|----------------------------------
`hosts`                                  | `Checar o range de IP disponível`

Realizado o passo citado a cima, dentro do container seguiremos da seguinte forma:

**OBS:** Comando --ssh-common-args='-o StrictHostKeyChecking=no' é responsável por ignorar o checking ssh de autenticação.

```bash
ansible-playbook -i hosts playbook.yaml --ssh-common-args='-o StrictHostKeyChecking=no'
```

Conectando via ssh no servidor minikube e startando serviço

```bash
vagrant ssh minikube
minikube start
```

Desligando servidor minikube

```bash
vagrant halt minikube
```

Destruindo servidor minikube

```bash
vagrant destroy -f minikube
```