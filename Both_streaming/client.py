# defining streaming client.

import random
import time
from concurrent import futures

import grpc
import ProdInfo_pb2_grpc
import ProdInfo_pb2

def client():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = ProdInfo_pb2_grpc.InfoStub(channel)
        try:
        #defining function for streaming requests
            def multiple_requests_interator():
                while True:
                    product_name = input("Enter name of the product: ")
                    if len(product_name) == 0:
                        break
                    request = ProdInfo_pb2.InfoRequest(name=product_name)
                    yield request
                    time.sleep(0.1)
        except Exception as err:
            print("Failed to send request:\n", err)

        else:
            # Collecting response from server
            responses = stub.MultipleInfo(multiple_requests_interator(),)
            for response in responses:
                print(response)


if __name__ == "__main__":
    try:
        client()
    except Exception as error:
        print("Client is failed to up with error:\n", error)



