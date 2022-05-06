# Code Execution Custom Resource Definition

Az src könyvtárban található konfigurációk betöltése után a következőképpen tesztelhető a CRD eseménykövetése (én archlinux képfájlt használtam hozzá):

```sh
kubectl run --namespace=code-execution --image=archlinux archlinux --command "/bin/sleep" "infinity"
```
```sh
kubectl exec --namespace=code-execution archlinux -- pacman -Syyuu python python-kubernetes --noconfirm
```
```sh
kubectl cp .\test\watch_test.py code-execution/archlinux:/opt
```
```sh
kubectl exec --namespace=code-execution archlinux -- chmod a+x /opt/watch_test.py
```
```sh
kubectl exec --namespace=code-execution archlinux -- sed -i 's/\r//g' /opt/watch_test.py
```
```sh
kubectl exec -i -t --namespace=code-execution archlinux -- /opt/watch_test.py
```