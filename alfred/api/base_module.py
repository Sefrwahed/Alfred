from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QTextEdit

import random


class BaseModule:
    def __init__(self, entities):
        self.entities = entities
        self.layout = QVBoxLayout()

    def main_layout(self):
        return self.layout

    def start(self):
        # execute()
        self.populate_view()

    def execute(self):
        pass

    def populate_view(self):
        plain = QTextEdit()
        text = random.choice("abcdefghijklmno") * random.randint(1, 100)
        plain.setText(text)
        plain.setReadOnly(True)

        self.layout.addWidget(plain)
