from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot


class WebBridge(QObject):
    signal_event_triggered = pyqtSignal(str, str)
    signal_value_submitted = pyqtSignal(str, str)

    @pyqtSlot(str, str)
    def broadcast_event(self, elem_id, event):
        self.signal_event_triggered.emit(elem_id, event)

    @pyqtSlot(str, str)
    def value_submitted(self, elem_id, val):
        self.signal_value_submitted.emit(elem_id, val)