#!/usr/bin/python3
""" unittests for base.py
Unittest classes:
    TestBase_instantiation
    TestBase_to_json_string
    TestBase_save_to_file
    TestBase_from_json_string
    TestBase_create
    TestBase_load_from_file
    TestBase_save_to_file_csv
    TestBase_load_from_file_csv
    """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase_instantiation(unittest.TestCase):
    """ test init of the Base class."""
    def test_no_arg(self):
        t1 = Base()
        t2 = Base()
        self.assertEqual(t1.id, t2.id - 1)

    def test_None_id(self):
        t1 = Base(None)
        t2 = Base(None)
        self.assertEqual(t1.id, t2.id - 1)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_id_public(self):
        t = Base(12)
        t.id = 15
        self.assertEqual(15, b.id)

    def test_three_bases(self):
        t1 = Base()
        t2 = Base()
        t3 = Base()
        self.assertEqual(t1.id, t3.id - 2)

    def test_id_public(self):
        t = Base(20)
        t.id = 30
        self.assertEqual(30, t.id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(20).__nb_instances)


class TestBase_to_json_string(unittest.TestCase):
    """ UnitTest for to_json_string  in base class"""
    def test_to_json_string_rectangle_type(self):
        r = Rectangle(14, 11, 6, 12, 10)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_rectangle_len_dict(self):
        r = Rectangle(14, 11, 6, 12, 10)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 54)

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))


class TestBase_save_to_file(unittest.TestCase):
    """ Unittests save_to_file  of Base class."""
    @classmethod
    def cleanFiles(self):
        """ clear already exisitng files before each new test"""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_len_rectangle(self):
        r = Rectangle(14, 11, 6, 12, 10)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 54)

    def test_save_to_file_len_square(self):
        s = Square(12, 9, 4, 10)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 40)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_overwrite(self):
        s = Square(14, 7, 44, 7)
        Square.save_to_file([s])
        s = Square(15, 12, 7, 13)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 40)


class TestBase_from_json_string(unittest.TestCase):
    """ Unittests  from_json_string method of Base class """
    def test_from_json_string_type(self):
        mylist = [{"id": 80, "width": 14, "height": 8}]
        in_list = Rectangle.to_json_string(mylist)
        out_list = Rectangle.from_json_string(in_list)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_two_squares(self):
        mylist = [{"id": 80, "size": 14, "height": 8},
                  {"id": 7, "size": 1, "height": 7}]
        in_list = Square.to_json_string(mylist)
        out_list = Square.from_json_string(in_list)
        self.assertEqual(in_list, out_list)


