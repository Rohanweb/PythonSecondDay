
#Command to Install Python ProtoBuf library
pip install grpcio-tools 

#Command to Generate Stub (Python Stub) for ProtoBuf contract

python -m grpc.tools.protoc -I<grpc library path| usually .> --python_out=<path of stub generation> --grpc_python_out=<path of grpc stub> simple.proto

