from layout.entry import Ui_EntryUi
from layout.config import Ui_ConfigUi
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
import sys
from PyQt5.QtWidgets import QApplication


class Config(QMainWindow):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_ConfigUi()
        self.ui.setupUi(self)


class Entry(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_EntryUi()
        self.ui.setupUi(self)

        self.ui.open_config_btn.clicked.connect(self.slot_open_config)

    def slot_open_config(self):
        config = Config(None)
        config.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    entry = Entry()
    entry.show()
    sys.exit(app.exec_())


