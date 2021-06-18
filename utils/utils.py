import base64


def get_base64_encoded_string(string):
    result = base64.b64encode(string.encode()).decode()
    return result
