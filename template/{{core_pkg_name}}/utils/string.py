def smart_str(o) -> str:
    if isinstance(o, str):
        return o
    elif isinstance(o, bytes):
        return o.decode('utf-8')
    else:
        return str(o)
