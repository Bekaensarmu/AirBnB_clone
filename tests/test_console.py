#!/usr/bin/python3
"""Unit test for the file storage class
"""
import unittest
import pep8
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.engine.file_storage import FileStorage
import os

class TestConsoleClass(unittest.TestCase):
    """TestConsoleClass resume
    Args:
        unittest (): Properties for unit testing
    """

    maxDiff = None

    def setUp(self):
        """Condition to test file saving"""
        with open("test.json", 'w'):
            FileStorage._FileStorage__file_path = "test.json"
            FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Destroys the created file"""
        FileStorage._FileStorage__file_path = "file.json"
        try:
            os.remove("test.json")
        except FileNotFoundError:
            pass

    def test_module_doc(self):
        """Check for module documentation"""
        self.assertTrue(len(HBNBCommand.__doc__) > 0)

    def test_class_doc(self):
        """Check for documentation"""
        self.assertTrue(len(HBNBCommand.__doc__) > 0)

    def test_method_docs(self):
        """Check for method documentation"""
        for method_name in dir(HBNBCommand):
            method = getattr(HBNBCommand, method_name)
            self.assertTrue(len(method.__doc__) > 0)

    def test_pep8(self):
        """Test base and test_base for PEP8 conformance"""
        style = pep8.StyleGuide(quiet=True)
        file1 = 'console.py'
        file2 = 'tests/test_console.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")

    def test_executable_file(self):
        """Check if the file has permissions to execute"""
        # Check for read access
        is_read_true = os.access('console.py', os.R_OK)
        self.assertTrue(is_read_true)
        # Check for write access
        is_write_true = os.access('console.py', os.W_OK)
        self.assertTrue(is_write_true)
        # Check for execution access
        is_exec_true = os.access('console.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_check_help(self):
        """Verifies that each command has help output"""
        with patch('sys.stdout', new=StringIO()) as help_val:
            HBNBCommand().onecmd("help create")
            self.assertTrue(len(help_val.getvalue()) > 0)
        with patch('sys.stdout', new=StringIO()) as help_val:
            HBNBCommand().onecmd("help all")
            self.assertTrue(len(help_val.getvalue()) > 0)
        with patch('sys.stdout', new=StringIO()) as help_val:
            HBNBCommand().onecmd("help show")
            self.assertTrue(len(help_val.getvalue()) > 0)
        with patch('sys.stdout', new=StringIO()) as help_val:
            HBNBCommand().onecmd("help destroy")
            self.assertTrue(len(help_val.getvalue()) > 0)
        with patch('sys.stdout', new=StringIO()) as help_val:
            HBNBCommand().onecmd("help update")
            self.assertTrue(len(help_val.getvalue()) > 0)

    def test_create_good(self):
        """Test the create function"""
        with patch('sys.stdout', new=StringIO()) as help_val:
            HBNBCommand().onecmd("create BaseModel")
            self.assertTrue(len(help_val.getvalue()) > 0)

    def test_create_empty(self):
        """Test the create function"""
        with patch('sys.stdout', new=StringIO()) as help_val:
            HBNBCommand().onecmd("create")
            self.assertEqual(help_val.getvalue(), "** class name missing **\n")

    def test_create_unknown(self):
        """Test the create function"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create Holberton")
            self.assertEqual(val.getvalue(), "** class doesn't exist **\n")

    def test_show(self):
        """Test show with normal parameters"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
            basemodel_id = val.getvalue()
            self.assertTrue(len(basemodel_id) > 0)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('show BaseModel ' + basemodel_id)
            self.assertTrue(val.getvalue() != "** no instance found **\n")

    def test_show_notfound(self):
        """Test with class that does not exist"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('show helloo ')
            self.assertTrue(val.getvalue() == "** class doesn't exist **\n")

    def test_show_empty(self):
        """Test with class missing"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('show')
            self.assertTrue(val.getvalue() == "** class name missing **\n")

    def test_show_id(self):
        """Test with id missing"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('show BaseModel')
            self.assertTrue(val.getvalue() == "** instance id missing **\n")

    def test_destroy_empty(self):
        """Check if class is missing"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('destroy')
            self.assertTrue(val.getvalue() == "** class name missing **\n")

    def test_destroy_wrong(self):
        """Check if class name does not exist"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('destroy fakeclass')
            self.assertTrue(val.getvalue() == "** class doesn't exist **\n")

    def test_destroy_id(self):
        """Check if the id is missing"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('destroy BaseModel')
            self.assertTrue(val.getvalue() == "** instance id missing **\n")

    def test_destroy_notfound(self):
        """Check if the id belongs to an instance"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('destroy BaseModel 121212')
            self.assertTrue(val.getvalue() == "** no instance found **\n")

    def destroy_working(self):
        """Check if the destroy method deletes an instance successfully"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
            basemodel_id = val.getvalue()
            self.assertTrue(len(basemodel_id) > 0)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('destroy BaseModel ' + basemodel_id)
            self.assertTrue(val.getvalue() != "** no instance found **\n")

    def test_all_fakeclass(self):
        """Check if class name exists"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('all FakeClass')
            self.assertTrue(val.getvalue() == "** class doesn't exist **\n")

    def test_all_working(self):
        """Check if the method all works correctly"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('all')
            self.assertTrue(len(val.getvalue()) > 0)

    def test_all_trueclass(self):
        """Check that the all method works correctly with a class input"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('all BaseModel')
            self.assertTrue(len(val.getvalue()) > 0)

    def test_update_missingclass(self):
        """Check if the class is missing"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('update')
            self.assertTrue(val.getvalue() == "** class name missing **\n")

    def test_update_wrongclass(self):
        """Check if the class exists"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('update FakeClass')
            self.assertTrue(val.getvalue() == "** class doesn't exist **\n")

    def test_update_noinstance(self):
        """Check if the instance id is missing"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('update BaseModel')
            self.assertTrue(val.getvalue() == "** instance id missing **\n")

    def test_update_notfound(self):
        """Check if instance id exists"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('update BaseModel 121212')
            self.assertTrue(val.getvalue() == "** no instance found **\n")

    def test_update_missing_name(self):
        """Check if the attribute name is missing"""
        with patch('sys.stdout', new=StringIO()) as my_id:
            HBNBCommand().onecmd('create BaseModel')
            basemodel_id = my_id.getvalue()
            self.assertTrue(len(basemodel_id) > 0)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('update BaseModel ' + basemodel_id)
            self.assertTrue(val.getvalue() == "** attribute name missing **\n")

    def test_update_missing_value(self):
        """Check if the attribute value is missing"""
        with patch('sys.stdout', new=StringIO()) as my_id:
            HBNBCommand().onecmd('create BaseModel')
            base_id = my_id.getvalue()
            self.assertTrue(len(base_id) > 0)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('update BaseModel ' + base_id + "first_name")
            self.assertTrue(val.getvalue() == "** value missing **\n")

    def test_update_ok(self):
        """Update test working"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create BaseModel")
            user_id = val.getvalue()
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("update BaseModel " + user_id + " name betty")
            HBNBCommand().onecmd("show BaseModel " + user_id)
            self.assertTrue("betty" in val.getvalue())

    def test_update_okextra(self):
        """Update test working"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create BaseModel")
            uid = val.getvalue()
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("update BaseModel " + uid + " name betty ho")
            HBNBCommand().onecmd("show BaseModel " + uid)
            self.assertTrue("betty" in val.getvalue())

    def test_user_console(self):
        """Test the class User with the console"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create User")
            user_id = val.getvalue()
            self.assertTrue(user_id != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show User " + user_id)
            self.assertTrue(val.getvalue() != "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("all User")
            self.assertTrue(val.getvalue() != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("update User " + user_id + " name betty")
            HBNBCommand().onecmd("show User " + user_id)
            self.assertTrue("betty" in val.getvalue())
            HBNBCommand().onecmd("destroy User " + user_id)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show User " + user_id)
            self.assertEqual(val.getvalue(), "** no instance found **\n")

    def test_place_console(self):
        """Test the class Place with the console"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create Place")
            user_id = val.getvalue()
            self.assertTrue(user_id != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show Place " + user_id)
            self.assertTrue(val.getvalue() != "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("all Place")
            self.assertTrue(val.getvalue() != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("update Place " + user_id + " name betty")
            HBNBCommand().onecmd("show Place " + user_id)
            self.assertTrue("betty" in val.getvalue())
            HBNBCommand().onecmd("destroy Place " + user_id)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show Place " + user_id)
            self.assertEqual(val.getvalue(), "** no instance found **\n")

    def test_state_console(self):
        """Test the class State with the console"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create State")
            user_id = val.getvalue()
            self.assertTrue(user_id != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show State " + user_id)
            self.assertTrue(val.getvalue() != "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("all State")
            self.assertTrue(val.getvalue() != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("update State " + user_id + " name betty")
            HBNBCommand().onecmd("show State " + user_id)
            self.assertTrue("betty" in val.getvalue())
            HBNBCommand().onecmd("destroy State " + user_id)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show State " + user_id)
            self.assertEqual(val.getvalue(), "** no instance found **\n")

    def test_city_console(self):
        """Test the class City with the console"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create City")
            user_id = val.getvalue()
            self.assertTrue(user_id != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show City " + user_id)
            self.assertTrue(val.getvalue() != "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("all City")
            self.assertTrue(val.getvalue() != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("update City " + user_id + " name betty")
            HBNBCommand().onecmd("show City " + user_id)
            self.assertTrue("betty" in val.getvalue())
            HBNBCommand().onecmd("destroy City " + user_id)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show City " + user_id)
            self.assertEqual(val.getvalue(), "** no instance found **\n")

    def test_amenity_console(self):
        """Test the class Amenity with the console"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create Amenity")
            user_id = val.getvalue()
            self.assertTrue(user_id != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show Amenity " + user_id)
            self.assertTrue(val.getvalue() != "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("all Amenity")
            self.assertTrue(val.getvalue() != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("update Amenity " + user_id + " name betty")
            HBNBCommand().onecmd("show Amenity " + user_id)
            self.assertTrue("betty" in val.getvalue())
            HBNBCommand().onecmd("destroy Amenity " + user_id)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show Amenity " + user_id)
            self.assertEqual(val.getvalue(), "** no instance found **\n")

    def test_review_console(self):
        """Test the class Review with the console"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create Review")
            user_id = val.getvalue()
            self.assertTrue(user_id != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show Review " + user_id)
            self.assertTrue(val.getvalue() != "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("all Review")
            self.assertTrue(val.getvalue() != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("update Review " + user_id + " name betty")
            HBNBCommand().onecmd("show Review " + user_id)
            self.assertTrue("betty" in val.getvalue())
            HBNBCommand().onecmd("destroy Review " + user_id)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show Review " + user_id)
            self.assertEqual(val.getvalue(), "** no instance found **\n")

    def test_alternative_all(self):
        """Test alternative all with [class].all"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("User.all()")
            self.assertTrue(len(val.getvalue()) > 0)

    def test_alternative_show(self):
        """Test alternative show with [class].show"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create User")
            user_id = val.getvalue()
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("User.show(" + user_id + ")")
            self.assertTrue(val.getvalue() != "** no instance found **\n")

    def test_alternative_count(self):
        """Test alternative count with [class].count"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("User.count()")
            self.assertTrue(len(val.getvalue()) > 0)

    def test_alternative_update(self):
        """Test alternative update with [class].update(id, attr, val)"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create User")
            user_id = val.getvalue()
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("User.update(" + user_id + ", 'name', 'betty')")
            self.assertTrue(val.getvalue() != "** no instance found **\n")

if __name__ == '__main__':
    unittest.main()

