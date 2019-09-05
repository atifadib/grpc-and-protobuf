import grpc
import sys
# import the generated classes
import calculator_pb2
import calculator_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = calculator_pb2_grpc.CalculatorStub(channel)

# create a valid request message
try:
	number = calculator_pb2.Number(value=float(sys.argv[1]))
except Exception as e:
	print("Exception occurred while GRPC call: "+str(e))

# make the call
response = stub.SquareRoot(number)

# et voilà
print(response.value)
