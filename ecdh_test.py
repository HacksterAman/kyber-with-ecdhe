import ecdh

# A
private_key_A, public_key_A = ecdh.keygen() # Key Generation

# B
private_key_B, public_key_B = ecdh.keygen() # Key Generation

# Public Key Exchange

# A: private_key_A, public_key_B
shared_secret_A = ecdh.derive_shared_secret(private_key_A, public_key_B) # Shared Secret Derivation

# B: private_key_B, public_key_A
shared_secret_B = ecdh.derive_shared_secret(private_key_B, public_key_A) # Shared Secret Derivation

print(shared_secret_A == shared_secret_B)