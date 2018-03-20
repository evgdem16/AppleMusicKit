
import datetime
import jwt

secret = """-----BEGIN PRIVATE KEY-----
MIGTAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBHkwdwIBAQQgl1srjSMdIM0vhMRkUdJtez+ZuF7DWwFM6ywO3H3DOP+gCgYIKoZIzj0DAQehRANCAARG9omiRqGKQDIjeLd86gOr4NQZPOdu5B5fdb5nhGBNhftNRbkQj6PGPIAGvtIpzXAB9lN3T8XTIUaBP6tGh2Vo
-----END PRIVATE KEY-----"""
keyId = "M272TB4D9S"
teamId = "J2G5P8NJGW"
alg = 'ES256'

time_now = datetime.datetime.now()
time_expired = datetime.datetime.now() + datetime.timedelta(hours=12)

headers = {
	"alg": alg,
	"kid": keyId
}

payload = {
	"iss": teamId,
	"exp": int(time_expired.strftime("%s")),
	"iat": int(time_now.strftime("%s"))
}

if __name__ == "__main__":
	"""Create an auth token"""
	token = jwt.encode(payload, secret, algorithm=alg, headers=headers)

	print "----TOKEN----"
	print token

	print "----CURL----"
	print "curl -v -H 'Authorization: Bearer %s' \"https://api.music.apple.com/v1/catalog/us/artists/36954\" " % (token)
