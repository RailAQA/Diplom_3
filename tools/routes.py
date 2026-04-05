from enum import Enum


class AppRoute(str, Enum):
    BASE = "https://stellarburgers.education-services.ru/"
    ORDER = BASE + "feed"
    LOGIN = BASE + "login"