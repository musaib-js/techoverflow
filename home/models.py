from django.db import models

CATEGORY_CHOICES = (
    ('general', 'General'),
    ('python', 'Python'),
    ('javascript', 'JavaScript'),
    ('cpp', 'C++'),
    ('web', 'Web Development'),
    ('app', 'App Development'),
    ('cp', 'Competitive Programming'),
)

class Post(models.Model):
    title = models.CharField(max_length = 200)
    heading = models.CharField(max_length = 600)
    author = models.CharField(max_length = 500)
    time_stamp = models.DateTimeField(auto_now_add=True)
    category = models.CharField(choices = CATEGORY_CHOICES, default="general", max_length=150)
    description = models.TextField()
    img = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title
    
