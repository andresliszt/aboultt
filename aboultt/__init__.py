"""Package initialization"""

from aboultt.settings import init_project_settings
from aboultt._logging import configure_logging


SETTINGS = init_project_settings()

logger = configure_logging("person_detector", SETTINGS, kidnap_loggers = True)




