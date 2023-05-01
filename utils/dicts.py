def get_val(collection, key, default='git'):
    if type(collection) is dict:
        if key in collection:
            return collection[key]
        return default
    return default
