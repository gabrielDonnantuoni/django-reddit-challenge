from accounts.models import User


def get_deleted_user():
    return User.objects.get_or_create(username='[deleted]')[0]
