import json


def simple_output(dict_out):
    """Returns the input entry, without any further modification

    Args:
        dict_out (dict): A dictionary to be converted to JSON

    Returns:
        string: a JSON string
    """
    del dict_out['_id']
    return json.dumps(dict_out)
