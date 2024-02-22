from exam_music_app.profiles.models import Profile


"""
We can add get_profile() method here and use it when we need it
Instead of writing the method each time
So if we user it from this file, we should only import the method correctly and delete the previous wrote method
"""


def get_profile():
    return Profile.objects.first()
