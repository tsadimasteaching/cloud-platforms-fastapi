## add helm repo

```bash
helm repo add minio https://charts.min.io/
```

```bash
 helm install myminio minio/minio --namespace minio --create-namespace -f minio-values.yaml
```


https://github.com/minio/console/issues/3262
https://min.io/docs/minio/linux/operations/external-iam/configure-keycloak-identity-management.html
https://blog.min.io/integrate-minio-with-keycloak-oidc/?hss_channel=lcp-6442270
https://github.com/minio/minio/blob/master/helm/minio/values.yaml

* create a client for minio
* create client scope ``minio-authorization`` and create mapper ``minio-policy-mapper``
* assign this client scope to client with default assign type
* create group ``minio-users`` and add policy attribute
* assign this group to user