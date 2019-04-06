import unittest 
from coding_skills import coding_skills, read_json

class TestCodingSkills(unittest.TestCase):
    def test_when_no_system_argument_is_given_are_throw_an_exception(self):
        self.assertRaises(Exception, read_json())

if __name__ == '__main__':
    unittest.main()