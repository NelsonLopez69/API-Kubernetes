# Implementation guide
For Ubuntu
1. Clone the [repo](https://github.com/NelsonLopez69/API-Kubernetes.git)
2. Install and configure microk8s
3. Enable [metallb](https://microk8s.io/docs/addon-metallb)
4. Run the DB deployment
5. Run the API deployment

## 1. Clone it

```console
git clone https://github.com/NelsonLopez69/API-Kubernetes.git
```

---
## 2. Install microk8s

Install MicroK8s from the command line:

```console
sudo snap install microk8s --classic
```


Add the user [yourUser] to the 'microk8s' group:
```console
sudo usermod -a -G microk8s [yourUser]
sudo chown -f -R [yourUser] ~/.kube
```
Restart or update de microk8s group
```console
newgrp microk8s
```

## 3. Enable MetalLB

```console
microk8s enable metallb:10.64.140.43-10.64.140.49
```

---

## 4. RUN DB deployment
```console
microk8s kubectl apply -f deployment-db.yml
```

---

## 5. RUN API deployment

```console
microk8s kubectl apply -f deployment-api.yml
```

## Enjoy!

Now you can use the app. Try inserting 10.64.140.44 in your browser.
Routes:
- /
- /health

Example: http://10.64.140.44/health

