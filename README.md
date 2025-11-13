# Подюков Илья. ФИТ-2-2024 НМ. Методы и инструменты DevOps. ЛР по лекции 9

- Через pacman устанавливаю minicube и kubectl
- Запускаю kubectl в режиме однонодового кластера k8s
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
- Проверяю minicube и k8s кластера
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
- Модифицирую flask_redis/app.py
- Произвожу сборку образа из исходников внутри minicube
```
ilya@erth ~/Р/vparanoid9 (main)> minikube image build -t flask:v1 flask_redis/

#0 building with "default" instance using docker driver

#1 [internal] load build definition from Dockerfile
#1 transferring dockerfile: 238B done
#1 DONE 0.0s

#2 [internal] load metadata for docker.io/library/python:latest
#2 DONE 3.8s

#3 [internal] load .dockerignore
#3 transferring context: 2B done
#3 DONE 0.0s

#4 [internal] load build context
#4 transferring context: 437B done
#4 DONE 0.0s

#5 [1/5] FROM docker.io/library/python:latest@sha256:e6b1f7011589cc717a5112e6fdb56217e9e734a57e4cb50216e912b068b392a8
#5 resolve docker.io/library/python:latest@sha256:e6b1f7011589cc717a5112e6fdb56217e9e734a57e4cb50216e912b068b392a8 0.0s done
#5 sha256:e6b1f7011589cc717a5112e6fdb56217e9e734a57e4cb50216e912b068b392a8 10.95kB / 10.95kB done
#5 sha256:c4a87c25190f591b29fb62b4ee424ea9907b4a1997357ed47e82d6db98c80b12 2.32kB / 2.32kB done
#5 sha256:e3143549f2b8b3ad8d79efdc47824641c6771796b3770f3c637a38aabd2b3462 0B / 25.62MB 0.1s
...
#5 extracting sha256:2fbf02c04055ee28543076a502ce51fa41895e386e4462739fb1526dc371425e
#5 extracting sha256:2fbf02c04055ee28543076a502ce51fa41895e386e4462739fb1526dc371425e 0.3s done
#5 extracting sha256:149075fcccd1b52406789bff7063813f1c14baf10b165df0e1e00fcb0ca415e5 done
#5 DONE 194.2s

#6 [2/5] WORKDIR /code
#6 DONE 0.0s

#7 [3/5] COPY requirements.txt requirements.txt
#7 DONE 0.0s

#8 [4/5] RUN pip install -r requirements.txt
#8 1.654 Collecting flask (from -r requirements.txt (line 1))
#8 2.073   Downloading flask-3.1.2-py3-none-any.whl.metadata (3.2 kB)
...
#8 5.872 Downloading markupsafe-3.0.3-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (23 kB)
#8 6.110 Downloading werkzeug-3.1.3-py3-none-any.whl (224 kB)
#8 6.143 Installing collected packages: redis, markupsafe, itsdangerous, click, blinker, werkzeug, jinja2, flask
#8 6.647 
#8 6.648 Successfully installed blinker-1.9.0 click-8.3.0 flask-3.1.2 itsdangerous-2.2.0 jinja2-3.1.6 markupsafe-3.0.3 redis-7.0.1 werkzeug-3.1.3
#8 6.648 WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.
#8 7.125 
#8 7.125 [notice] A new release of pip is available: 25.2 -> 25.3
#8 7.125 [notice] To update, run: pip install --upgrade pip
#8 DONE 7.3s

#9 [5/5] COPY app.py .
#9 DONE 0.0s

#10 exporting to image
#10 exporting layers
#10 exporting layers 1.0s done
#10 writing image sha256:4bbbe144c9903f9ce59da689078a800f3c698d11acebe0c926722f35ace9ec04 done
#10 naming to docker.io/library/flask:v1 done
#10 DONE 1.0s
```
- Загружаю готовый образ redis внутрь кластера и проверяю, что образы стали доступны внутри кластера
```
ilya@erth ~/Р/vparanoid9 (main)> minikube image load redis:alpine
ilya@erth ~/Р/vparanoid9 (main)> minikube image ls
registry.k8s.io/pause:3.10.1
registry.k8s.io/kube-scheduler:v1.34.0
registry.k8s.io/kube-proxy:v1.34.0
registry.k8s.io/kube-controller-manager:v1.34.0
registry.k8s.io/kube-apiserver:v1.34.0
registry.k8s.io/etcd:3.6.4-0
registry.k8s.io/coredns/coredns:v1.12.1
gcr.io/k8s-minikube/storage-provisioner:v5
docker.io/library/redis:alpine
docker.io/library/flask:v1
```
- Готовлю манифесты для каждого сервиса и применяю их
```
ilya@erth ~/Р/vparanoid9 (main)> kubectl apply -f flask_redis_k8s/
service/service-devops unchanged
deployment.apps/flask-app created
service/redis unchanged
deployment.apps/redis unchanged
```
- Проверяю статус развёртывания реплик
```
ilya@erth ~/Р/vparanoid9 (main)> kubectl get pods
NAME                         READY   STATUS    RESTARTS   AGE
flask-app-79b8d5d949-276n4   1/1     Running   0          49s
flask-app-79b8d5d949-6r62w   1/1     Running   0          49s
flask-app-79b8d5d949-jr75r   1/1     Running   0          49s
flask-app-79b8d5d949-prnkz   1/1     Running   0          49s
flask-app-79b8d5d949-zj8mr   1/1     Running   0          49s
redis-59bd98c78b-xscfv       1/1     Running   0          3m46s
```
- Проверяю сервисы
```
ilya@erth ~/Р/vparanoid9 (main)> kubectl get services
NAME             TYPE           CLUSTER-IP       EXTERNAL-IP     PORT(S)          AGE
kubernetes       ClusterIP      10.96.0.1        <none>          443/TCP          36m
redis            ClusterIP      10.96.61.3       <none>          6379/TCP         4m23s
service-devops   LoadBalancer   10.102.117.148   10.122.202.66   8000:32066/TCP   3m20s
```
- Обновляю приложение и поды на новую версию - пересобираю образ с тегом v5 и делаю его доступным в minicube
```
ilya@erth ~/Р/vparanoid9 (main)> minikube image build -t flask:v5 flask_redis/
#0 building with "default" instance using docker driver

#1 [internal] load build definition from Dockerfile
#1 transferring dockerfile: 238B done
#1 DONE 0.0s

#2 [internal] load metadata for docker.io/library/python:latest
#2 DONE 2.2s

#3 [internal] load .dockerignore
#3 transferring context: 2B done
#3 DONE 0.0s

#4 [1/5] FROM docker.io/library/python:latest@sha256:e6b1f7011589cc717a5112e6fdb56217e9e734a57e4cb50216e912b068b392a8
#4 DONE 0.0s

#5 [internal] load build context
#5 transferring context: 449B done
#5 DONE 0.0s

#6 [2/5] WORKDIR /code
#6 CACHED

#7 [3/5] COPY requirements.txt requirements.txt
#7 CACHED

#8 [4/5] RUN pip install -r requirements.txt
#8 CACHED

#9 [5/5] COPY app.py .
#9 DONE 0.0s

#10 exporting to image
#10 exporting layers
#10 exporting layers 0.9s done
#10 writing image sha256:65fbca5b70d731cedcdab0bbcbd317dc0a0cd104c68e740e6328d56a4b966b53 done
#10 naming to docker.io/library/flask:v5 done
#10 DONE 0.9s
```
```
ilya@erth ~/Р/vparanoid9 (main)> kubectl set image deployments/flask-app flask=flask:v5
deployment.apps/flask-app image updated
```
```
ilya@erth ~/Р/vparanoid9 (main)> kubectl get pods
NAME                         READY   STATUS    RESTARTS   AGE
flask-app-56959d94d9-kztlx   1/1     Running   0          24s
flask-app-56959d94d9-n4hps   1/1     Running   0          24s
flask-app-56959d94d9-nbc9x   1/1     Running   0          24s
flask-app-56959d94d9-thdlg   1/1     Running   0          24s
flask-app-56959d94d9-tsvsx   1/1     Running   0          24s
redis-59bd98c78b-xscfv       1/1     Running   0          11m
```
```
ilya@erth ~/Р/vparanoid9 (main)> kubectl describe deployment flask-app 
Name:                   flask-app
Namespace:              default
CreationTimestamp:      Thu, 13 Nov 2025 10:06:58 +0500
Labels:                 app=flask-app
Annotations:            deployment.kubernetes.io/revision: 2
Selector:               app=flask-app,svc=front
Replicas:               5 desired | 5 updated | 5 total | 5 available | 0 unavailable
StrategyType:           RollingUpdate
MinReadySeconds:        0
RollingUpdateStrategy:  25% max unavailable, 25% max surge
Pod Template:
  Labels:  app=flask-app
           svc=front
  Containers:
   flask:
    Image:      flask:v5
    Port:       5000/TCP
    Host Port:  0/TCP
    Limits:
      memory:      256Mi
    Environment:   <none>
    Mounts:        <none>
  Volumes:         <none>
  Node-Selectors:  <none>
  Tolerations:     <none>
Conditions:
  Type           Status  Reason
  ----           ------  ------
  Available      True    MinimumReplicasAvailable
  Progressing    True    NewReplicaSetAvailable
OldReplicaSets:  flask-app-79b8d5d949 (0/0 replicas created)
NewReplicaSet:   flask-app-56959d94d9 (5/5 replicas created)
Events:
  Type    Reason             Age    From                   Message
  ----    ------             ----   ----                   -------
  Normal  ScalingReplicaSet  8m42s  deployment-controller  Scaled up replica set flask-app-79b8d5d949 from 0 to 5
  Normal  ScalingReplicaSet  57s    deployment-controller  Scaled up replica set flask-app-56959d94d9 from 0 to 2
  Normal  ScalingReplicaSet  57s    deployment-controller  Scaled down replica set flask-app-79b8d5d949 from 5 to 4
  Normal  ScalingReplicaSet  57s    deployment-controller  Scaled up replica set flask-app-56959d94d9 from 2 to 3
  Normal  ScalingReplicaSet  57s    deployment-controller  Scaled down replica set flask-app-79b8d5d949 from 4 to 3
  Normal  ScalingReplicaSet  57s    deployment-controller  Scaled up replica set flask-app-56959d94d9 from 3 to 4
  Normal  ScalingReplicaSet  57s    deployment-controller  Scaled down replica set flask-app-79b8d5d949 from 3 to 2
  Normal  ScalingReplicaSet  57s    deployment-controller  Scaled up replica set flask-app-56959d94d9 from 4 to 5
  Normal  ScalingReplicaSet  56s    deployment-controller  Scaled down replica set flask-app-79b8d5d949 from 2 to 1
  Normal  ScalingReplicaSet  55s    deployment-controller  (combined from similar events): Scaled down replica set flask-app-79b8d5d949 from 1 to 0
```
```
ilya@erth ~/Р/vparanoid9 (main)> kubectl rollout status deployment flask-app 
deployment "flask-app" successfully rolled out
```
- Пробрасываю порты для запуска
```
ilya@erth ~/Р/vparanoid9 (main)> kubectl port-forward service/service-devops 8000:8000
Forwarding from 127.0.0.1:8000 -> 5000
Forwarding from [::1]:8000 -> 5000
Handling connection for 8000
Handling connection for 8000
```
- Смотрю результат
<img width="915" height="108" alt="изображение" src="https://github.com/user-attachments/assets/b265d8d8-e099-486f-933f-b076c230387d" />
  
