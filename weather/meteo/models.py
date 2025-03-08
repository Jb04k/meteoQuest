# meteoquest/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Model for searched city (can be used temporarily)
class City(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

# Extend the User with a Profile that holds gamification data
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    last_check_in = models.DateField(null=True, blank=True)
    streak = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} Profile"

# An Achievement (badge) definition
class Achievement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    points_required = models.IntegerField()
    icon = models.CharField(max_length=100, default="default_badge.png")
    
    def __str__(self):
        return self.name

# Which achievements a user (Profile) has earned
class UserAchievement(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    date_earned = models.DateField(default=timezone.now)
    
    def __str__(self):
        return f"{self.profile.user.username} - {self.achievement.name}"
