import grpc
from protofiles import calc_pb2, calc_pb2_grpc


# Step 1: Create a Channel
channel = grpc.insecure_channel('localhost:50051')

# Step 2: Create a Stub
stub = calc_pb2_grpc.CalculatorStub(channel)

# Step 3: call API
number = calc_pb2.Number(value=16)
response = stub.SquareRoot(number)
print(response.value)