from layout.entry import Ui_EntryUi
from layout.config import Ui_ConfigUi
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QThread, pyqtSignal
import sys
import os
import yaml
from pprint import pprint
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QImage, QPixmap
from init import select_ticket_info_for_gui as select_ticket_info

base_dir = os.path.dirname(__file__)

config_path = os.path.join(base_dir, 'config', 'ticket_config.yaml')

pic_dir = os.path.join(base_dir, 'tmp', 'pic')


class QueryTicketThread(QThread):
    signOut = pyqtSignal(str)

    def __int__(self):
        super().__init__(self)

    def run(self):
        select_ticket_info.select(sign=self.signOut).main()



class Config(QMainWindow):
    def __init__(self, parent=None):
        self.conf_dict = {}
        self.load_config()

        super().__init__(parent)
        self.ui = Ui_ConfigUi()
        self.ui.setupUi(self)

        self.ui.accounts_of_12306_box.setStyleSheet("QGroupBox{ border: 1px groove grey; border-radius:5px;border-style: inset;}")
        self.ui.station_dates_box.setStyleSheet("QGroupBox{ border: 1px groove grey; border-radius:5px;border-style: inset;}")
        self.ui.station_date_input.setStyleSheet("QGroupBox{ border: 1px groove grey; border-radius:5px;border-style: inset;}")
        self.ui.station_dates_label.setStyleSheet("QGroupBox{ border: 1px groove grey; border-radius:5px;border-style: inset;}")
        self.ui.ticke_peoples_box.setStyleSheet("QGroupBox{ border: 1px groove grey; border-radius:5px;border-style: inset;}")
        self.ui.ticke_peoples_box_2.setStyleSheet("QGroupBox{ border: 1px groove grey; border-radius:5px;border-style: inset;}")
        self.ui.station_trains_box.setStyleSheet("QGroupBox{ border: 1px groove grey; border-radius:5px;border-style: inset;}")
        self.ui.station_names_box.setStyleSheet("QGroupBox{ border: 1px groove grey; border-radius:5px;border-style: inset;}")
        self.ui.set_types_box.setStyleSheet("QGroupBox{ border: 1px groove grey; border-radius:5px;border-style: inset;}")

    def open(self):
        if not self.isVisible():
            self.show()

    def load_config(self):
        with open(config_path) as f:
            self.conf_dict = yaml.load(f)
        pprint(self.conf_dict)

class Entry(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.ui = Ui_EntryUi()
        self.config = Config()
        self.ui.setupUi(self)

        self.image = QImage('/Users/roc.maple/work/12306/tmp/pic/0.png')
        self.ui.query_btn.setPixmap(QPixmap.fromImage(self.image))

        self.ui.open_config_btn.clicked.connect(self.config.open)

        self.query_ticket_thread = QueryTicketThread()
        self.ui.query_btn.clicked.connect(self.start_query_ticket_thread)

    def start_query_ticket_thread(self):
        self.query_ticket_thread.signOut.connect(self.show_append_log)
        self.query_ticket_thread.start()

    def show_append_log(self, msg):
        self.ui.log_list.addItem(msg)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    entry = Entry()
    entry.show()
    sys.exit(app.exec_())


