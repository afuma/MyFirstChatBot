# code de test pour convertir un vocal en texte en direct.
# le code fonctionne correctement, mais l'API de google mais parfois 5 a 10 secondes pour donner une response
# la cause est peut-être le connexion internet lente du logement

import speech_recognition as sr

def ft_microphone():
    micros = sr.Microphone.list_microphone_names()
    for index, micro in enumerate(micros):
        if (micro == "default"):
            index_micro = index
            break
    mic = sr.Microphone(device_index=index_micro)

    return mic

mic = ft_microphone()
while True:
    r = sr.Recognizer()
    with mic as source:
        print("\n Listening...")
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
    print("no longer listening")
    try:
        user_input = r.recognize_google(audio)
        print(user_input)
    except:
        continue
    print("fin du message")