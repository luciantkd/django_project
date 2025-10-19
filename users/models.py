# users/models.py
from django.db import models
from django.contrib.auth.models import User
from PIL import Image, ImageOps

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_images/')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        # pass through args/kwargs so force_insert/force_update work
        super().save(*args, **kwargs)

        # Protect against missing file (e.g., default image not on disk)
        if not self.image or not hasattr(self.image, "path"):
            return

        # Open and auto-fix EXIF orientation
        img = ImageOps.exif_transpose(Image.open(self.image.path))

        if img.height > 300 or img.width > 300:
            img.thumbnail((300, 300))
            img.save(self.image.path)
