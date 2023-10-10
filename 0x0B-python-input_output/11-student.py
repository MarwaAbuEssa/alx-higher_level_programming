#!/usr/bin/python3
""" class Student."""


class Student:
    """  a student."""

    def __init__(self, first_name, last_name, age):
        """ init new student

        Args:
            first_name (str): The first name
            last_name (str): The last name
            age (int): The age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ dic of the Student.

        Args:
            attrs (list): (Optional) The attributes
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """ replace attr of student

        Args:
            json (dict): key/value pair to replace atr
        """
        for k, v in json.items():
            setattr(self, k, v)
