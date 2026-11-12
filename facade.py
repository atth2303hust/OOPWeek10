# /****************/
# Mã sinh viên: 202419007
# Họ tên: Phạm Anh Tú
# /****************/
"""Facade: gom nhiều thao tác thành các chế độ tự động."""

from .configuration import HomeConfiguration


class SmartHomeFacade:
    def __init__(self, light, fan, door, config=None):
        self.light = light
        self.fan = fan
        self.door = door
        if config is not None:
            self.config = config
        else:
            self.config = HomeConfiguration.instance()

    def go_to_work(self):
        """Đi làm: tắt đèn, tắt quạt, khóa cửa."""
        self.light.turn_off()
        self.fan.turn_off()
        self.door.lock()

    def go_to_sleep(self):
        """Đi ngủ: tắt quạt, khóa cửa, bật đèn và chỉnh độ sáng ban đêm."""
        self.fan.turn_off()
        self.door.lock()
        self.light.turn_on()
        level = self.config.night_light_level
        self.light.set_brightness(level)
        print(f"Night light level: {level}%")
