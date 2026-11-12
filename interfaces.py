# /****************/
# Mã sinh viên: 202419007
# Họ tên: Phạm Anh Tú
# /****************/
"""Các lớp cơ sở cho thiết bị trong nhà thông minh."""


class IDevice:
    """Lớp cha chung cho mọi thiết bị bật/tắt."""

    def __init__(self, name):
        self.name = name
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"{self.name}: ON")

    def turn_off(self):
        self.is_on = False
        print(f"{self.name}: OFF")


class ILockable:
    """Lớp hỗ trợ khóa/mở khóa cho cửa."""

    def __init__(self):
        self.is_locked = False

    def lock(self):
        self.is_locked = True
        print(f"{self.name}: LOCKED")

    def unlock(self):
        self.is_locked = False
        print(f"{self.name}: UNLOCKED")


class IDimmable(IDevice):
    """Lớp mở rộng cho thiết bị chỉnh được độ sáng."""

    def __init__(self, name):
        super().__init__(name)
        self.brightness = 100

    def set_brightness(self, level):
        if 0 <= level <= 100:
            self.brightness = level
            print(f"{self.name}: brightness {level}%")
        else:
            print("Mức sáng phải từ 0 đến 100!")
