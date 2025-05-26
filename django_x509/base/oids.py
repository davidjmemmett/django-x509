from cryptography.hazmat.bindings._rust import ObjectIdentifier
from cryptography.hazmat._oid import ExtensionOID

class NetscapeOID:
    CERT_TYPE = ObjectIdentifier('2.16.840.1.113730.1.1')

KNOWN_OIDS = {
    'nsCertType': NetscapeOID.CERT_TYPE,
}
