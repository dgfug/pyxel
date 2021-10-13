import pyxel

from .button import Button
from .settings import (
    BUTTON_DISABLED_COLOR,
    BUTTON_ENABLED_COLOR,
    BUTTON_PRESSED_COLOR,
    BUTTON_TEXT_COLOR,
)


class TextButton(Button):
    """
    Events:
        press
        release
    """

    def __init__(self, parent, x, y, text, **kwargs):
        super().__init__(
            parent,
            x,
            y,
            len(text) * pyxel.FONT_WIDTH + 3,
            pyxel.FONT_HEIGHT + 1,
            **kwargs
        )

        self._text = text

        self.add_event_listener("draw", self.__on_draw)

    def __on_draw(self):
        x = self.x
        y = self.y
        w = self.width
        h = self.height
        col = (
            BUTTON_PRESSED_COLOR
            if self.is_pressed
            else (BUTTON_ENABLED_COLOR if self.is_enabled else BUTTON_DISABLED_COLOR)
        )

        pyxel.line(x + 1, y, x + w - 2, y, col)
        pyxel.rect(x, y + 1, w, h - 2, col)
        pyxel.line(x + 1, y + h - 1, x + w - 2, y + h - 1, col)
        pyxel.text(x + 2, y + 1, self._text, BUTTON_TEXT_COLOR)
