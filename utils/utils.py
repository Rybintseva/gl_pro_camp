import base64


def base64_encode(string):
    result = base64.b64encode(string.encode()).decode()
    return result


def base64_encode_header(username, password):
    headers = {"Authorization": f"Basic {base64_encode(f'{username}:{password}')}"}
    return headers
