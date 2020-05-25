import hashlib
import datetime

def hash_code(str, str_salt):
    hash_algorithm = hashlib.sha256()
    str += str_salt
    hash_algorithm.update(str.encode())

    return hash_algorithm.hexdigest()