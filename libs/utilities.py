import platform


def is_raspberry() -> bool:
    if platform.system() != "Linux" or "aarch64" not in platform.machine():
        return False

    return True
