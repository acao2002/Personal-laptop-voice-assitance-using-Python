import speech_recognition as sr

class VoiceAI: 

    r = sr.Recognizer()
    mic = sr.Microphone()

    def Listen(self): 
        
        with self.mic as source:
            self.r.adjust_for_ambient_noise(source)
            self.input = self.r.listen(source) 

    def Recognize(self):
        try: 
            self.outputText = self.r.recognize_google(self.input)
            return self.outputText
        
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return 0
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return 0

VoiceAI = VoiceAI()

'''
while True:
    print("say sth")
    VoiceAI.Listen()
    print(VoiceAI.Recognize())
'''    


    
