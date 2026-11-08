
image bg davis_outside = "images/Backgrounds/bg davis entrance.png"
image bg davis_outside_rain = "images/Backgrounds/bg davis entrance rain.png"
image bg davis_1st = "images/Backgrounds/bg davis 1st floor.png"

define cat = Character("Cat", color= "#d53535")

image alien neutral = "images/Characters/AlienNeutral.png"
image alien angry = "images/Characters/AlienAngry.png"
image alien flustered = "images/Characters/AlienFlustered.png"
image alien happy = "images/Characters/AlienHappy.png"
image alien upset = "images/Characters/AlienUpset.png"

default psdb = [
    [0.2, 0.5],
    [0.5, 0.5],
    [0.8, 0.5],
    [0.3, 0.7],
    [0.7, 0.7]
]

default clicks_easy = 0
default clicks_mid = 0
default clicks_hard = 0

default wrapped_kitty = False

label chase_cat:

    scene bg davis_outside:
        zoom 0.5
        yalign 0.5

    show expression "cat/Cat Front.png" as cat:
        xalign 0.5
        yalign 0.7

    $ clicks_easy = 0
    $ clicks_mid = 0
    $ clicks_hard = 0

    mc "Hey there!"

    "You know this cat...."
    mc "This cat looks like Zephyr's cat..."
    mc "Nvm, that cute cat is in LONG ISLAND! (Best island in the best state - Ethan Blanton)"

    "You need to catch this!"
    "Try to click on the cat at least 30 times until the timer dies."
    "You have little time to do it! .. so keep eyes on the cat :)"

    hide cat

    call screen cat_game_easy

    if _return != "won":
        "Uhmmmmm How old are uuu????"
        call c322
        return

    "That was easy!"
    "Keep chasing the cat."

    call screen cat_game_mid

    if _return != "won":
        "Uhmmmmm How old are uuu????"
        call c322
        return

    "Still doable!! Stilll like the cat?"
    "Keep chasing the cat."

    call screen cat_game_hard

    if _return == "won":
        "You cought the cat! YAY! :)"
        call c321
    else:
        "You didn't catch the cat on time! Oh naur! :("
        call c322

    return


screen cat_game_easy():

    modal True

    default time_left = 15
    default cLoc = renpy.random.randint(0, len(psdb) - 1)

    timer 1 repeat True action If(
        time_left > 1,
        SetScreenVariable("time_left", time_left - 1),
        Return("timeout")
    )

    timer 1 repeat True action SetScreenVariable(
        "cLoc",
        renpy.random.randint(0, len(psdb) - 1)
    )

    frame:
        xalign 0.5
        yalign 0.03
        background "#ffffff"
        padding (20, 10)

        hbox:
            spacing 60

            text "Clicks: [clicks_easy]/30" color "#000000" size 30
            text "Time: [time_left]" color "#000000" size 30

    imagebutton:
        idle "cat/Cat Front.png"

        xalign psdb[cLoc][0]
        yalign psdb[cLoc][1]

        action If(
            clicks_easy >= 29,
            [
                SetVariable("clicks_easy", 30),
                Return("won")
            ],
            SetVariable("clicks_easy", clicks_easy + 1)
        )


screen cat_game_mid():

    modal True

    default time_left = 15
    default cLoc = renpy.random.randint(0, len(psdb) - 1)

    timer 1 repeat True action If(
        time_left > 1,
        SetScreenVariable("time_left", time_left - 1),
        Return("timeout")
    )

    timer 0.65 repeat True action SetScreenVariable(
        "cLoc",
        renpy.random.randint(0, len(psdb) - 1)
    )

    frame:
        xalign 0.5
        yalign 0.03
        background "#ffffff"
        padding (20, 10)

        hbox:
            spacing 60

            text "Clicks: [clicks_mid]/30" color "#000000" size 30
            text "Time: [time_left]" color "#000000" size 30

    imagebutton:
        idle "cat/Cat Front.png"

        xalign psdb[cLoc][0]
        yalign psdb[cLoc][1]

        action If(
            clicks_mid >= 29,
            [
                SetVariable("clicks_mid", 30),
                Return("won")
            ],
            SetVariable("clicks_mid", clicks_mid + 1)
        )



