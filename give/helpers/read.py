def read(file_name: str) -> list[str]:
    file = open(file_name, 'r')
    return [line.strip() for line in file.readlines() if line.strip()]
