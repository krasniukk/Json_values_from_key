"""This module returns all the values found
from given key.
"""

import jmespath
import json
import pprint

def json_loader(path: str) -> dict:
    """Writes json to dict.
    """

    with open(path, 'r') as file:

        info = json.load(file)

    return info

def find_keys(info: dict) -> dict:
    """Determines all the keys and their parent keys.
    """

    avail_keys = {}

    def if_dict(dct: dict, prev_key: str):

        for key in dct.keys():

            if key not in avail_keys:
                    avail_keys[key] = prev_key

    
            if type(dct[key]) == dict:
                if_dict(dct[key], key + '[].')

            elif type(dct[key]) == list:

                for item in dct[key]:

                    if type(item) == dict:
                        if_dict(item, key + '[].')

    if_dict(info, '')
    # print(avail_keys)

    return avail_keys

def ask_for_key_show_value(path: str):
    """Asks to input a key and shows all the values form the key.
    """

    info = json_loader(path)
    keys_data = find_keys(info)
    print('Keys form json:', keys_data.keys())
    key_requested = input('Key:')
    
    print('Values form all keys named "', key_requested, '"')
    pprint.pprint(jmespath.search('{}{}'.format(keys_data[key_requested], key_requested), info))
    # print('{}'.format(info))
