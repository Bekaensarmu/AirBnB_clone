#!/usr/bin/python3
import cmd
import json
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class ALXCommand(cmd.Cmd):
    """
    This class represents the command line interface for ALX project.
    """
    prompt = '(hbnb) '
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_quit(self, arg):
        """
        Exit the command line.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the command line when using CTRL+D.
        """
        print("")
        return True

    def emptyline(self):
        """
        Override the behavior of an empty line.
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of a class.
        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)
        if args[0] not in ALXCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = ALXCommand.classes[args[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Show the string representation of an instance.
        Usage: show <class name> <id>
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in ALXCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) <= 1:
            print("** instance id missing **")
            return
        storage.reload()
        objs_dict = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key in objs_dict:
            obj_instance = str(objs_dict[key])
            print(obj_instance)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Destroy an instance based on the class name and id.
        Usage: destroy <class name> <id>
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in ALXCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) <= 1:
            print("** instance id missing **")
            return
        storage.reload()
        objs_dict = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key in objs_dict:
            del objs_dict[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Print all string representations of instances.
        Usage: all [<class name>]
        """
        storage.reload()
        objects_json = []
        objs_dict = storage.all()
        if not arg:
            for key in objs_dict:
                objects_json.append(str(objs_dict[key]))
            print(json.dumps(objects_json)
            return
        args = shlex.split(arg)
        if args[0] in ALXCommand.classes:
            for key in objs_dict:
                if args[0] in key:
                    objects_json.append(str(objs_dict[key]))
            print(json.dumps(objects_json))
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Update an instance based on the class name and id.
        Usage: update <class name> <id> <attribute name> <attribute value>
        """
        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)
        storage.reload()
        objs_dict = storage.all()
        if args[0] not in ALXCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        try:
            key = "{}.{}".format(args[0], args[1])
            objs_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        obj_instance = objs_dict[key]
        if hasattr(obj_instance, args[2]):
            attr_type = type(getattr(obj_instance, args[2]))
            setattr(obj_instance, args[2], attr_type(args[3]))
        else:
            setattr(obj_instance, args[2], args[3])
        storage.save()

    def do_count(self, arg):
        """
        Count the number of instances of a class.
        Usage: count <class name>
        """
        counter = 0
        objs_dict = storage.all()
        for key in objs_dict:
            if (arg in key):
                counter += 1
        print(counter)

    def default(self, arg):
        """
        Handle new ways of inputting data.
        """
        val_dict = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update
        }
        arg = arg.strip()
        values = arg.split(".")
        if len(values) != 2:
            cmd.Cmd.default(self, arg)
            return
        class_name = values[0]
        command = values[1].split("(")[0]
        line = ""
        if (command == "update" and values[1].split("(")[1][-2] == "}"):
            inputs = values[1].split("(")[1].split(",", 1)
            inputs[0] = shlex.split(inputs[0])[0]
            line = "".join(inputs)[0:-1]
            line = "{} {}".format(class_name, line)
            self.do_update2(line.strip())
            return
        try:
            inputs = values[1].split("(")[1].split(",")
            for num in range(len(inputs)):
                if (num != len(inputs) - 1):
                    line = "{} {}".format(line, shlex.split(inputs[num])[0])
                else:
                    line = "{} {}".format(line, shlex.split(inputs[num][0:-1])[0])
        except IndexError:
            inputs = ""
            line = ""
        line = "{} {}".format(class_name, line)
        if (command in val_dict):
            val_dict[command](line.strip())

if __name__ == '__main__':
    ALXCommand().cmdloop()
