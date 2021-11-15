from PyQt5.QtWidgets import *


class MyQTextEdit(QTextEdit):
    def __init__(self, *args, **kwargs):
        super(QTextEdit, self).__init__(*args, **kwargs)

    def focusOutEvent(self, e):
        # Do something with the event here
        super(QTextEdit, self).focusOutEvent(e)  # Do the default action on the parent class QLineEdit