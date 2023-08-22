import speech_recognition as sr


def voiceLoad():
    global r
    global mic
    r = sr.Recognizer()
    mic = sr.Microphone()

def Answer(language="it", verbose = True):

    if (language == "it"):
        lang_input = "it-IT"
    if (language == "de"):
        lang_input = "de-DE"
    if (language == "en"):
        lang_input = "en-US"  
    
    
    with mic as source:
        print('Speak anything: ')
        audio = r.listen(source)

        #with open("C:/Users/epass/Desktop/gino.wav", "wb") as f:
        #     f.write(audio.get_wav_data())

        try:
            text = r.recognize_google(audio, language=lang_input)
            if verbose:
                print(text)
            return text

        except:
            print('Sorry could not recognize your voice')

