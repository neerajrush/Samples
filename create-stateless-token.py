import jwt
import datetime
import hashlib

method = 'GET'
uri = '/volumes'
secret = 'KMaubYnG/SjosCECvuImDLkrR0FIgZT4Xw7ei9WXIpw='

claims = {}

# Issuer
claims['iss'] = 'admin'

# Issued at time
claims['iat'] = datetime.datetime.utcnow()

# Expiration time
claims['exp'] = datetime.datetime.utcnow() \
	+ datetime.timedelta(minutes=10)

# URI tampering protection
claims['qsh'] = hashlib.sha256((method + '&' + uri).encode('utf-8')).hexdigest()

print(jwt.encode(claims, secret, algorithm='HS256'))
