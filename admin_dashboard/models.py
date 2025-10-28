from django.db import models

# Create your models here.


class Organiser(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    info = models.TextField()
    photo = models.ImageField(upload_to='organisers/')

    def __str__(self):
        return self.name
    
class Mentor(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField()
    photo = models.ImageField(upload_to='mentors/')

    def __str__(self):
        return self.name    
    
class CricketNews(models.Model):
    heading = models.CharField(max_length=255)
    subheading = models.CharField(max_length=255, blank=True)
    content = models.TextField()
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to='cricket_news/images/', blank=True)
    video = models.FileField(upload_to='cricket_news/videos/', blank=True)

    def __str__(self):
        return self.heading


class Sponsor(models.Model):
    image = models.ImageField(upload_to='sponsors/images/')
    url = models.URLField(blank=True)
    info = models.TextField(blank=True)

    def __str__(self):
        return self.url if self.url else self.info[:30]

class Announcement(models.Model):
    heading = models.CharField(max_length=200)
    date = models.DateField()
    info = models.TextField()
    image = models.ImageField(upload_to='announcements/', blank=True)

    def __str__(self):
        return self.heading

from django.db import models

class Result(models.Model):
    heading = models.CharField(max_length=255)
    date = models.DateField()
    image = models.ImageField(upload_to='results/')

    def __str__(self):
        return f"{self.heading} - {self.date}"


class Tournament(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="tournament_logos/")
    start_date = models.DateField()
    end_date = models.DateField()
    venue = models.CharField(max_length=255)
    num_teams = models.IntegerField()
    num_matches = models.IntegerField()

    def __str__(self):
        return self.name
    
class TeamEntry(models.Model):
    owner_name = models.CharField(max_length=100)
    team_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='team_entries/photos/', blank=True, null=True)
    tournaments = models.ManyToManyField(Tournament, related_name="teams")  # 🔗 link to tournaments

    def __str__(self):
        return f"{self.team_name} ({self.owner_name})"


class Player(models.Model):
    PLAYING_ROLES = [
        ("Batsman", "Batsman"),
        ("Bowler", "Bowler"),
        ("All-rounder", "All-rounder"),
        ("Wicket-Keeper", "Wicket-Keeper"),
    ]

    player_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    dob = models.DateField()
    playing_role = models.CharField(max_length=50, choices=PLAYING_ROLES)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    team = models.ForeignKey(TeamEntry, on_delete=models.CASCADE, related_name="players")
    tournaments = models.ManyToManyField(Tournament, related_name="players")  # 🔗 link to tournaments

    def __str__(self):
        return f"{self.player_name} - {self.team.team_name}"


    
from django.db import models

# For slider
class SliderImage(models.Model):
    image = models.ImageField(upload_to="slider/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Slider Image {self.id}"


# For team members
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=200)
    image = models.ImageField(upload_to="team/")
    linkedin = models.URLField(max_length=250, blank=True, null=True)
    instagram = models.URLField(max_length=250, blank=True, null=True)
    facebook = models.URLField(max_length=250, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to="gallery/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title if self.title else f"Image {self.id}"
    

from django.db import models

class Contact(models.Model):
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.email


class Advertisement(models.Model):
    image = models.ImageField(upload_to='advertisements/')  # stored in media/advertisements/
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Advertisement {self.id}"