class TestBase_create(unittest.TestCase):
    """Unittests create of Base class."""
    def test_create_rectangle_original(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))

    def test_create_rectangle_new(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))

    def test_create_rectangle_is(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_rectangle_equals(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_square_original(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s1))

    def test_create_square_new(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s2))

    def test_create_square_is(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def test_create_square_equals(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)


class TestBase_load_from_file(unittest.TestCase):
    """Unittests load_from_file of Base class."""

    @classmethod
    def clearFiles(self):
        """clear previous file before start test."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

        def test_load_from_file_first_rectangle(self):
            r1 = Rectangle(10, 7, 2, 8, 1)
            r2 = Rectangle(2, 4, 5, 6, 2)
            Rectangle.save_to_file([r1, r2])
            list_rectangles_output = Rectangle.load_from_file()
            self.assertEqual(str(r1), str(list_rectangles_output[0]))

        def test_load_from_file_second_rectangle(self):
            r1 = Rectangle(10, 7, 2, 8, 1)
            r2 = Rectangle(2, 4, 5, 6, 2)
            Rectangle.save_to_file([r1, r2])
            list_rectangles_output = Rectangle.load_from_file()
            self.assertEqual(str(r2), str(list_rectangles_output[1]))

        def test_load_from_file_rectangle_types(self):
            r1 = Rectangle(10, 7, 2, 8, 1)
            r2 = Rectangle(2, 4, 5, 6, 2)
            Rectangle.save_to_file([r1, r2])
            output = Rectangle.load_from_file()
            self.assertTrue(all(type(obj) == Rectangle for obj in output))

        def test_load_from_file_first_square(self):
            s1 = Square(5, 1, 3, 3)
            s2 = Square(9, 5, 2, 3)
            Square.save_to_file([s1, s2])
            list_squares_output = Square.load_from_file()
            self.assertEqual(str(s1), str(list_squares_output[0]))

        def test_load_from_file_second_square(self):
            s1 = Square(5, 1, 3, 3)
            s2 = Square(9, 5, 2, 3)
            Square.save_to_file([s1, s2])
            list_squares_output = Square.load_from_file()
            self.assertEqual(str(s2), str(list_squares_output[1]))

        def test_load_from_file_square_types(self):
            s1 = Square(5, 1, 3, 3)
            s2 = Square(9, 5, 2, 3)
            Square.save_to_file([s1, s2])
            output = Square.load_from_file()
            self.assertTrue(all(type(obj) == Square for obj in output))

        def test_load_from_file_no_file(self):
            output = Square.load_from_file()
            self.assertEqual([], output)

        def test_load_from_file_more_than_one_arg(self):
            with self.assertRaises(TypeError):
                Base.load_from_file([], 1)


class TestBase_save_to_file_csv(unittest.TestCase):
    """Unittests testing save_to_file_csv of Base class."""

    @classmethod
    def clearFiles(self):
        """clear previous file before start test."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

        def test_save_to_file_csv_one_rectangle(self):
            r = Rectangle(10, 7, 2, 8, 5)
            Rectangle.save_to_file_csv([r])
            with open("Rectangle.csv", "r") as f:
                self.assertTrue("5,10,7,2,8", f.read())

        def test_save_to_file_csv_two_rectangles(self):
            r1 = Rectangle(10, 7, 2, 8, 5)
            r2 = Rectangle(2, 4, 1, 2, 3)
            Rectangle.save_to_file_csv([r1, r2])
            with open("Rectangle.csv", "r") as f:
                self.assertTrue("5,10,7,2,8\n2,4,1,2,3", f.read())

        def test_save_to_file_csv_one_square(self):
            s = Square(10, 7, 2, 8)
            Square.save_to_file_csv([s])
            with open("Square.csv", "r") as f:
                self.assertTrue("8,10,7,2", f.read())

        def test_save_to_file_csv_two_squares(self):
            s1 = Square(10, 7, 2, 8)
            s2 = Square(8, 1, 2, 3)
            Square.save_to_file_csv([s1, s2])
            with open("Square.csv", "r") as f:
                self.assertTrue("8,10,7,2\n3,8,1,2", f.read())

        def test_save_to_file__csv_cls_name(self):
            s = Square(10, 7, 2, 8)
            Base.save_to_file_csv([s])
            with open("Base.csv", "r") as f:
                self.assertTrue("8,10,7,2", f.read())

        def test_save_to_file_csv_overwrite(self):
            s = Square(9, 2, 39, 2)
            Square.save_to_file_csv([s])
            s = Square(10, 7, 2, 8)
            Square.save_to_file_csv([s])
            with open("Square.csv", "r") as f:
                self.assertTrue("8,10,7,2", f.read())

        def test_save_to_file__csv_None(self):
            Square.save_to_file_csv(None)
            with open("Square.csv", "r") as f:
                self.assertEqual("[]", f.read())

        def test_save_to_file_csv_empty_list(self):
            Square.save_to_file_csv([])
            with open("Square.csv", "r") as f:
                self.assertEqual("[]", f.read())

        def test_save_to_file_csv_no_args(self):
            with self.assertRaises(TypeError):
                Rectangle.save_to_file_csv()

        def test_save_to_file_csv_more_than_one_arg(self):
            with self.assertRaises(TypeError):
                Square.save_to_file_csv([], 1)


class TestBase_load_from_file_csv(unittest.TestCase):
    """Unittests load_from_file_csv  of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_from_file_csv_first_rectangle(self):
        r1 = Rectangle(13, 10, 5, 11, 4)
        r2 = Rectangle(4, 6, 7, 8, 4)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_csv_second_rectangle(self):
        r1 = Rectangle(13, 10, 5, 11, 4)
        r2 = Rectangle(4, 6, 7, 8, 4)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rectangle_types(self):
        r1 = Rectangle(13, 10, 5, 11, 4)
        r2 = Rectangle(4, 6, 7, 8, 4)
        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_csv_first_square(self):
        s1 = Square(15, 3, 9, 9)
        s2 = Square(10, 6, 3, 4)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_csv_second_square(self):
        s1 = Square(15, 3, 9, 9)
        s2 = Square(10, 6, 3, 4)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_csv_square_types(self):
        s1 = Square(15, 3, 9, 9)
        s2 = Square(10, 6, 3, 4)
        Square.save_to_file_csv([s1, s2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_csv_no_file(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)


if __name__ == "__main__":
    unittest.main()
