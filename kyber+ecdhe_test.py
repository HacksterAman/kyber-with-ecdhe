from kyber import Kyber1024
import ecdh

# In this example I have implimented Two Way Approch for Kyber

# A
kyber_public_key_A, kyber_secret_key_A = Kyber1024.keygen() # Kyber Key Generation
ecdh_private_key_A, ecdh_public_key_A = ecdh.keygen() # ECDH Key Generation

# B
kyber_public_key_B, kyber_secret_key_B = Kyber1024.keygen() # Kyber Key Generation
ecdh_private_key_B, ecdh_public_key_B = ecdh.keygen() # ECDH Key Generation

# Public Key Exchange

# A: kyber_secret_key_A, kyber_public_key_B, ecdh_private_key_A, ecdh_public_key_B
cipher_A, kyber_shared_secret_A = Kyber1024.enc(kyber_public_key_B) # Key Encapsulation
ecdh_shared_secret_A = ecdh.derive_shared_secret(ecdh_private_key_A, ecdh_public_key_B) # Shared Secret Derivation

# B: kyber_secret_key_B, kyber_public_key_A, ecdh_private_key_B, ecdh_public_key_A
cipher_B, kyber_shared_secret_B = Kyber1024.enc(kyber_public_key_A) # Key Encapsulation
ecdh_shared_secret_B = ecdh.derive_shared_secret(ecdh_private_key_B, ecdh_public_key_A) # Shared Secret Derivation

# Cipher Exchange

# A: kyber_secret_key_A, kyber_shared_secret_A, cipher_B, ecdh_shared_secret_A
_kyber_shared_secret_B = Kyber1024.dec(cipher_B, kyber_secret_key_A) # Key Dencapsulation
final_key_A = kyber_shared_secret_A + _kyber_shared_secret_B + ecdh_shared_secret_A # Final Key Combination

# B: kyber_secret_key_B, kyber_shared_secret_B, cipher_A, ecdh_shared_secret_B
_kyber_shared_secret_A = Kyber1024.dec(cipher_A, kyber_secret_key_B) # Key Dencapsulation
final_key_B = _kyber_shared_secret_A + kyber_shared_secret_B + ecdh_shared_secret_B  # Final Key Combination

print(kyber_shared_secret_A == _kyber_shared_secret_A and kyber_shared_secret_B == _kyber_shared_secret_B)
print(final_key_A == final_key_B)