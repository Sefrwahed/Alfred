import json

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot


class WebBridge(QObject):
    signal_event_triggered = pyqtSignal(str, str, dict)
    signal_form_submitted = pyqtSignal(str, dict)
    signal_wrong_module = pyqtSignal()

    @pyqtSlot(str, str, str)
    def broadcast_event(self, elem_id, event, attrs):
        self.signal_event_triggered.emit(elem_id, event, json.loads(attrs))

    @pyqtSlot(str, str)
    def form_submitted(self, form_attrs, form_vals):
        self.signal_form_submitted.emit(form_attrs, json.loads(form_vals))

    @pyqtSlot()
    def feedback_toast_clicked(self):
    	self.signal_wrong_module.emit()