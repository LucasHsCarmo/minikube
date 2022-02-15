import os
from time import sleep

name_server = "minikube"
print("\nCriando servidor {}\n".format(name_server))
start_machine = "vagrant up minikube"
os.system(start_machine)

print("\nTempo de espera\n")
for cronometro in range(10):
    print("Aguardando servidor estar up em {} segundos.".format(cronometro+1))
    tempo = sleep(1)

print("\nIniciando container para provisionamento do servidor\n")
start_container_ansible = "docker container run -it lucascarmo/ansible_minikube:v1"
os.system(start_container_ansible)

#start_minikube = ""
#os.system(start_minikube)