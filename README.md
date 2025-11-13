# Подюков Илья. ФИТ-2-2024 НМ. Методы и инструменты DevOps. ЛР по лекции 9

- через pacman устанавливаю minicube и kubectl
- запускаю kubectl в режиме однонодового кластера k8s
```
ilya@erth ~ [14]> minikube start --vm-driver=docker 
😄  minikube v1.37.0 на Arch 
✨  Используется драйвер docker на основе конфига пользователя
📌  Using Docker driver with root privileges
👍  Starting "minikube" primary control-plane node in "minikube" cluster
🚜  Pulling base image v0.0.48 ...
💾  Скачивается Kubernetes v1.34.0 ...
    > preloaded-images-k8s-v18-v1...:  337.07 MiB / 337.07 MiB  100.00% 2.24 Mi
    > gcr.io/k8s-minikube/kicbase...:  488.52 MiB / 488.52 MiB  100.00% 2.24 Mi
🔥  Creating docker container (CPUs=2, Memory=3072MB) ...
🐳  Подготавливается Kubernetes v1.34.0 на Docker 28.4.0 ...
🔗  Configuring bridge CNI (Container Networking Interface) ...
🔎  Компоненты Kubernetes проверяются ...
    ▪ Используется образ gcr.io/k8s-minikube/storage-provisioner:v5
🌟  Включенные дополнения: storage-provisioner, default-storageclass
🏄  Готово! kubectl настроен для использования кластера "minikube" и "default" пространства имён по умолчанию
```
- проверяю minicube и k8s кластера
```
ilya@erth ~> minikube status
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured

ilya@erth ~> kubectl get nodes
NAME       STATUS   ROLES           AGE     VERSION
minikube   Ready    control-plane   2m32s   v1.34.0
ilya@erth ~> 
ilya@erth ~> kubectl get services
NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   2m38s
```
- Модифицирую flask.py
- 
