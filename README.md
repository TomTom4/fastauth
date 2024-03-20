# FastAuth
a free authentication and authorization server, based on FastApi, SQLModel and jwcrypto.

## Install locally
 Here below you
will find basic guidelines to install it on your system, and be able to play with it.

### clone
This project being in its early stage, It is only available through git :/
At some point I would like to distribute it through a docker image and/or as a 
python package. But so far, you need to clone it, like so:

```bash
git clone git@github.com:TomTom4/fastauth.git
cd fastauth
```

### setup
please consider using a virtualenv, and then install all the required dependencies 
necessary for this project to work. Here an example:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Generate key pair
for the authentication process to work, you need a pair of public and private keys, that
would be use to respectively verify and sign your tokens.

```bash
# generate a private key
openssl ecparam -name secp521r1 -genkey -noout -out private.pem

# extract the public key
openssl ec -in private.pem -pubout -out public.pem
```

### setup .env
For convenience, I provided a simple env-sample that is preconfigured with all the basic
values. However, This will be your go to if you would like to customize your 
configurations.

```bash
cp env-sample .env
```

## launch it 
To launch the server, make sure that you have followed the installation process described
above, and that your virtual environment is activated.
then just do:

```bash
uvicorn src.main:app --reload
```

## launch tests
```bash
pytest
```
