import hashlib


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256str(data: str) -> str:
    return sha256(bytes(data, encoding='utf-8'))
