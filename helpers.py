import hashlib


def sha256sum(filename):
    """SHA256 File Checksum"""

    with open(filename, 'rb', buffering=0) as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()
