from jose import jwt
from dotenv import load_dotenv
import os


load_dotenv(".env")

public_key_file: str = os.environ.get("PUBLIC_KEY") or ""
private_key_file: str = os.environ.get("PRIVATE_KEY") or ""
algorithm: str = os.environ.get("ALGORITHM") or ""


to_encode = {"toto": "hello"}
print(to_encode)

with open(private_key_file, "r") as f:
    private_key = f.read()

with open(public_key_file, "r") as f:
    public_key = f.read()

encoded_jwt = jwt.encode(to_encode, private_key, algorithm=algorithm)

print(f"here is the encoded token: {encoded_jwt}")

decoded_jwt = jwt.decode(encoded_jwt, public_key, algorithms=[algorithm])
print(f"here is the decoded token: {decoded_jwt}")
