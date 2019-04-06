import json
import ast
import sys

# class Jsonable:
#     def to_json(self, indent=4):
#         d = {str(type(self).__name__) : self.__dict__}
#         return str(json.dumps(d, indent = 4, sort_keys=True))

#     @classmethod
#     def fromStrToClass(cls, class_name, arguments):
#         class_ = getattr(sys.modules[__name__], class_name)
#         instance = class_(**arguments)
#         return instance

#     @classmethod
#     def from_json(cls, json_string):
#         dic = ast.literal_eval(json_string)
#         obj_type = next(iter(dic))
#         return cls.fromStrToClass(obj_type, dic[obj_type])

class Jsonable:
    def to_json(self, indent=4):
        d = {str(type(self).__name__) : self.__dict__}
        return str(json.dumps(d, indent = 4, sort_keys=True))

    @classmethod
    def from_json(cls, json_string):
        dic = json.loads(json_string)
        return cls(**dic[cls.__name__])

import dicttoxml
class Xmlable:
    def to_xml(self):
        return dicttoxml.dicttoxml(self.__dict__)
    
    @classmethod
    def from_xml(cls, xml_string):
        pass

class Panda(Jsonable, Xmlable):
    def __init__(self, name, age):
        self.name = name
        self.age = age

def main():
    p = Panda('Preslava', 19)
    print(p.to_json())
    p2 = Panda.from_json(p.to_json())
    print(p2.name)
    print(p.to_xml())

if __name__ == '__main__':
    main()