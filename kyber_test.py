from kyber import Kyber1024

def server2client():

    # server
    public_key_server, secret_key_server = Kyber1024.keygen() # Key Generation

    # Public Key Exchange: server -> client

    # client: public_key_server
    cipher_client, shared_secret_client = Kyber1024.enc(public_key_server) # Key Encapsulation

    # Cipher Exchange: client -> server

    # server: secret_key_server, public_key_client, key_server, cipher_client
    _shared_secret_client = Kyber1024.dec(cipher_client, secret_key_server) # Key Dencapsulation

    print(shared_secret_client == _shared_secret_client)

def client2server():

    # Client
    public_key_client, secret_key_client = Kyber1024.keygen() # Key Generation

    # Public Key Exchange: client -> server

    # Server: public_key_client
    cipher_server, shared_secret_server = Kyber1024.enc(public_key_client) # Key Encapsulation

    # Cipher Exchange: server -> client

    # Client: secret_key_client, public_key_server, key_client, cipher_server
    _shared_secret_server = Kyber1024.dec(cipher_server, secret_key_client) # Key Dencapsulation

    print(shared_secret_server == _shared_secret_server)

def twoWay():

    # A
    public_key_A, secret_key_A = Kyber1024.keygen() # Key Generation

    # B
    public_key_B, secret_key_B = Kyber1024.keygen() # Key Generation

    # Public Key Exchange

    # A: secret_key_A, public_key_B
    cipher_A, shared_secret_A = Kyber1024.enc(public_key_B) # Key Encapsulation

    # B: secret_key_B, public_key_A
    cipher_B, shared_secret_B = Kyber1024.enc(public_key_A) # Key Encapsulation

    # Cipher Exchange

    # A: secret_key_A, public_key_B, shared_secret_A, cipher_B
    _shared_secret_B = Kyber1024.dec(cipher_B, secret_key_A) # Key Dencapsulation

    # B: secret_key_B, public_key_A, shared_secret_B, cipher_A
    _shared_secret_A = Kyber1024.dec(cipher_A, secret_key_B) # Key Dencapsulation

    print(shared_secret_A == _shared_secret_A and shared_secret_B == _shared_secret_B)
    print(shared_secret_A + _shared_secret_B == _shared_secret_A + shared_secret_B)

server2client()
client2server()
twoWay()