screen cat_game_hard():

    modal True

    default time_left = 15
    default cLoc = renpy.random.randint(0, len(psdb) - 1)

    timer 1 repeat True action If(
        time_left > 1,
        SetScreenVariable("time_left", time_left - 1),
        Return("timeout")
    )

    timer 0.5 repeat True action SetScreenVariable(
        "cLoc",
        renpy.random.randint(0, len(psdb) - 1)
    )

    frame:
        xalign 0.5
        yalign 0.03
        background "#ffffff"
        padding (20, 10)

        hbox:
            spacing 60

            text "Clicks: [clicks_hard]/25" color "#000000" size 30
            text "Time: [time_left]" color "#000000" size 30

    imagebutton:
        idle "cat/Cat Front.png"

        xalign psdb[cLoc][0]
        yalign psdb[cLoc][1]

        action If(
            clicks_hard >= 24,
            [
                SetVariable("clicks_hard", 25),
                Return("won")
            ],
            SetVariable("clicks_hard", clicks_hard + 1)
        )

label c321:
    show alien happy:
        zoom 0.5
        xalign 0.1
    show expression "cat/Cat Front.png" as cat:
        xalign 0.5
        yalign 0.7

    "You caught the stray kitty."

    "They'd hold the scared little cat, gently cooing at the kitty and petting its soft little head."

    show alien neutral:
        zoom 0.5
        xalign 0.1

    b "There there little guy.. Don't be scared."

    "It's unclear how soothing Billee's methods are to the kitten but he stays put in Billee's arms."

    mc "Not to be the bearer of bad news, but what are we gonna do with him?"

    b "They'd pause for a moment, thinking. Then they'd look down at the cat again. I don't know."

    "The sky decided not to give you the time to really think about that. A drop of water would fall, then another."

    show bg davis_outside_rain:
        zoom 0.5
    with dissolve

    b "Shoot."

    b "We should start by finding cover."

    "Before you even have the chance, those few drops would turn to a downpour."

    "They'd quickly cover the kitty with their body, shielding it from the rain."

    b "C'mon!" 
    
    "They'd get up and would take off running for cover under the nearest building."

    scene bg davis_1st:
        zoom 0.67
        xalign 0.5
    with fade


    show alien neutral:
        zoom 0.5
        xalign 0.1
    show expression "cat/Cat Front.png" as cat:
        xalign 0.5
        yalign 0.7

    "Soon you two were huddled under a random overhang, with a scared kitty clutched to Billee's chest."

    cat "Mrow..."

    b "Shhh, I'm sorry for scaring you again."

    mc "You'd look at the rain, thinking about how it would be an issue for the kitty."

    menu:
        "Wrap the kitty in your hoodie to keep it safe and warm":

            $ wrapped_kitty = True
            $ bil += 2

            "The kitty would purr softly, being wrapped in the warm embrace of the hoodie."

            "Still, you and Billee were sitting under a random building overhang, with a cat wrapped in your hoodie."

        "Try to convince Billee to let the cat go":

            $ wrapped_kitty = False
            $ bil -= 1

            b "No way! This poor little guy shouldn't be out in the rain."

            "It's clear Billee isn't going to let the cat go."

            "But the problem is that you two are under a random building overhang, with a cat."

    mc "Sigh. Alright."

    mc "What's the plan then."

    b "They'd blink, thinking before a smirk came across their face."

    b "I'll call my mom!"

    b "They'd take out their phone, dialing their mother's number."

    b "I don't live far from campus, and we already have 2 cats.. What's one more?"

    "Billee's mom would answer and they'd explain the situation to her over the phone."

    "A long sigh would come out of Billee's speakers, but they'd smile. She was clearly coming to take the little kitten back to their house."

    show alien happy:
        zoom 0.5
        xalign 0.1

    b "Well, now we just wait for like, 10 minutes."

    "It seems that all's well that ends well."


    if bil > 5:

        "A few minutes would pass. Billee glancing between you and the kitty cradled in their arms."

        b "They'd grab your hand. You can sit down, no need to stand for this long."

        "Convinced by their antics, you sit down next to Billee."

        b "They'd take your hand, bringing it close to the kitten's face."

        "The kitty would sniff your hand before butting its head against you. Its soft fur tickling your skin."

        b "In a gentle voice. It seems like he likes you."

        "You gently move your hand to pet the kitten's head, enjoying the affection of a kitty."

        "You'd notice that Billee was staring more at you than at the kitten in their arms."

        b "They'd stare at you, a dopey smile and flushing cheeks crossing their cheeks."

        b "You know [mcname].. I thought this hackathon would suck."

        b "They'd chuckle softly, but would scoot a little closer to you."

        b "I only signed up because all my professors were pushing it so much. But I'm glad I came."

        b "They'd smile at [mcname]. I'm glad I met you, [mcname]. You've made all this such a wonderful experience."

    "Ten minutes would pass in the blink of an eye. A car would pull up across from where you two were sitting on the road."

    "Billee would stand up, walking over and sheltering the kitten from the rain."

    "They'd hand the kitty to their mom, would thank her for coming and then would come back to where you were."

    if wrapped_kitty:

        "Billee would hand your hoodie back to you, slightly covered in cat hair and damp."

    b "Alright, we better get back to the hackathon! Lunch is definitely over."

    mc "Definitely."

    b "Welp. Hope you're ready to make a run for it!"

    "They'd take off into the rain, running towards the building the hackathon is in."

    mc "Hey! Wait up!"

    "Then you were taking off after them."

    return



