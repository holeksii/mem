def find(source: list, finder: list) -> int:
    for i in range(len(source)):
        if source[i:i+len(finder)] == finder:
            return i
    return -1

def replace(source: list, finder: list, replacer: list) -> list:
    index = find(source, finder)
    if index == -1:
        raise ValueError('Cannot find the list in the source')
    return source[:index] + replacer + source[index + len(finder):]
