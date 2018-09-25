from django.db import models


class Artist(models.Model):
    """Model the data of a musical artist"""

    Artist_ID = models.AutoField(primary_key=True)
    Artist_Name = models.CharField(max_length=140)
    Year_Established = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        verbose_name = ("Artist")
        verbose_name_plural = ("Artists")

    def __str__(self):
        return self.Artist_Name

    def get_absolute_url(self):
        return reverse("Artist_detail", kwargs={"pk": self.pk})


class Song(models.Model):
    """Model the data of a song track"""

    Song_ID = models.AutoField(primary_key=True)
    Song_Title = models.CharField(max_length=140)
    Song_Length = models.DurationField(blank=True, null=True)
    Release_Date = models.DateField(auto_now=False, auto_now_add=False)
    Genre_ID = models.ForeignKey("Genre", on_delete=models.CASCADE)
    Artist_ID = models.ForeignKey("Artist", on_delete=models.CASCADE)
    Album_ID = models.ForeignKey("Album", on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Song")
        verbose_name_plural = ("Songs")

    def __str__(self):
        return self.Song_Title

    def get_absolute_url(self):
        return reverse("Song_detail", kwargs={"pk": self.pk})


class Album(models.Model):
    """Model the data of an album"""

    Album_ID = models.AutoField(primary_key=True)
    Album_Title = models.CharField(max_length=140, blank=True, null=True)
    Release_Date = models.DateField(auto_now=False, auto_now_add=False)
    Album_Length = models.DurationField(blank=True, null=True)
    Album_Label = models.CharField(max_length=50)
    Artist_ID = models.ForeignKey("Artist", on_delete=models.CASCADE)
    Genre_ID = models.ForeignKey("Genre", on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Album")
        verbose_name_plural = ("Albums")

    def __str__(self):
        return self.Album_Title

    def get_absolute_url(self):
        return reverse("Album_detail", kwargs={"pk": self.pk})


class Genre(models.Model):
    """Model the data of a genre"""

    Genre_ID = models.AutoField(primary_key=True)
    Genre_Name = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Genre")
        verbose_name_plural = ("Genres")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Genre_detail", kwargs={"pk": self.pk})
