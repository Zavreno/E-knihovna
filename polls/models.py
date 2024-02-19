from django.db import models
from PIL import Image
from django.utils import timezone


class Book(models.Model):
    ROMANCE = "Romány - Beletrie"
    ADVENTURE = "Dobrodružné"
    SCIFI = "Sci-Fi - Fantasy"
    CRIMI = "Krimi"
    MILITARY = "Vojenské"
    PIC_PUBLICATION = "Obrazové publikace"
    SPECIALIZED = "Odborné - Naučné"
    LOCAL_NAMES = "Místopis"
    PRAGENSIA = "Pragensie"
    HISTORY = "Historie"
    COMICS = "Komiksy"
    CHILDREN = "Děti - Mládež"
    ART = "Umění"
    BIOGRAPHY = "Biografie"
    ENCYCLOPEDIA = "Encyklopedie"
    BEST_READ = "Nejlepší světové čtení"
    OTHER = "Ostatní"
    GENRE_CHOICES = [
        (ROMANCE, "Romány - Beletrie"),
        (ADVENTURE, "Dobrodružné"),
        (SCIFI, "Sci-Fi - Fantasy"),
        (CRIMI, "Krimi"),
        (MILITARY, "Vojenské"),
        (PIC_PUBLICATION, "Obrazové publikace"),
        (SPECIALIZED, "Odborné - Naučné"),
        (LOCAL_NAMES, "Místopis"),
        (PRAGENSIA, "Pragensie"),
        (HISTORY, "Historie"),
        (COMICS, "Komiksy"),
        (CHILDREN, "Děti - Mládež"),
        (ART, "Umění"),
        (BIOGRAPHY, "Biografie"),
        (ENCYCLOPEDIA, "Encyklopedie"),
        (BEST_READ, "Nejlepší světové čtení"),
        (OTHER, "Ostatní"),
    ]
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=200, choices=GENRE_CHOICES)
    publisher = models.CharField(max_length=200)
    price = models.IntegerField(null=True, blank=True)
    web_price = models.IntegerField(null=True, blank=True)
    pub_date = models.IntegerField(null=True, blank=True)
    up_date = models.DateTimeField("date uploaded", default=timezone.now)
    image = models.ImageField(default="profile_pics/default.jpg", upload_to="profile_pics")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

