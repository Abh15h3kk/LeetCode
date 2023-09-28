def firstRepeatChar(str):
    visited = {}
    for ch in str:
        if ch in visited:
            return ch
        else:
            visited[ch] = True
    return False
