"""
A simple test script for hello_world.py.
"""
from package import hello_world


def test_hello_world_output():
    """
    Tests the output of hello_world() function.
    """
    assert hello_world.hello_world() == 'Hello World'
