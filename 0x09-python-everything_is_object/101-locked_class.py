#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    the user can't init LockedClass attributes
    for all except 'first_name'.
    """

    __slots__ = ["first_name"]
