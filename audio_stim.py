from gtts import gTTS

language = 'en'

for number in range(0,10):
    item = gTTS(text=str(number), lang=language, slow=False)
    item.save("C:/Users/epass/OneDrive/ANALYSES/AIS/dual_task/audio/number_" + language + "_" + str(number) + ".mp3")