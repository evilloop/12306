import threading
import time
from init import select_ticket_info_for_gui as select_ticket_info


class QueryTicketThread(threading.Thread):
    def __int__(self):
        threading.Thread.__init__(self)

    def run(self):
        select_ticket_info.select().main()
