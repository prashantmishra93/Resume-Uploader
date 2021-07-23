from django.db import models
from django.utils import timezone


study = (
    ('ITI', 'ITI'),
    ('Diploma', 'Diploma'),
    ('B Tech,', 'B Tech.'),
    ('M Tech', 'M Tech'),
    ('BA.', 'BA.'),
    ('BSc.', 'BSc.'),
    ('BCom.', 'BCom.'),
    ('Phd.', 'Phd.'),
)

skill = (
    ('Python', 'Python'),
    ('Machine Learning', 'Machine Learning'),
    ('Java', 'Java'),
    ('Web Developer', 'Web Developer'),
    ('Web Designer', 'Web Designer'),
    ('Artificial Intelligent', 'Artificial Intelligent'),
    ('Deep Learning', 'Deep Learning'),
    ('Data Science', 'Data Science'),
    ('Data Analysis', 'Data Analysis'),
    ('Designer', 'Designer'),
    ('Tool Designer', 'Tool Designer'),
    ('Auto CAD', 'Auto CAD'),
    ('Creo', 'Creo'),
    ('Catia', 'Catia'),
    ('NX', 'NX'),
    ('FEA', 'FEA'),
    ('Design Engineer', 'Design Engineer'),
    ('Draftsman', 'Draftsman'),
    ('Solidwork', 'Solidwork'),
    ('Programmer', 'Programmer'),
    ('DelCAM', 'DelCAM'),

)


class ResumeUpload(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(auto_now_add=False, auto_now=False)
    contact = models.PositiveIntegerField()
    email = models.EmailField()
    gender = models.CharField(max_length=50)
    father = models.CharField(max_length=100)
    mother = models.CharField(max_length=100)
    sivling = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100)
    pin = models.CharField(max_length=50)
    home_town = models.CharField(max_length=50)
    education = models.CharField(choices=study, max_length=50)
    experience = models.CharField(max_length=50, blank=True)
    skill = models.CharField(choices=skill, max_length=100, blank=True)
    language = models.CharField(max_length=50)
    hobbies = models.CharField(max_length=100)
    profile_img = models.ImageField(upload_to='profile', blank=True)
    document = models.FileField(upload_to='document', blank=True)
    date = models.DateTimeField(default=timezone.now())

    def publish(self):
        self.date = timezone.now()
