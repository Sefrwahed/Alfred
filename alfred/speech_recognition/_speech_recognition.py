import speech_recognition as sr

class SpeechRecognition():
    def __init__(self):
        self.r = sr.Recognizer()
        self.m = sr.Microphone()

    def listen(self):
        try:
            with self.m as source: self.r.adjust_for_ambient_noise(source)
            with self.m as source: self.audio = self.r.listen(source)
            message = self.r.recognize_google(self.audio)
            print("Google Speech Recognition thinks you said " + message)
            return message
            m.__exit__()
            r.__exit__()
        except sr.UnknownValueError:
            #print("Google Speech Recognition could not understand audio")
            return ''
        except sr.RequestError as e:
            #print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return ''
