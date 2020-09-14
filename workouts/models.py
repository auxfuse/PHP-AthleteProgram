from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Categories
categories = [
    ('', 'Select Workout Category'),
    ('crossfit', 'Crossfit'),
    ('gymnastics', 'Gymnastics'),
    ('metcon', 'Metcon'),
    ('olympic weightlifting', 'Olympic Weightlifting'),
    ('strength and conditioning', 'Strength & Conditioning'),
]


# Models
class Workout(models.Model):
    """
    Model to define the fields required to create workouts per day.
    """
    title = models.CharField(max_length=150)
    coach = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=25, choices=categories)
    part_a = models.TextField()
    part_b = models.TextField()
    part_c = models.TextField()
    coach_comments = models.TextField()

    def __str__(self):
        return self.title
