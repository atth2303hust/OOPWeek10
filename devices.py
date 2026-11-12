# /****************/
# Mã sinh viên: 202419007
# Họ tên: Phạm Anh Tú
# /****************/
"""Các thiết bị cụ thể: Đèn, Quạt, Cửa."""

from .interfaces import IDevice, IDimmable, ILockable


class SmartLight(IDimmable):
    """Đèn thông minh có thể bật/tắt và chỉnh độ sáng."""

    def __init__(self, name):
        if not name or not name.strip():
            raise ValueError("Tên thiết bị không được để trống.")
        super().__init__(name.strip())


class SmartFan(IDevice):
    """Quạt thông minh chỉ có bật/tắt."""

    def __init__(self, name):
        if not name or not name.strip():
            raise ValueError("Tên thiết bị không được để trống.")
        super().__init__(name.strip())


class SmartDoor(IDevice, ILockable):
    """Cửa thông minh vừa bật/tắt vừa khóa/mở khóa được."""

    def __init__(self, name):
        if not name or not name.strip():
            raise ValueError("Tên thiết bị không được để trống.")
        IDevice.__init__(self, name.strip())
        ILockable.__init__(self)
