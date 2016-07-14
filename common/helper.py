def convert_to_bool(literal):
    a = {'True': True, 'False': False, 'true':True, 'false':False}
    return a[literal]

def select_from_list_if_true(list):
    return [x for x in list if x]




