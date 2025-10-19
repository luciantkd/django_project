from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Ensures every user always has a profile.
    Creates one if missing, updates it otherwise.
    Works even for users created before signals were set up.
    """
    # Create a profile if this is a new user
    if created:
        Profile.objects.get_or_create(user=instance)
        print(f'Profile created for new user: {instance.username}')
    else:
        # For existing users, ensure a profile exists (important for password reset)
        profile, _ = Profile.objects.get_or_create(user=instance)
        profile.save()
        print(f'Profile updated for user: {instance.username}')
