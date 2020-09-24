# Turns a private key into a threshold key. This is NOT a DKG and only for experimental purposes
# Alternatively, this can be used to turn an already existing validator into a secret shared validator;
# however, if the key was compromised before the split happened, it does not help.

from python_ibft.bls_threshold import eval_poly, generate_keys
import sys
import random
import base64
import py_ecc.optimized_bls12_381 as b
from py_ecc.bls.g2_primatives import G1_to_pubkey

if len(sys.argv) != 2:
    print("Usage: python privkey_to_threshold.py {privkey_as_hex}")
    sys.exit(1)

privkey = int(sys.argv[1], base=16)
printable_pubkey = G1_to_pubkey(b.multiply(b.G1, privkey)).hex()
print("Generating threshold keys for validator {0}".format(printable_pubkey))

coefs = [privkey] + [random.randint(0, b.curve_order) for i in range(2)]
privkeys = [eval_poly(x, coefs) for x in range(1,5)]

printable_pubkeys = [G1_to_pubkey(b.multiply(b.G1, p)).hex() for p in privkeys]
printable_privkeys = [base64.encodebytes(p.to_bytes(32, byteorder="big")).decode()[:-1] for p in privkeys]


for i, p in enumerate(zip(printable_pubkeys, printable_privkeys)):
    print("Pubkey {0}:".format(i), p[0])
    print("Privkey {0}:".format(i), p[1])

print()
print("Copy this into validators.json:")
print([{"public_key": printable_pubkey, "threshold_public_keys": printable_pubkeys}])
print()
print("Unencrypted keystores for validator clients:")
print()

for i, p in enumerate(printable_privkeys):
    print("threshold_key_{0}.json".format(i))
    print('{"keys":[{"validator_key":"'+p+'","withdrawal_key":""}]}')
    print()
