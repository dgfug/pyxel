import pyxel

from .settings import (
    WIDGET_CLICK_DIST,
    WIDGET_CLICK_TIME,
    WIDGET_HOLD_TIME,
    WIDGET_PANEL_COLOR,
    WIDGET_REPEAT_TIME,
    WIDGET_SHADOW_COLOR,
)
from .widget_var import WidgetVar


class MouseCaptureInfo:
    widget = None
    key = None
    time = None
    press_pos = None
    last_press_pos = None


class Widget:
    """
    Variables:
        is_visible_var
        is_enabled_var

    Events:
        show
        hide
        enabled
        disabled
        mouse_down (key, x, y)
        mouse_up (key, x, y)
        mouse_drag (key, x, y, dx, dy)
        mouse_repeat (key, x, y)
        mouse_click (key, x, y)
        mouse_hover (x, y)
        update
        draw
    """

    _mouse_capture_info = MouseCaptureInfo()

    def __init__(
        self, parent, x, y, width, height, *, is_visible=True, is_enabled=True
    ):
        if parent:
            parent._children.append(self)

        self._parent = parent
        self._children = []
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._event_listeners = {}

        # is_visible_var
        self.new_var("is_visible_var", is_visible)
        self.add_var_event_listener("is_visible_var", "get", self.__on_is_visible_get)
        self.add_var_event_listener(
            "is_visible_var", "change", self.__on_is_visible_change
        )

        # is_enabled_var
        self.new_var("is_enabled_var", is_enabled)
        self.add_var_event_listener("is_enabled_var", "get", self.__on_is_enabled_get)
        self.add_var_event_listener(
            "is_enabled_var", "change", self.__on_is_enabled_change
        )

    @property
    def x(self):
        if self._parent:
            return self._parent.x + self._x
        else:
            return self._x

    @property
    def y(self):
        if self._parent:
            return self._parent.y + self._y
        else:
            return self._y

    @property
    def x2(self):
        return self.x + self.width - 1

    @property
    def y2(self):
        return self.y + self.height - 1

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def is_hit(self, x, y):
        return self.x <= x <= self.x2 and self.y <= y <= self.y2

    def set_pos(self, x, y):
        self._x = x
        self._y = y

    def set_size(self, width, height):
        self._width = width
        self._height = height

    def add_event_listener(self, event, listener):
        self._event_listeners.setdefault(event, [])
        self._event_listeners[event].append(listener)

    def remove_event_listener(self, event, listener):
        self._event_listeners.setdefault(event, [])
        self._event_listeners[event].remove(listener)

    def trigger_event(self, event, *args):
        self._event_listeners.setdefault(event, [])

        for listener in self._event_listeners[event]:
            listener(*args)

    def update_all(self):
        capture_widget = Widget._mouse_capture_info.widget

        if capture_widget:
            capture_widget._process_capture()
        else:
            self._process_input()

        self._update()

    def _process_input(self):
        if not self.is_visible_var or not self.is_enabled_var:
            return False

        for widget in reversed(self._children):
            if widget._process_input():
                return True

        x = pyxel.mouse_x
        y = pyxel.mouse_y

        if self.is_hit(x, y):
            key = None

            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                key = pyxel.MOUSE_BUTTON_LEFT
            elif pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT):
                key = pyxel.MOUSE_BUTTON_RIGHT
            elif pyxel.btnp(pyxel.MOUSE_BUTTON_MIDDLE):
                key = pyxel.MOUSE_BUTTON_MIDDLE

            if key is not None:
                self._start_capture(key)
                self.trigger_event("mouse_down", key, x, y)

            self.trigger_event("mouse_hover", x, y)

            return True

        return False

    def _start_capture(self, key):
        capture_info = Widget._mouse_capture_info
        capture_info.widget = self
        capture_info.key = key
        capture_info.time = pyxel.frame_count
        capture_info.press_pos = (pyxel.mouse_x, pyxel.mouse_y)
        capture_info.last_press_pos = capture_info.press_pos

    def _end_capture(self):
        capture_info = Widget._mouse_capture_info
        capture_info.widget = None
        capture_info.key = None
        capture_info.time = None
        capture_info.press_pos = None
        capture_info.last_press_pos = None

    def _process_capture(self):
        capture_info = Widget._mouse_capture_info
        last_x, last_y = capture_info.last_press_pos

        x = pyxel.mouse_x
        y = pyxel.mouse_y

        if x != last_x or y != last_y:
            self.trigger_event(
                "mouse_drag",
                capture_info.key,
                x,
                y,
                x - last_x,
                y - last_y,
            )
            capture_info.last_press_pos = (x, y)

        if self.is_hit(x, y):
            self.trigger_event("mouse_hover", x, y)

        if pyxel.btnp(capture_info.key, WIDGET_HOLD_TIME, WIDGET_REPEAT_TIME):
            self.trigger_event("mouse_repeat", capture_info.key, x, y)

        if pyxel.btnr(capture_info.key):
            self.trigger_event("mouse_up", capture_info.key, x, y)

            press_x, press_y = capture_info.press_pos

            if (
                pyxel.frame_count <= capture_info.time + WIDGET_CLICK_TIME
                and abs(x - press_x) <= WIDGET_CLICK_DIST
                and abs(y - press_y) <= WIDGET_CLICK_DIST
            ):
                self.trigger_event("mouse_click", capture_info.key, x, y)

            self._end_capture()

    def _update(self):
        if not self.is_visible_var:
            return

        self.trigger_event("update")

        for child in self._children:
            child._update()

    def draw_all(self):
        if not self.is_visible_var:
            return

        self.trigger_event("draw")

        for child in self._children:
            child.draw_all()

    @staticmethod
    def draw_panel(x, y, width, height, *, with_shadow=True):
        w = width
        h = height

        pyxel.line(x + 1, y, x + w - 2, y, WIDGET_PANEL_COLOR)
        pyxel.rect(x, y + 1, w, h - 2, WIDGET_PANEL_COLOR)
        pyxel.line(x + 1, y + h - 1, x + w - 2, y + h - 1, WIDGET_PANEL_COLOR)

        if with_shadow:
            pyxel.line(x + 2, y + h, x + w - 1, y + h, WIDGET_SHADOW_COLOR)
            pyxel.line(x + w, y + 2, x + w, y + h - 1, WIDGET_SHADOW_COLOR)
            pyxel.pset(x + w - 1, y + h - 1, WIDGET_SHADOW_COLOR)

    def new_var(self, name, value):
        member_name = self._widget_var_name(name)
        widget_var = WidgetVar(value)
        setattr(self, member_name, widget_var)

        def getter(self):
            return getattr(self, member_name).get()

        def setter(self, value):
            getattr(self, member_name).set(value)

        setattr(self.__class__, name, property(getter, setter))

    def copy_var(self, name, org_widget, org_name=None):
        new_member_name = self._widget_var_name(name)
        org_member_name = self._widget_var_name(org_name or name)
        widget_var = getattr(org_widget, org_member_name)
        setattr(self, new_member_name, widget_var)

        def getter(self):
            return getattr(self, new_member_name).get()

        def setter(self, value):
            getattr(self, new_member_name).set(value)

        setattr(self.__class__, name, property(getter, setter))

    def add_var_event_listener(self, name, event, listener):
        member_name = self._widget_var_name(name)
        widget_var = getattr(self, member_name)
        widget_var.add_event_listener(event, listener)

    def remove_var_event_listener(self, name, event, listener):
        member_name = self._widget_var_name(name)
        widget_var = getattr(self, member_name)
        widget_var.remove_event_listener(event, listener)

    @staticmethod
    def _widget_var_name(name):
        return "_widget_var_" + name

    def __on_is_visible_get(self, value):
        if self._parent:
            return self._parent.is_visible_var and value
        else:
            return value

    def __on_is_visible_change(self, value):
        self._trigger_visible_event(value)

    def _trigger_visible_event(self, is_visible):
        self.trigger_event("show" if is_visible else "hide")

        for child in self._children:
            if child.is_visible_var == is_visible:
                child._trigger_visible_event(is_visible)

    def __on_is_enabled_get(self, value):
        if self._parent:
            return self._parent.is_enabled_var and value
        else:
            return value

    def __on_is_enabled_change(self, value):
        self._trigger_enabled_event(value)

    def _trigger_enabled_event(self, is_enabled):
        self.trigger_event("enabled" if is_enabled else "disabled")

        for child in self._children:
            if child.is_enabled_var == is_enabled:
                child._trigger_enabled_event(is_enabled)
