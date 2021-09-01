import platform

system = platform.system()

if system == "Darwin":
    from .lib.mac.pyxel_wrapper import *  # type: ignore  # noqa F403
elif system == "Windows":
    from .lib.windows.pyxel_wrapper import *  # type: ignore  # noqa F403
elif system == "Linux":
    from .lib.linux.pyxel_wrapper import *  # type: ignore  # noqa F403
else:
    raise Exception("unsupported platform")
