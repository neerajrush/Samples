import grpc
import KV_Store_pb2
import KV_Store_pb2_grpc
import sys

def get_key_query_from_service(kv_store_service, kv_store_query):
	return kv_store_service.Get(kv_store_query)

def set_key_value_pair_in_service(kv_store_service, kv_pair_info):
	return kv_store_service.Set(kv_pair_info)

def input_key_info(kv_store_query):
	while kv_store_query.key == "":
		kv_store_query.key = input("Enter Key: ")

def input_key_pair_info(kv_store_query):
	while kv_store_query.key == "":
		kv_store_query.key = input("Enter Key: ")
		kv_store_query.value = input("Enter Value: ")

if __name__ == "__main__":
	print("Running KV Store Client:")
	channel = grpc.insecure_channel('localhost:50051')
	kv_store_service = KV_Store_pb2_grpc.KV_Store_ServiceStub(channel)
	if kv_store_service is not None:
		print("Client is successfully connected to the KV service.")
		while True:
			kvInput = input("GET or SET: ")
			if kvInput == "GET":
				kv_store_query = KV_Store_pb2.KV_query()
				input_key_info(kv_store_query)
				print(kv_store_query)
				kv_pair = get_key_query_from_service(kv_store_service, kv_store_query)
				print(kv_pair)
			
			elif kvInput == "SET":
				kv_pair_info = KV_Store_pb2.KV_pair()
				input_key_pair_info(kv_pair_info)
				print(kv_pair_info)
				KV_op_result = set_key_value_pair_in_service(kv_store_service, kv_pair_info)
				print(KV_op_result)
				print("..... Done settting KV pair.")
			elif kvInput == "q":
				print("Quit.")
				break
			else:
				print("Invalid message type. try again.")
	else:
		print("Client is failed to connect to the KV Store.")
