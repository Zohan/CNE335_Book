import unittest

from User import User
from PowerUser import PowerUser
from Admin import Admin
from NormalUser import NormalUser


class TestCase(unittest.TestCase):
    def test_admin_class_creation_type(self):
        admin = Admin("Andy", "AdminAndy", "PassAndy", "Andy@User.com")
        self.assertEqual(Admin, type(admin))

    def test_admin_class_attributes_stored(self):
        admin = Admin("Andy", "AdminAndy", "PassAndy", "Andy@User.com")
        self.assertEqual(admin.name, "Andy")
        self.assertEqual(admin.username, "AdminAndy")
        self.assertEqual(admin.password, "PassAndy")
        self.assertEqual(admin.email_address, "Andy@User.com")
        self.assertIn("delete", admin.actions)
        self.assertIn("add_action", admin.actions)
        self.assertIn("cd", admin.actions)

    def test_admin_class_add_action_success(self):
        admin = Admin("Andy", "AdminAndy", "PassAndy", "Andy@User.com")
        self.assertEqual(Admin, type(admin))
        self.assertTrue(admin.add_action(admin, "add_action"))
        new_normal_user = NormalUser("Sam", "NormalSam", "PassSam", "Sam@User.com")
        new_power_user = PowerUser("Pam", "PowerPam", "PassPam", "Pam@User.com")
        self.assertTrue(admin.add_action(new_normal_user, "new_action"))
        self.assertIn("new_action", new_normal_user.actions)
        self.assertTrue(admin.add_action(new_power_user, "new_action"))
        self.assertIn("new_action", new_power_user.actions)

    def test_user_class_creation_type(self):
        user = User("Bob", "UserBob", "PassBob", "Bob@User.com", ["ls"])
        self.assertEqual(User, type(user))

    def test_user_class_attributes_stored(self):
        user = User("Bob", "UserBob", "PassBob", "Bob@User.com", ["ls"])
        self.assertEqual(user.name, "Bob")
        self.assertEqual(user.username, "UserBob")
        self.assertEqual(user.password, "PassBob")
        self.assertEqual(user.email_address, "Bob@User.com")
        self.assertIn("ls", user.actions)
        self.assertNotIn("add_action", user.actions)
        self.assertNotIn("cd", user.actions)

    def test_user_class_add_action_fail(self):
        user = User("Bob", "UserBob", "PassBob", "Bob@User.com", ["ls"])
        self.assertEqual(User, type(user))
        self.assertNotEquals(Admin, type(user))
        self.assertFalse(user.add_action(user, "add_action"))

    def test_normal_user_class_creation_type(self):
        normal_user = NormalUser("Sam", "NormalSam", "PassSam", "Sam@User.com")
        self.assertEqual(NormalUser, type(normal_user))

    def test_normal_user_class_attributes_stored(self):
        normal_user = NormalUser("Sam", "NormalSam", "PassSam", "Sam@User.com")
        self.assertEqual(normal_user.name, "Sam")
        self.assertEqual(normal_user.username, "NormalSam")
        self.assertEqual(normal_user.password, "PassSam")
        self.assertEqual(normal_user.email_address, "Sam@User.com")
        self.assertIn("ls", normal_user.actions)
        self.assertNotIn("add_action", normal_user.actions)
        self.assertIn("cd", normal_user.actions)

    def test_normal_user_class_add_action_fail(self):
        normal_user = NormalUser("Sam", "NormalSam", "PassSam", "Sam@User.com")
        self.assertEqual(NormalUser, type(normal_user))
        self.assertNotEquals(Admin, type(normal_user))
        self.assertFalse(normal_user.add_action(normal_user, "add_action"))

    def test_power_user_class_creation_type(self):
        power_user = PowerUser("Pam", "PowerPam", "PassPam", "Pam@User.com")
        self.assertEqual(PowerUser, type(power_user))

    def test_power_user_class_attributes_stored(self):
        power_user = PowerUser("Pam", "PowerPam", "PassPam", "Pam@User.com")
        self.assertEqual(power_user.name, "Pam")
        self.assertEqual(power_user.username, "PowerPam")
        self.assertEqual(power_user.password, "PassPam")
        self.assertEqual(power_user.email_address, "Pam@User.com")
        self.assertIn("delete", power_user.actions)
        self.assertNotIn("add_action", power_user.actions)
        self.assertIn("cd", power_user.actions)

    def test_power_user_class_add_action_fail(self):
        power_user = PowerUser("Pam", "PowerPam", "PassPam", "Pam@User.com")
        self.assertEqual(PowerUser, type(power_user))
        self.assertNotEquals(Admin, type(power_user))
        self.assertFalse(power_user.add_action(power_user, "add_action"))
