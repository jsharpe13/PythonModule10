import unittest
from class_definitions import Student as t


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student1 = t.Student('Johnson', 'Mark', 'Computers', 3.5)
        self.student2 = t.Student('Richards', 'Simon', 'Computers')

    def tearDown(self):
        del self.student1
        del self.student2

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student2.last_name, 'Richards')
        self.assertEqual(self.student2.first_name, 'Simon')
        self.assertEqual(self.student2.major, 'Computers')
        self.assertEqual(self.student2.gpa, 0.0)

    def test_object_created_all_attributes(self):
        assert self.student1.last_name == 'Johnson'
        assert self.student1.first_name == 'Mark'
        assert self.student1.major == 'Computers'
        assert self.student1.gpa == 3.5

    def test_student_str(self):
        self.assertEqual(str(self.student1), 'Johnson, Mark has major Computers with gpa: 3.5')

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            s = t.Student('123', 'Mark', 'Computers')

    def test_object_not_created_error_fist_name(self):
        with self.assertRaises(ValueError):
            s = t.Student('Johnson', '123', 'Computers')

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            s = t.Student('Johnson', 'Mark', '123')

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            s = t.Student('Johnson', 'Mark', 'Computers', 'Three')


if __name__ == '__main__':
    unittest.main()
