from django.db import models
# Create your models here.

class Owner(models.Model):
    name = models.CharField(max_length=200)
    do_we_like = models.BooleanField(default=None, null=True, blank=True)
    other_observations = models.TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class Pet(models.Model):
    legnum_choices = [
        ("0", "0"),
        ("2", "2"),
        ("4", "4"),
        ("6", "6"),
        ("8", "8"),
        ("Other", "Other"),
    ]

    name = models.CharField(max_length=100)
    race = models.CharField(max_length=100)
    owner_name = models.ForeignKey(to=Owner, on_delete=models.SET_NULL, null=True, blank=True)
    leg_number = models.CharField(max_length=50, choices=legnum_choices, default="4")
    do_we_like = models.BooleanField(default=None, null=True, blank=True)
    age = models.IntegerField("Age", null=True, blank=True)

    def __str__(self):
        return self.name




