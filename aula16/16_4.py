import json

def main():
    data = [
        {'time': 1394984189, 'name': 'cpu', 'value': 12},
        {'time': 1394984190, 'name' :'cpu', 'value': 19}
        [
            {'key1':123,'key2':'abc','key3':78},
            {'key1':456,'key2':'def','key3':90}
        ]
    ]
    print(json.dumps(data,indent=4))

main()