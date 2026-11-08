default letter_opened = False
default message_clicked = False
default guess = ""
default guess_wrong = False
define cipher_answer = "If you want to guess who am I, go to the place we first met and find the quiz!"

image bg table = "images/Backgrounds/bg table.png"
image bg opening = "images/Backgrounds/bg opening ceremony.png"

define audio.love = "audio/love theme.mp3"
define audio.choice = "audio/choice.mp3"

define love_interest = "Billee"
#define love_interest = "Asterlayna"
#define love_interest = "Sterling"

define ans = 0

label love_letter:
    $ letter_opened = False
    $ message_clicked = False

    play music love

    scene bg table:
        zoom 0.75
        yalign 0.5

    show expression "images/items/letter.png" as letter:
        xalign 0.5
        yalign 0.5

    "You were approaching your desk when you noticed the letter on top of your things."

    call screen open_letter

    "Do you want to decipher the last sentence? (P.S thing)"
    menu:
        "Yes":
            play sound choice noloop
            $ guess = ""
            $ guess_wrong = False
            call screen decipher
            if _return:
                "That's it! You decoded the message."
                "If you want to guess who am I, go to the place we first met and find the quiz!..."
                "Do you want to go to the place you first met?"
                menu:
                    "Yes":
                        play music choice noloop
                        scene bg opening:
                            zoom 0.67
                            xalign 0.5
                        with fade

                        "You see the paper note on the seat you sat in during the opening ceremony."
                        "You unfold it and find a set of questions."

                        "Take quiz?"
                        menu:
                            "Yes":
                                $ ans = 0

                                if love_interest == "Billee":
                                    menu:
                                        "What's the second letter of the alphabet?"
                                        "B":
                                            "Correct!"
                                            $ ans += 1
                                        "A":
                                            "Wrong. You'll never find out who this person was."
                                        "C":
                                            "Wrong. You'll never find out who this person was."

                                    menu:
                                        "Commonly used letter to identify the variable in a for loop"
                                        "a":
                                            "Wrong. You'll never find out who this person was."
                                        "i":
                                            "Correct!"
                                            $ ans += 1
                                        "m":
                                            "Wrong. You'll never find out who this person was."

                                    menu:
                                        "Teenagers use this to call someone lame, opposite to W"
                                        "K":
                                            "Wrong. You'll never find out who this person was."
                                        "L":
                                            "Correct!"
                                            $ ans += 1
                                        "N":
                                            "Wrong. You'll never find out who this person was."

                                    menu:
                                        "Electrical Engineers are noted as..."
                                        "ee":
                                            "Correct!"
                                            $ ans += 1
                                        "ce":
                                            "Wrong. You'll never find out who this person was."
                                        "me":
                                            "Wrong. You'll never find out who this person was."

                                elif love_interest == "Asterlayna":
                                    menu:
                                        "What's the first letter of the alphabet?"
                                        "B":
                                            "Wrong. You'll never find out who this person was."
                                        "A":
                                            "Correct!"
                                            $ ans += 1
                                        "C":
                                            "Wrong. You'll never find out who this person was."

                                    menu:
                                        "Highest tier in a typical tier list"
                                        "a":
                                            "Wrong. You'll never find out who this person was."
                                        "s":
                                            "Correct!"
                                            $ ans += 1
                                        "d":
                                            "Wrong. You'll never find out who this person was."

                                    menu:
                                        "Letter that looks like a perpendicular sign upside down"
                                        "K":
                                            "Wrong. You'll never find out who this person was."
                                        "T":
                                            "Correct!"
                                            $ ans += 1
                                        "I":
                                            "Wrong. You'll never find out who this person was."

                                    menu:
                                        "First letter of one of the CSE 115 profs' first name"
                                        "e":
                                            "Correct!"
                                            $ ans += 1
                                        "m":
                                            "Wrong. You'll never find out who this person was."
                                        "s":
                                            "Wrong. You'll never find out who this person was."

                                elif love_interest == "Sterling":
                                    menu:
                                        "Highest tier in a typical tier list"
                                        "A":
                                            "Wrong. You'll never find out who this person was."
                                        "S":
                                            "Correct!"
                                            $ ans += 1
                                        "D":
                                            "Wrong. You'll never find out who this person was."

                                    menu:
                                        "Letter that looks like a perpendicular sign upside down"
                                        "K":
                                            "Wrong. You'll never find out who this person was."
                                        "T":
                                            "Correct!"
                                            $ ans += 1
                                        "I":
                                            "Wrong. You'll never find out who this person was."

                                    menu:
                                        "First letter of one of the CSE 115 profs' first name"
                                        "e":
                                            "Correct!"
                                            $ ans += 1
                                        "m":
                                            "Wrong. You'll never find out who this person was."
                                        "s":
                                            "Wrong. You'll never find out who this person was."

                                    menu:
                                        "First letter of Elizabeth's last name"
                                        "r":
                                            "Correct!"
                                            $ ans += 1
                                        "m":
                                            "Wrong. You'll never find out who this person was."
                                        "s":
                                            "Wrong. You'll never find out who this person was."

                                if ans == 4:
                                    mc "The answers make up their name..."
                                    mc "[love_interest] wrote this letter!"

                            "No":
                                "..."
                    "No":
                        "Why? :("

            else:
                "You don't want to decipher the letter :("
        "No":
            pass
    return


screen open_letter():
    if not letter_opened:
        imagebutton:
            idle "images/items/letter.png"
            hover "images/items/letter.png"
            xalign 0.5
            yalign 0.5
            action SetVariable("letter_opened", True)

    elif not message_clicked:
        imagebutton:
            idle "images/items/letter open.png"
            hover "images/items/letter open.png"
            xalign 0.5
            yalign 0.5
            action SetVariable("message_clicked", True)

    else:
        add "images/items/message.jpg":
            xalign 0.5
            yalign 0.1
        textbutton "Continue":
            xalign 0.5
            yalign 0.95
            action Return()


screen decipher():
    modal True

    add "images/items/cipher.png":
        xalign 0.5
        yalign 0.1
        zoom 1.5

    add "images/items/ps part.png":
        xalign 0.5
        yalign 0.65
        zoom 1.3

    vbox:
        xalign 0.5
        yalign 0.85
        spacing 10

        if guess_wrong:
            text "That's not it. Try again." xalign 0.5 color "#f66"

        frame:
            xminimum 600
            input:
                value VariableInputValue("guess")
                length 300
                copypaste True

        hbox:
            xalign 0.5
            spacing 30
            textbutton "Confirm":
                action If(guess.strip().lower() == cipher_answer.lower(),
                          Return(True),
                          SetVariable("guess_wrong", True))
            textbutton "Give up":
                action Return(False)