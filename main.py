import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)

    try:
        ses = r.listen(source, timeout=5, phrase_time_limit=2)
        print(r.recognize_google(ses, language='tr-tr'))
    except sr.WaitTimeoutError:
        print("Dinleme zaman aşımına uğradı")

    except sr.UnknownValueError:
        print("Ne dediğini anlayamadım")