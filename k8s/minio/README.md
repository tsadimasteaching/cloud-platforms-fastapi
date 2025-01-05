## add helm repo

```bash
helm repo add minio https://charts.min.io/
```

```bash
 helm install myminio minio/minio --namespace minio --create-namespace -f minio-values.yaml
```