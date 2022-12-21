***Kubernetes manifests***

___

#### MinIO

In order to run this project, the open-source object storage software *MinIO* might be required.

(*alternative*) Otherwise you can also use the server as a file store.

Before running submitting the manifest to your cluster please modify the following env. variables within [minio-standalone.yaml](minio-standalone.yaml) :
```yaml
...
        env:
        # Minio access key and secret key
        - name: MINIO_ACCESS_KEY
          value: "<TODO>"
        - name: MINIO_SECRET_KEY
          value: "<TODO>"
...
```


#### MLflow

Same as the manifest for [MinIO](#minio), please modify the following env. variables within [k8s-mlflow.yaml](k8s-mlflow.yaml) :

```yaml
...
        env:
        - name: MLFLOW_S3_ENDPOINT_URL
          value: "<TODO>"
        - name: AWS_ACCESS_KEY_ID
          value: "<TODO>"
        - name: AWS_SECRET_ACCESS_KEY
          value: "<TODO>"
          # http://localhost:500 or something else
        - name: MLFLOW_TRACKING_URI
          value: "<TODO>"
...
```

