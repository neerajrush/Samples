import grpc
#import helloworld_pb2


#channel = grpc.insecure_channel('localhost:50051')

#creds = grpc.ssl_channel_credentials(open('roots.pem').read())
#channel = grpc.secure_channel('myservice.example.com:443', creds)

from google import auth as google_auth
from google.auth.transport import grpc as google_auth_transport_grpc
from google.auth.transport import requests as google_auth_transport_requests

credentials, _ = google_auth.default(scopes=(scope,))

request = google_auth_transport_requests.Request()

channel = google_auth_transport_grpc.secure_authorized_channel(
              credentials, request, 'greeter.googleapis.com:443')
