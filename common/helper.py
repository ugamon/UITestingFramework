# encoding=utf-8
def convert_to_bool(literal):
    return {'True': True, 'False': False, 'true': True, 'false': False}[literal]

def select_from_list_if_true(list):
    return [x for x in list if x]

def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

def convert_to_unicode(string):
    return unicode(string, 'utf-8')



