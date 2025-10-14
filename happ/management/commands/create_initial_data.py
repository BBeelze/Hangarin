# happ/management/commands/create_initial.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from ...models import Category, Priority, Task, SubTask, Note

class Command(BaseCommand):
    help = 'Create initial data for Hangarin app'

    def handle(self, *args, **kwargs):
        self.create_categories_and_priorities()
        self.create_tasks_with_subtasks_and_notes(20)  # Generate 20 tasks
        self.stdout.write(self.style.SUCCESS('✅ Initial Hangarin data created successfully!'))

    def create_categories_and_priorities(self):
        # Categories (as per spec)
        categories = ["Work", "School", "Personal", "Finance", "Projects"]
        for name in categories:
            Category.objects.get_or_create(name=name)

        # Priorities (as per spec)
        priorities = ["Critical", "High", "Medium", "Low", "Optional"]
        for name in priorities:
            Priority.objects.get_or_create(name=name)

        self.stdout.write(self.style.SUCCESS('✅ Categories and Priorities created.'))

    def create_tasks_with_subtasks_and_notes(self, count):
        fake = Faker()
        categories = list(Category.objects.all())
        priorities = list(Priority.objects.all())

        if not categories or not priorities:
            self.stdout.write(self.style.ERROR('❌ Categories or Priorities are empty. Run this command again after they exist.'))
            return

        for _ in range(count):
            # Create a task
            task = Task.objects.create(
                title=fake.sentence(nb_words=5).rstrip('.'),
                description=fake.paragraph(nb_sentences=3),
                status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
                deadline=timezone.make_aware(fake.date_time_this_month()),
                priority=fake.random_element(priorities),
                category=fake.random_element(categories)
            )

            # Create 1–3 SubTasks
            num_subtasks = fake.random_int(1, 3)
            for _ in range(num_subtasks):
                SubTask.objects.create(
                    title=fake.sentence(nb_words=4).rstrip('.'),
                    status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
                    task=task
                )

            # Create 0–2 Notes
            num_notes = fake.random_int(0, 2)
            for _ in range(num_notes):
                Note.objects.create(
                    task=task,
                    content=fake.paragraph(nb_sentences=2)
                )

        self.stdout.write(self.style.SUCCESS(f'✅ {count} Tasks with SubTasks & Notes created.'))