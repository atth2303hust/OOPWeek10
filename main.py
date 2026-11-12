# /****************/
# Mã sinh viên: 202419007
# Họ tên: Phạm Anh Tú
# /****************/
"""Chương trình chính Smart Home Mini. Chạy: python main.py hoặc python main.py --demo."""

import sys

from smarthome import (
    DeviceFactory,
    HomeConfiguration,
    IDimmable,
    ILockable,
    SmartHomeFacade,
    UnsupportedDeviceTypeError,
)


def build_home():
    light = DeviceFactory.create("light", "Living room light")
    fan = DeviceFactory.create("fan", "Living room fan")
    door = DeviceFactory.create("door", "Main door")

    config = HomeConfiguration.instance()
    facade = SmartHomeFacade(light, fan, door, config)
    devices = {
        light.name: light,
        fan.name: fan,
        door.name: door,
    }
    return devices, facade, config


def show_devices(devices):
    print("\nTRẠNG THÁI THIẾT BỊ")
    for dev in devices.values():
        status = "ON" if dev.is_on else "OFF"
        info = f"- {dev.name}: {status}"

        if isinstance(dev, ILockable):
            lock_text = "LOCKED" if dev.is_locked else "UNLOCKED"
            info += f" | {lock_text}"

        if isinstance(dev, IDimmable):
            info += f" | brightness={dev.brightness}%"

        print(info)


def run_demo():
    devices, facade, config = build_home()
    config.home_name = "My Home"
    config.night_light_level = 30

    print("=== DEMO SMART HOME MINI ===")
    print(f"Singleton identity: {config is HomeConfiguration.instance()}")

    print("\n[GoToWork]")
    facade.go_to_work()

    print("\n[GoToSleep]")
    facade.go_to_sleep()

    show_devices(devices)


def run_cli():
    devices, facade, config = build_home()
    print("SMART HOME MINI - FACTORY / SINGLETON / FACADE")

    while True:
        print("\n1. Xem thiết bị | 2. Đi làm | 3. Đi ngủ")
        print("4. Điều khiển một thiết bị | 5. Tạo thiết bị")
        print("6. Đổi độ sáng ban đêm | 7. Xem cấu hình | 0. Thoát")

        choice = input("Chọn: ").strip()

        if choice == "0":
            print("Tạm biệt!")
            break
        elif choice == "1":
            show_devices(devices)
        elif choice == "2":
            facade.go_to_work()
        elif choice == "3":
            facade.go_to_sleep()
        elif choice == "4":
            show_devices(devices)
            name = input("Tên thiết bị cần điều khiển: ").strip()
            if name not in devices:
                print("Không tìm thấy thiết bị.")
                continue

            device = devices[name]
            action = input("Lệnh (on/off/lock/unlock): ").strip().lower()
            if action == "on":
                device.turn_on()
            elif action == "off":
                device.turn_off()
            elif action == "lock" and isinstance(device, ILockable):
                device.lock()
            elif action == "unlock" and isinstance(device, ILockable):
                device.unlock()
            else:
                print("Thiết bị không hỗ trợ lệnh này.")
        elif choice == "5":
            kind = input("Loại (light/fan/door): ")
            name = input("Tên thiết bị mới: ").strip()
            if name in devices:
                print("Tên thiết bị đã tồn tại.")
                continue
            try:
                device = DeviceFactory.create(kind, name)
                devices[device.name] = device
                print(f"Đã tạo: {type(device).__name__} - {device.name}")
            except (UnsupportedDeviceTypeError, ValueError) as exc:
                print(f"Không tạo được: {exc}")
        elif choice == "6":
            try:
                level = int(input("Mức sáng (0-100): "))
                if 0 <= level <= 100:
                    config.night_light_level = level
                    print(f"Đã lưu mức sáng ban đêm: {config.night_light_level}%")
                else:
                    print("Mức sáng phải từ 0 đến 100.")
            except ValueError:
                print("Vui lòng nhập số nguyên!")
        elif choice == "7":
            print(f"Nhà: {config.home_name}; Mức sáng: {config.night_light_level}%")
        else:
            print("Lựa chọn không hợp lệ.")


def main():
    if "--demo" in sys.argv:
        run_demo()
    else:
        run_cli()


if __name__ == "__main__":
    main()
