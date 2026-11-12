# /****************/
# Mã sinh viên: 202419007
# Họ tên: Phạm Anh Tú
# /****************/
"""Singleton: lưu cấu hình dùng chung cho cả ngôi nhà."""


class HomeConfiguration:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.home_name = "My Home"
            cls._instance.night_light_level = 30
        return cls._instance

    @classmethod
    def instance(cls):
        return cls()
