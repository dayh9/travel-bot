"""Extract nested values from a JSON tree."""


def json_extract(obj, key, is_list=False):
    """Recursively fetch values from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            if is_list:
                arr.append(obj)
            else:
                for item in obj:
                    extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    if len(values):
        return values[0]
    return None
