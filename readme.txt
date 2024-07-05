dans cette version, je suis entrain de tester le long_press pour la voix humaine entrante
j'ai reussi a trouver ce superbe code github qui permet de rajouter un evenement long_press sur un clic de boutton kivy
https://gist.github.com/MaddoxRauch/c7ab4df15b5f4cbfd7fad831d31e3248
j'ai remplace le boutton par un MDbutton(heritage de la classe) qui me permet de le mettre dans mon fichier chats2.kv
(faire comme sur busuu)

Utilisation de la fonction listen() de la bibliotheque python speech_recognition:
https://stackoverflow.com/questions/65641455/how-do-i-give-the-time-duration-of-listening-to-python-speech-recognition-librar

Pour lire un fichier audio pour le beep sonore de la voix humaine au demarrage:
https://pypi.org/project/playsound/
ou la bibliotheque pygame.mixer
