import grpc
import KV_Store_pb2
import KV_Store_pb2_grpc
import sys
from concurrent import futures
import time

_ONE_DAY_IN_SECONDS = 30

KV_STORE = { }

class KV_Store_Service(KV_Store_pb2_grpc.KV_Store_ServiceServicer):
	def Get(self, request, context):
		kv_pair = KV_Store_pb2.KV_pair()
		kv_pair.key = request.key
		print("INFO: look up in KV Store: ", request.key)
		if request.key not in KV_STORE:
			return kv_pair
		kv_pair.value = KV_STORE[request.key]
		return kv_pair

	def Set(self, request, context):
		kv_op_result = KV_Store_pb2.KV_op_result()
		print("INFO: set in KV Store: ", request)
		KV_STORE[request.key] = request.value

		kv_op_result.ok = True

		return kv_op_result

def run_server():
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
	KV_Store_pb2_grpc.add_KV_Store_ServiceServicer_to_server(KV_Store_Service(), server)
	server.add_insecure_port('[::]:9001')
	server.start()
	try:
		while True:
			time.sleep(_ONE_DAY_IN_SECONDS)
	except KeyboardInterrupt:
		server.stop(0)

if __name__ == "__main__":
	print("Running Server ==> plugging KV_Store Service:")
	run_server()
