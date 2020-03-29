print("Enter a sound level in decibel:")
soundLevel: int = int(input())

if soundLevel < 40 :
    print("The decibel level is quitter than a quite room.")
elif soundLevel == 40 :
    print("The decibel level is as quite as a quite room.")
elif soundLevel == 70:
    print("The decibel level is as loud as an alarm clock.")
elif soundLevel == 106 :
    print("The decibel level is as loud as an gas lawnmower.")
elif soundLevel == 130 :
    print("The decibel level is as loud as an gas jackhammer.")
elif soundLevel > 130 :
    print("The decibel level is louder than a jackhammer.")
elif soundLevel > 106 :
    print("The decibel level is between the noise of a gas lawnmower and a jackhammer.")
elif soundLevel > 70 :
    print("The decibel level is between the noise of a alarm clock and a gas lawnmower.")
elif soundLevel > 40:
    print("The decibel level is between the noise of a quite room and a alarm clock.")


