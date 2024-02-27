# free-auth
a free authentication and authorization server


## Generate key pair

```bash
# generate a private key
openssl ecparam -name secp521r1 -genkey -noout -out ec-p512-private.pem

# extract the public key
openssl ec -in ec-p512-private.pem -pubout -out ec-p512-public.pem
```

# start
```bash
uvicorn src.main:app --reload
```
