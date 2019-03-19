# utilitron_py_service

A gRPC service for utilitron_py

## Compile lastest protos:
Ensure the [protoc compiler](https://github.com/protocolbuffers/protobuf/releases/tag/v3.7.0) is installed
Install grpcio-tools `pip3 install grpcio-tools`

Compile protos:
`cd utilitron_py_service`
`git submodule update --remote --merge`
`python3 -m grpc_tools.protoc -I./utilitron_protos/src --descriptor_set_out=api_descriptor.pb --python_out=. --grpc_python_out=. ./utilitron_protos/src/*`

Deploy endpoints config:
`gcloud endpoints services deploy api_descriptor.pb api_config.yaml`

Deploy to a kubernetes cluster:
`kubectl create -f grpc-utility-py-service.yaml`

View the deployed IP address:
`kubectl get service`
