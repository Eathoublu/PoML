import hashlib


def hash256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def hash256str(data: str) -> str:
    return hash256(bytes(data, encoding='utf-8'))
