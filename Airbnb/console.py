import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Exit the program"""
        return True

    def do_EOF(self, line):
        """Exit the program on EOF (Ctrl+D)"""
        return True

    def do_help(self, arg: str):
        """Displays help documentation"""
        print("Custom help message for HBNBCommand:")
        print("- quit: Exit the program")
        print("- EOF: Exit the program on EOF (Ctrl+D)")

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of a class and save it to the JSON file"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        class_name = arg.split()[0]
        
        try:
            class_module = globals()[class_name]
        except KeyError:
            print("** class doesn't exist **")
            return
        
        new_instance = class_module()
        new_instance.save()
        print(new_instance.id)



    def do_show(self, line):
        """Show the string representation of an instance"""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exit **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_id = "{}.{}".format(args[0], args[1])
            all_objs = storage.all()
            if obj_id in all_objs:
                print(all_objs[obj_id])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Delete an instance base on class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exit **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_id = "{}.{}".format(args[0], args[1])
            all_objs = storage.all()
            if obj_id in all_objs:
               del all_objs[obj_id]
               storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """Prints string representation of all instances based on class name"""
        objects = storage.all().values()

        if args:
            try:
                filtered_objects = [str(obj) for obj in objects if type(obj).__name__ == args]
                if not filtered_objects:
                    print("** class doesn't exist **")
                    return
                print(filtered_objects)
            except NameError:
                pass
        else:
            result = [str(obj) for obj in objects]
            print(result)

    # def do_update(self, arg):
    #     '''Updates an instance of a class in the JSON file'''
    #     args = arg.split()
    #     if len(args) == 0:
    #         print("** class name missing **")
    #         return

    #     cls_name = args[0]
    #     if cls_name != "BaseModel":
    #         print("** class doesn't exist **")
    #         return

    #     if len(args) < 2:
    #         print("** instance id missing **")
    #         return

    #     clsa = BaseModel
    #     all_ids = [obj.id for obj in storage.all().values() if isinstance(obj, clsa)]
    #     obj_id = args[1]
    #     if obj_id not in all_ids:
    #         print("** no instance found **")
    #         return

    #     if len(args) < 3:
    #         print("** attribute name missing **")
    #         return

    #     attr_name = args[2]
    #     if attr_name in ["id", "created_at", "updated_at"]:
    #         print("cannot update id, created_at or updated_at")
    #         return

    #     if len(args) < 4:
    #         print("** value missing **")
    #         return

    #     value = args[3]
    #     obj = storage.get(cls_name, obj_id)
    #     setattr(obj, attr_name, value)
    #     obj.save()

    def do_update(self, args):
        data = storage.all()
        arg = args.split()

        if arg[0] in data and arg[1] in data[arg[0]]:
            instance = data[arg[0]][arg[1]]

            if arg[2] in instance:
                instance 



if __name__ == "__main__":
    HBNBCommand().cmdloop()