label c322:
    
    show alien neutral:
        zoom 0.5
        xalign -0.1

    "You lost the cat minigame."

    show alien upset:
        zoom 0.5
        xalign -0.1

    b "Oh man! We lost him…"

    mc "Well, you win some you lose some."

    show alien angry:
        zoom 0.5
        xalign -0.1

    b "I guess. SIGH!"

    show alien neutral:
        zoom 0.5
        xalign -0.1

    "Billee would stare at they sky for a minute or two, before looking back at you."

    show alien happy:
        zoom 0.5
        xalign -0.1

    b "No point in dwelling on it! We still have time before the warden demands us back in our cells!"

    mc "Warden?"

    show alien neutral:
        zoom 0.5
        xalign -0.1

    b "Sterling! He's been soooo uptight this whole time."

    b "Mocking Sterling. Ok, so you're a weak link."

    "It's true that Sterling's been a bit mean to the other members of the group this whole time."

    mc "Why don't we talk to him when we get back then?"
    show alien happy:
        zoom 0.5
        xalign -0.1

    b "They'd smile. That sounds like a good plan."

    "Before either of you really had the chance to say more, a drop then another would fall from the sky."

    show bg davis_outside_rain:
        zoom 0.5
    with dissolve

    show alien upset:
        zoom 0.5
        xalign -0.1
    
    b "I saw that it was overcast, but I didn't think it would start raining."

    "In an almost cartoonish fashion, the rain would suddenly begin to downpour."

    show alien neutral:
        zoom 0.5
        xalign -0.1

    b "Yikes! Come on!"

    "Billee would call to you as they entered the davis hall."

    scene bg davis_1st:
        zoom 0.67
        xalign 0.5
    with fade

    "You'd follow them, also ducking under what seemed to be the only dry spot left outside."
    

    "Billee was panting beside you, before starting to laugh."

    show alien happy:
        zoom 0.5
        xalign -0.1

    b "Well, I guess our plans of eating outside got.. Washed down the drain??"

    "They had an almost too pleased smile on their face. Too happy about their own bad pun."


    menu:
        "That was terrible":

            $ bil += 1

        "I think we just got flushed out.":

            $ bil += 2

    "Billee would smile even wider."

    show alien neutral:
        zoom 0.5
        xalign -0.1

    b "Well.. what to do now?"

    "A few minutes seemed to stretch an eternity as the two of you stood there, contemplating your next move."


    if bil > 5:
        show alien flustered:
            zoom 0.5
            xalign -0.1
        b "They'd stare at you, a dopey smile and flushing cheeks crossing their cheeks."

        b "You know [mcname].. I thought this hackathon would suck."

        b "They'd chuckle softly, but would walk to be a little closer to you."

        b "I only signed up because all my professors were pushing it so much. But I'm glad I came."

        show alien happy:
            zoom 0.5
            xalign -0.1

        b "They'd smile at [mcname]. I'm glad I met you, [mcname]. You've made all this such a wonderful experience."

        "Their sudden confession would make your face split into a smile."

        mc "I'm glad I met you too Billee. Hopefully we'll all make friends that will last us a while."

        show alien flustered:
            zoom 0.5
            xalign -0.1

        b "Their face would be flushed."

        b "Yeah. Just friends.."

    show alien neutral:
            zoom 0.5
            xalign -0.1
    b "Well.. do you want to brave the storm and make it back inside?"

    mc "Yeah. Let's get back to the Hackathon."

    return
