import cmd
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

    def do_create(self, obj):
        obj = BaseModel()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
