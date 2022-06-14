from django.test import TestCase
from django.urls import reverse

from .models import Todo

# Create your tests here.

# class TodoModelTests(TestCase):

#     def test_todo_with_empty_title(self):
#         """
#         test that creation of an empty todo item will fail
#         """
#         todo = Todo()
#         todo.save()


class TodoIndexViewTests(TestCase):

    def test_no_items(self):
        """
        If no todos, display 'You have no todo items.' in template view
        """

        response = self.client.get(reverse('todolist:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'You have no todo items.')
        self.assertQuerysetEqual(response.context['todos'], [])

    def test_created_todo_items_get_displayed(self):
        """
        Create two todo items and assert they are displayed on page
        """
        todo = Todo.objects.create(title='Todo Item 1')
        todo2 = Todo.objects.create(title='Todo Item 2')

        response = self.client.get(reverse('todolist:index'))
        
        self.assertContains(response, 'Todo Item 1')
        self.assertContains(response, 'Todo Item 2')

        self.assertQuerysetEqual(response.context['todos'], [todo, todo2], ordered=False)



