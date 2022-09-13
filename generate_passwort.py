import random
import config
import os
import hashlib

def generate():

    save = random.choice(config.gross_buchstaben)
    
    gross1 = random.choice(config.gross_buchstaben)
    gross2 = random.choice(config.gross_buchstaben)
    gross3 = random.choice(config.gross_buchstaben)
    gross4 = random.choice(config.gross_buchstaben)
    gross5 = random.choice(config.gross_buchstaben)
    save_gross = gross1 + gross2 + gross3 + gross4 + gross5
    
    klein1 = random.choice(config.klein_buchstaben)
    klein2 = random.choice(config.klein_buchstaben)
    klein3 = random.choice(config.klein_buchstaben)
    save_klein = klein1 + klein2 + klein3 + klein1
    
    zahl1 = random.choice(config.zahlen)
    zahl2 = random.choice(config.zahlen)
    save_zahl = zahl1 + zahl2 + zahl1 +zahl2
    
    sonder1 = random.choice(config.sonderzeichen)
    sonder2 = random.choice(config.sonderzeichen)
    sonder3 = random.choice(config.sonderzeichen)
    sonder4 = random.choice(config.sonderzeichen)
    sonder5 = random.choice(config.sonderzeichen)
    save_sonder = sonder1 + sonder2 + sonder3 + sonder4 + sonder5 + sonder1 + sonder2
    
    mix_all = save_klein + save_gross + save_sonder + save_zahl

    mix1 = random.choice(mix_all)
    mix2 = random.choice(mix_all)
    mix3 = random.choice(mix_all)
    mix4 = random.choice(mix_all)
    mix5 = random.choice(mix_all)
    mix6 = random.choice(mix_all)
    mix7 = random.choice(mix_all)
    mix8 = random.choice(mix_all)
    mix9 = random.choice(mix_all)
    mix10= random.choice(mix_all)
    mix11 = random.choice(mix_all)
    mix12 = random.choice(mix_all)

    save_all = mix1 + mix2 + mix3 + mix4 + mix5 + mix6 + mix7 + mix8 + mix9 + mix10 + mix11 + mix12

    if not os.path.exists("output"):
        os.mkdir("output")

    with open(f"output/password.txt", "w") as f:
        f.write(save_all)
    

    
