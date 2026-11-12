# /****************/
# Mã sinh viên: 202419007
# Họ tên: Phạm Anh Tú
# /****************/
"""Simple Factory: tạo thiết bị dựa theo tên loại."""

from .devices import SmartDoor, SmartFan, SmartLight


class UnsupportedDeviceTypeError(ValueError):
    """Lỗi khi nhập sai loại thiết bị."""
    pass


class DeviceFactory:
    @staticmethod
    def create(device_type, name):
        kind = str(device_type).strip().lower()
        if kind == "light":
            return SmartLight(name)
        elif kind == "fan":
            return SmartFan(name)
        elif kind == "door":
            return SmartDoor(name)
        else:
            raise UnsupportedDeviceTypeError(f"Không hỗ trợ loại thiết bị: {device_type}")
