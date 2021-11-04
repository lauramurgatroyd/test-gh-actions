import unittest

class TestModuleBase(unittest.TestCase):
    def test_version(self):
        try:
            from hello_world import version
            a = version.version
            print ("version", a)
            self.assertTrue(isinstance(a, str))
        except ImportError as ie:
            self.assertFalse(True, str(ie))
