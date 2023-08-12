import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage

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
        """Create a new instance of BaseModel and save it to yhe JSON file"""
        if not arg:
            print("** class name missing **")
        try:
            new_class = eval(arg+"()")
        except NameError:
            print("** class doesn't exit **")
            return
        new_class.save()
        print(new_class.id)

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

    def do_destroy(self, args):
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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
