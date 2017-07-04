import speech_recognition as sr
from PyQt5.QtCore import QObject, QThread, pyqtSignal, pyqtSlot

class SpeechRecognition(QThread):

    return_msg = pyqtSignal(str)

    def __init__(self):
        QThread.__init__(self) ##Thread
        self.r = sr.Recognizer()
        self.m = sr.Microphone()

    def __del__(self):
        self.wait()

    def listen(self):
        try:
            with self.m as source: self.r.adjust_for_ambient_noise(source)
            with self.m as source: self.audio = self.r.listen(source)
            message = self.r.recognize_google(self.audio)
            print("Google Speech Recognition thinks you said " + message) ##Debug
            self.return_msg.emit(message)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio") ##Debug
            self.return_msg.emit('')
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e)) ##Debug
            self.return_msg.emit('')

    def run(self):
        self.listen()
