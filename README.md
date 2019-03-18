# utilitron_py_service

A gRPC service for utilitron_py

## Compile lastest protos:
Ensure the [protoc compiler](https://github.com/protocolbuffers/protobuf/releases/tag/v3.7.0) is installed
Install grpcio-tools `pip3 install grpcio-tools`

Compile:
`cd utilitron_py_service`
`git submodule update --remote --merge`
`python3 -m grpc_tools.protoc -I./utilitron_protos/src --python-out=. --grpc_python_out=. ./utilitron_protos/*`
