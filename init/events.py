import wx


class NotifyMainWindowEvent(wx.PyCommandEvent):
    def __init__(self, evtType, id):
        wx.PyCommandEvent.__init__(self, evtType, id)
        self.eventArgs = ""

    def GetEventArgs(self):
        return self.eventArgs

    def SetEventArgs(self, args):
        self.eventArgs = args


EVT_TYPE_NOTIFY_MAIN_WINDOW = wx.NewEventType()
EVT_BINDER_NOTIFY_MAIN_WINDOW = wx.PyEventBinder(EVT_TYPE_NOTIFY_MAIN_WINDOW, 1)
