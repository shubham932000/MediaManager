from django.db import models


class Album(models.Model):
	title = models.CharField(max_length=200)
	artist = models.CharField(max_length=200)
	genre = models.CharField(max_length=50, choices=[
		('English', 'English'),
		('Rock', 'Rock'),
		('Bollywood', 'Bollywood'),
		('Pop', 'Pop'),
		('Indie', 'Indie'),
		('Soundtrack', 'Soundtrack'),
		('Other', 'Other'),
	])
	rating = models.IntegerField(default=0, choices=[
		(1, 1),
		(2, 2),
		(3, 3),
		(4, 4),
		(5, 5),
	])
	cover_image = models.ImageField(default=None, null=True)

	def __str__(self):
		return self.title


class Song(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	file = models.FileField(default=None, null=True)

	def __str__(self):
		return self.album.title + " - " + self.name
'''

1> python code -> models.py

2> python manage.py makemigrations
migrations/0001_initals.py -> intermediate file 

3> python manage.py migrate
This will convert our python code in migrations folder to SQL code and run it 

'''