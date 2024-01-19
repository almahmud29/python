def list_to_dict():
    keys = [1,2,3]
    values = ["one", "two", "three"]
    result=dict(zip(keys, values))
    print(result)

list_to_dict()