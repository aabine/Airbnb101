import json
class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
    
    def save(self):
        with open(self.__file_path, "w") as j_file:
            json.dump(self.__objects, j_file)

    def reload(self):
        if self.__file_path:
            try:
                with open(self.__file_path, "r") as j_file:
                    self.__objects = json.load(j_file)
            except FileNotFoundError:
                pass
        
    