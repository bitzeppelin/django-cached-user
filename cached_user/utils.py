from django.conf import settings
from django.contrib.auth.models import User
from django.core.cache import cache

from cached_user.constants import CACHED_USER_KEY_TEMPLATE
from cached_users import settings as app_settings

def get_cached_user(user_id):
    """ Gets a User object from the Cache, or try to get it from the DB, or
    return a None object if it does not exist. Receives the User Id as the
    parameter.
    """
    cache_key = app_settings.CACHED_USER_KEY_TEMPLATE.format(
        site_id=settings.SITE_ID, 
        user_id=user_id
    )
    user = cache.get(cache_key, None)
    if user is None:
        try:
            user = User.objects.get(pk=user_id)
            cache.set(cache_key, user, app_settings.DEFAULT_CACHE_TIMEOUT)
        except User.DoesNotExist:
            user = None
    return user
