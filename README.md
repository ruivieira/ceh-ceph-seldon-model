# ceh-ceph-seldon-model

## Building

Build the model using the `s2i` as:

```shell
$ s2i build . \
  seldonio/seldon-core-s2i-python36:0.18 \
  ruivieira/ceh-ceph-seldon-model
```

## Running locally

If have an S3 bucket `data` containing a model `uploaded/model.pkl` you can run the model locally using:

```shell
$ docker run -i --rm \
    -e S3_ENDPOINT_URL=<S3_ENDPOINT> \
    -e AWS_ACCESS_KEY_ID=<ACESS_KEY> \
    -e AWS_SECRET_ACCESS_KEY=<SECRET_ACESS> \
    -p 5000:5000 ruivieira/ceh-ceph-seldon-model
```

To test a prediction, run:

```shell
curl --header "Content-Type: application/json" \
     --request POST \
     --data '{"data":{"ndarray":[[100.0, 1, 2]]}}' \
     http://localhost:5000/predict
```

## Deploy on OpenShift

A standalone server can be deploying using:

```shell
$ oc new-app ruivieira/ceh-ceph-seldon-model \
     -e S3_ENDPOINT_URL=<S3_ENDPOINT> \
     -e AWS_ACCESS_KEY_ID=<ACESS_KEY> \
     -e AWS_SECRET_ACCESS_KEY=<SECRET_ACESS>
```
