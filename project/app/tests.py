from app.models import Student
import unittest
from selenium import webdriver


class StudentTest(unittest.TestCase):

    def create_student(self, username="testuser"):
        return Student.objects.create(id=1, username=username, student_id="000001", email="tester@mail.com")

    def test_student_creation(self):
        student = self.create_student()
        self.assertTrue(isinstance(student, Student))
        self.assertEqual(student.__unicode__(), student.username)


class TeacherViewTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_teacher_view(self):
        self.driver.get('http://localhost:7000/app/teacher/')
        self.driver.find_element_by_id('mainTitle')
        self.driver.find_element_by_id('courseName')
        self.driver.find_element_by_id('mainContent')
        self.driver.find_element_by_id('addGroupBtn')
        self.driver.find_element_by_id('autoGroupBtn')
        self.driver.find_element_by_id('groupSettingsBtn')

    def test_auto_group_button(self):
        self.driver.get('http://localhost:7000/app/teacher/')
        self.driver.find_element_by_id('autoGroupBtn').click()
        self.driver.find_element_by_id('autoGroupModal')
        group_size_field = self.driver.find_element_by_id('autoGroupSize')
        group_size_field.clear()
        group_size_field.send_keys('5')
        self.driver.find_element_by_id('createButton').click()


    def tearDown(self):
        self.driver.quit

if __name__ == '__main__':
    unittest.main()
