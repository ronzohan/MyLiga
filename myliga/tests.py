from django.test import TestCase
from .models import Manager


class ManagerModelTest(TestCase):
    def test_the_str_representation_of_manager(self):
        my_manager = Manager()
        my_manager.first_name = "Ron"
        my_manager.last_name = "Magno"
        my_manager.save()

        saved_manager = Manager.objects.all()
        self.assertEqual(saved_manager.count(), 1)
        self.assertEqual(saved_manager.first(), my_manager)

    def test_str_representation_if_no_first_name(self):
        my_manager = Manager()
        my_manager.last_name = "Magno"
        my_manager.save()

        saved_managers = Manager.objects.all()
        self.assertEqual(saved_managers.first(), my_manager)