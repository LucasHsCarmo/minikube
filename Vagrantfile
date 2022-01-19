# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.define "minikube" do |machine|
    machine.vm.box = "ubuntu/bionic64"
    machine.vm.network "private_network", ip: "192.168.56.20"
    machine.vm.provider "virtualbox" do |vb| 
      vb.name = "minikube.dev"
      vb.memory = 2048
      vb.cpus = 2
      vb.customize ["modifyvm", :id, "--groups", "/Lab-k8s"]
    end
  end
end
