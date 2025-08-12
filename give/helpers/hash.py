import hashlib

BUFF_SIZE = 64_000

def hash_line(line: str) -> str:
    md5 = hashlib.md5()
    i = 0

    while i < len(line):
        md5.update(line[i:i+BUFF_SIZE].encode('ascii'))
        i += BUFF_SIZE
    
    return md5.hexdigest()

def hash_file(file_name: str) -> str:
    md5 = hashlib.md5()

    with open(file_name, 'rb') as f:
        while True:
            data = f.read(BUFF_SIZE)
            if not data:
                break
            md5.update(data)

    return md5.hexdigest()
