from django.db import models


# Create your models of University Classes
class UniversityCampus(models.Model):
    name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=60, default="", blank=True, null=False)
    campus_id = models.IntegerField(default="", blank=True, null=False)

    # Creates model manager
    object = models.Manager()

    # Displays the object output values in the form of a string
    def __str__(self):
        display_campus = '{0.title}: {0.instructor_name}'
        return display_campus.format(self)

    # removes added 's' that Django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "University Campuses"
