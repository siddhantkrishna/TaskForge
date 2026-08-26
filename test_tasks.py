import unittest
from task import Task

class TestTaskModel(unittest.TestCase):
    def test_task_creation(self):
        t = Task(1, "Test Task", "high")
        self.assertEqual(t.task_id, 1)
        self.assertEqual(t.title, "Test Task")
        self.assertEqual(t.priority, "high")
        self.assertFalse(t.completed)

if __name__ == "__main__":
    unittest.main()
