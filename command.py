# -*- coding:utf-8 -*-
import sublime
from .status import MessageStatus


class CommandWithStatus(object):
    """
    This Command class allow you to control
    message status bar.
    """
    def __init__(self, *args, **kwargs):
        self._messageStatus = MessageStatus()

    def set_timed_message(self, message, time=5000, clear=False):
        """
        Show a message for a specified amount of time
        and re-set the previous after it.
        """
        old_message = self._messageStatus.message
        self.set_message(message)
        if not clear:
            sublime.set_timeout(lambda: self.set_message(old_message), time)
        else:
            self.unset_message()

    def set_message(self, message):
        """ Set a message """
        self._messageStatus.set_message(message)
        if not self._messageStatus.is_running:
            self._messageStatus.is_running = True
            self._messageStatus.run()

    def unset_message(self):
        """
        Unset message and stop refreshing
        status message bar.
        """
        self._messageStatus.is_running = False
