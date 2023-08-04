from django.db import models

class TestApp(models.Model):
    title = models.CharField(max_length=100)
    app_name = models.CharField(max_length=100)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.title
