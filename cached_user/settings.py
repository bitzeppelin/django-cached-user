from django.conf import settings
from cached_user import constants


CACHED_USER_DEFAULT_USER_ID = getattr(
    settings,
    'CACHED_USER_DEFAULT_USER_ID',
    constants.CACHED_USER_DEFAULT_USER_ID
)


DEFAULT_CACHE_TIMEOUT = getattr(
    settings,
    'DEFAULT_CACHE_TIMEOUT',
    constants.DEFAULT_CACHE_TIMEOUT
)


CACHED_USER_KEY_TEMPLATE = getattr(
    settings,
    'CACHED_USER_KEY_TEMPLATE',
    constants.CACHED_USER_KEY_TEMPLATE
)

