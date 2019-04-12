from unittest import TestCase
import main_file


class TestEmployee(TestCase):

    def setUp(self):
        self.emp1 = main_file.Employee('Azamat', 'Sultanov')
        self.emp2 = main_file.Employee('Munara', 'Mamaeva')

    def tearDown(self):
        pass

    def test_email(self):

        self.assertEqual(self.emp1.email(), 'Azamat.Sultanov@mail.ru')
        self.assertEqual(self.emp2.email(), 'Munara.Mamaeva@mail.ru')

    def test_fullname(self):
        self.assertEqual(self.emp1.fullname(), 'Azamat Sultanov')
        self.assertEqual(self.emp2.fullname(), 'Munara Mamaeva')
