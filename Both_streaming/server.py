# crating server file here
import random
from concurrent import futures

import grpc
import ProdInfo_pb2_grpc
import ProdInfo_pb2


class InfoServicer(ProdInfo_pb2_grpc.InfoServicer):

    def MultipleInfo(self, request_interator, context):
        for request in request_interator:
            print(request)

            # Here we are taking random information about the product & sending it to client.
            product_name = request.name
            possible_price_range = range(100, 500)
            possible_name_companies = ["Parle-G", "MRF", "Lenovo", "Micromax"]
            possible_name_country = ["India", "Russia", "Bhutan", "France"]

            product_price = random.choice(possible_price_range)
            product_company = random.choice(possible_name_companies)
            product_country = random.choice(possible_name_country)

            response = ProdInfo_pb2.InfoReply(res_name=product_name,
                                              price=product_price,
                                              company=product_company,
                                              made_in=product_country)
            yield response


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # this server can establish connection with 10 clients.
    ProdInfo_pb2_grpc.add_InfoServicer_to_server(InfoServicer, server)
    server.add_insecure_port("localhost:" + port)
    print(f"The server is up and running on port {port}.")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
