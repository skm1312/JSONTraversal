import json

file = "myfile_1.json"
data = {}
with open(file, 'r') as f:
    data = json.load(f)
    
def create_traverse_list(user_input):
    traverse_list = user_input.split('/')
    return traverse_list
    
def extract_value(dict_obj, traverse_list):
    if len(traverse_list) == 0:
        return str(list(dict_obj.keys()))[1:-1]
    else:
        key = traverse_list[0]
        del traverse_list[0]
        if key in dict_obj:
            if type(dict_obj[key]) == dict:
                return extract_value(dict_obj[key], traverse_list)
            elif type(dict_obj[key]) == list:
                if len(traverse_list) == 0:
                    return str(dict_obj[key])[1:-1]
                else:
                    if traverse_list[0] in dict_obj[key]:
                        return "Available"
                    else:
                        return "Not Available"
        else:
            print("Not available")
            
traverse_list = create_traverse_list(input("Input: "))
result = extract_value(data, traverse_list)
print(result)