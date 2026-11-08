# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Billee", color= "#00ff00")
define a = Character("Asterlayna",color = "#00bfff")
define s = Character("Sterling", color = "#c800ff")

define mc = Character("[mcname]")
default pronouns = []

default project = None
#Affection point tracker
default sterl = 0
default bil = 0
default aster = 0

screen timer(duration, target_label):
    timer duration action [Hide("timer"), Jump(target_label)]


# The game starts here.

label start:

    #Scene 0
    $ mcname = renpy.input("What is your name?", length=32)
    $ mcname = mcname.strip()
    menu choosePronouns:
        "Please chose your pronouns"
        "He/Him":
            $ pronouns = ["he","him","his","himself"]
        "She/Her":
            $ pronouns = ["she","her","her","herself"]
        "They/Them":
            $ pronouns = ["they","them","their","themselves"]
    
    #call c1
    #call c2
    #call c3
    
    #call chase_cat
    call love_letter
        

    return

label c1:
    #Scene 1
    define mystb = Character("Mystery Person", color= "#00ff00")
    define mysta = Character("Mystery Girl",color = "#00bfff")
    define mysts = Character("Mystery Boy", color = "#c800ff")

    scene bg opening ceremony:
        zoom 0.75
        yalign 0.5

    "Your morning was spent wandering around the hall the Hackathon is being hosted in, attending a career fair, and then going to Opening Ceremonies."

    "The student organizers stand at the front of the lecture hall, microphones in hand speaking to all the participants."

    "Hackathon Official" "Alright. That’s the end of what we have for kick off. Good luck everyone!"

    mc "Dang.. I don’t know anyone here, and I have to make a project in 24 hours.. I have no clue what to do either."
    
    show star neutral:
        zoom 0.5
        xalign 0.5
    
    mysta "Hey you seem lost. Need a group?"

    "You see a girl with blue braids waving to you. She was sitting a few chairs away from you during the kickoff meeting, and you think you’ve seen her before in your CS classes."

    show star happy:
        zoom 0.5
        xalign 0.5
    mysta "I’m Asterlayna, but you can just call me Lay."

    show star neutral:
        zoom 0.5
        xalign 0.5

    a "Lets see who else we can find. We can have up to 4 people in our group."
    #If you have time make a shocked expression for Asterlayna here
    a "Shoot I totally forgot to ask your name."

    mc "It's alright, I’m [mcname]."
    show star happy:
        zoom 0.5
        xalign 0.5
    a "Alright, nice to meet you [mcname]! Now lets try and find 2 people for our group."
    
    show star neutral:
        xalign -0.5
    with move
    
    "Looking around the meeting room, you spot two others, hovering nearby. They both seem like they need a group to be in."

    a "Why don’t you go talk to tall and dark over there, and I’ll ask the silly one, then we meet back up."

    mc "Sounds good."

    hide star neutral
    "The two of you split up, Asterlayna heading towards someone with brown and green hair. You find yourself heading towards a stoic guy with glasses."

    mc "Excuse me, do you need a group?"

    show satellite neutral:
        zoom 0.5
        xalign 0.5
    mysts "{i}scoff.{/i} Need is a strong word."

    mc "{i}Well that’s rude.{/i}"

    mc "Alright, well in that case.."
    #Another good spot for a shocked expression
    mysts "Wait!!"

    mysts "Ahem."
    
    mysts "It would make my work load far lighter if I was in a group, so I suppose it would be beneficial for me to join yours."

    mc "Alright then, I’m [mcname]. You are?"
    
    show satellite happy:
        zoom 0.5
        xalign 0.5
    mysts "Sterling. Sterling Kitadai."

    mc "{i}Who introduces themself with their first and last name?{/i}"

    show satellite neutral:
        zoom 0.5
        xalign 0.5

    s "Forget it. Where’s the rest of your group."

    mc "C’mon."
    hide satellite angry
    with moveoutright
    "The two of you walk to the front of the lecture hall, where Asterlayna and your 4th member are waiting."
    show star happy:
        zoom 0.5
        xalign 1.5
    show alien neutral:
        zoom 0.5
        xalign 0.5
    show satellite neutral:
        zoom 0.5
        xalign -0.5
    a "Oh cool! You got icy."
    show star neutral:
        zoom 0.5
        xalign 1.5
    show alien happy:
        zoom 0.5
        xalign 0.5
    "The other person would snicker a little."
    show alien neutral:
        zoom 0.5
        xalign 0.5
    a "Introductions are in order. I’m Asterlayna, you can call me Lay. She/Her."

    mystb "Nice to meet the rest of you, I’m Billee, They/Them."

    mc "I’m [mcname], I use [pronouns[0]]/[pronouns[1]] pronouns."
    show star upset:
        zoom 0.5
        xalign 1.5
    "The whole group would turn and look at Sterling, waiting for him to introduce himself."

    s "Sterling Kitadai. He/Him. Now if you’re all done wasting time getting to know each other, we need to chose a project."
    show star neutral:
        zoom 0.5
        xalign 1.5
    s "Now, I’ve already began formulating a project."
    show star happy:
        zoom 0.5
        xalign 1.5
    a "No way! Me too! I have an idea"
    show alien happy:
        zoom 0.5
        xalign 0.5
    b "Me three, what did you guys have in mind?"

    mc "{i}Am I the only one who came unprepared?{/i}"
    
    show alien neutral:
        zoom 0.5
        xalign 0.5
    a "Well my idea was–"

    show star upset:
        zoom 0.5
        xalign 1.5
    s "We’re going with my idea. A Sleep quality analyzer using phone sensor data."

    b "I don’t think that’s how democracy works."
    show star angry:
        zoom 0.5
        xalign 1.5
    a "Excuse you." 
    show star neutral:
        zoom 0.5
        xalign 1.5
    a "As I was saying. My idea is to make a Smart Plant Watering System."

    a "We’d need some hardware parts, but I think we can borrow them from the hackathon."
    show satellite angry:
        zoom 0.5
        xalign -0.5
    s "That sounds like a stupid idea, and it’s already been done before."
    show satellite neutral:
        zoom 0.5
        xalign -0.5
    show star upset:
        zoom 0.5
        xalign 1.5
    a "Like your sleep quality analyzer hasn’t?"
    show alien upset:
        zoom 0.5
        xalign 0.5
    show satellite angry:
        zoom 0.5
        xalign -0.5
    s "It’s a more sophisticated project!"
    show star angry:
        zoom 0.5
        xalign 1.5
    show satellite neutral:
        zoom 0.5
        xalign -0.5
    a "It’s been done a million times. I think my dad has an app for that on his phone."
    show star neutral:
        zoom 0.5
        xalign 1.5
    show satellite angry:
        zoom 0.5
        xalign -0.5
    s "Well we don’t have to reinvent the wheel. But at least my idea is more advanced than an automated sprinkler."
    show star upset:
        zoom 0.5
        xalign 1.5
    show satellite neutral:
        zoom 0.5
        xalign -0.5
    a "Uh huh. I’m {i}sure it is.{/i}"
    show star neutral:
        zoom 0.5
        xalign 1.5
    show alien neutral:
        zoom 0.5
        xalign 0.5
    mc "Why don’t we cool it for a bit. Billee what’s your idea?"
    
    b "My idea? I mean it’s not as sophisticated as a snore counter, but I thought it could be fun to make a Habit tracker, with streaks."
    show alien happy:
        zoom 0.5
        xalign 0.5
    b "It could display on your phone screen and the better your habits the better you’ll feel by having a cooler thing on your phone."
    show alien upset:
        zoom 0.5
        xalign 0.5
    show satellite angry:
        zoom 0.5
        xalign -0.5
    s "Another silly idea. You guys seriously think either of these can win?"
    
    mc "Maybe winning is the friends we made along the way."
    show alien neutral:
        zoom 0.5
        xalign 0.5
    s "Right..."

    b "[mcname], do you have a project idea?"
    
    mc "Oh, no I didn’t come up with one. I just came here to vibe(code)."
    show satellite angry:
        zoom 0.5
        xalign -0.5
    s "Unbelievable"
    show satellite neutral:
        zoom 0.5
        xalign -0.5
    b "Well since you don’t have a project idea why don’t you choose?"

    a "Yeah [mcname] would be a neutral party"

    s "This is ridiculous and we should’ve started working by now."
    show star angry:
        zoom 0.5
        xalign 1.5
    a "Oh hush rocket boy, which project do you think we should make?"

    menu chooseProject:
        "Which Project do you want to make?"
        "Asterlayna’s Smart Plant Watering System":
            $ project = "Watering System"
            $ aster += 2
            $ sterl -= 1
        "Billee’s Habit tracker with streaks":
            $ project = "Habit Tracker"
            $bil += 2
            $sterl -= 1
        "Sterling’s Sleep quality analyzer using phone sensor data":
            $ project = "Sleep quality analyzer"
            $ sterl += 2
    

    return

label c2:
    #Scene 2
    #Sterling is always angry
    #Sterling doesn't disappear
    
    scene bg opening ceremony:
        zoom 0.75
        yalign 0.5
    show star happy:
        zoom 0.5
        xalign 1.5
    show alien neutral:
        zoom 0.5
        xalign 0.5
    show satellite neutral:
        zoom 0.5
        xalign -0.5
    a "Great, now that we’ve got a project chosen lets get to it!"
    show star neutral:
        zoom 0.5
        xalign 1.5
    if(project == "Sleep quality analyzer"):
        show satellite happy:
            zoom 0.5
            xalign -0.5
        s "I knew you’d make the right decision."
    show satellite neutral:
        zoom 0.5
        xalign -0.5
    s "We’ve wasted enough time. Let’s get to work."

    "Hackathon Official" "Alright! It’s time. Hacking starts now! Get going hackers!"

    "The group would take off, finding a nice table in the hall to set up and get working."
    scene bg davis table:
        zoom 0.75
        yalign 0.5
    with dissolve
    show star neutral:
        zoom 0.5
        xalign 1.5
    show alien neutral:
        zoom 0.5
        xalign 0.5
    show satellite neutral:
        zoom 0.5
        xalign -0.5
    "You landed at a corner table."

    "Asterlayna would pull out a computer covered in stickers."

    "Billee’s computer is very similar, though their stickers are more memes and cats."

    "Sterling, ever serious, pulls out a completely barren, high end computer."

    mc "Wow, both your computers are so decorated!"
    show star happy:
        zoom 0.5
        xalign 1.5
    a "Aww thanks! I can tell you about all the stickers on mine."
    show alien happy:
        zoom 0.5
        xalign 0.5
    b "Me too! Though, I think mine are mostly because I thought they’re funny."
    show star neutral:
        zoom 0.5
        xalign 1.5
    show alien neutral:
        zoom 0.5
        xalign 0.5
    show satellite angry:
        zoom 0.5
        xalign -0.5
    s "This is not productive, and we don’t have enough time for this."

    menu chooseWork:
        "Loosen up Grumpy Pants":
            $ aster += 1
            $ bil += 1
            $ sterl -= 1
            show star happy:
                zoom 0.5
                xalign 1.5
            a "Haha! You heard the group leader. We have time for some silliness."
            show star neutral:
                zoom 0.5
                xalign 1.5
            show satellite angry:
                zoom 0.5
                xalign -0.5
            s "So [mcname] is the group leader now?"
            show alien happy:
                zoom 0.5
                xalign 0.5
            show satellite neutral:
                zoom 0.5
                xalign -0.5
            b "Why not? [pronouns[0]] chose which project we’re doing."
            show alien neutral:
                zoom 0.5
                xalign 0.5
            mc "I don’t think we need a group leader."
        
        "Maybe a different time.":
            a "Alright, I’ll tell ya about them later."

            s "Good, lets start working."
        
        "Sterling’s right, we need to get to work":
            $ sterl += 2
            show star upset:
                zoom 0.5
                xalign 1.5
            show alien upset:
                zoom 0.5
                xalign 0.5
    show star neutral:
        zoom 0.5
        xalign 1.5
    show alien neutral:
        zoom 0.5
        xalign 0.5
    s "Let’s start by dividing up the work. Then each of us can work on our own bit."

    a "Alright, how do we want to divy it up?"

    s "The most logical way is based on everyone’s strengths and weaknesses. How much experience do you have with programming?"
    show alien upset:
        zoom 0.5
        xalign 0.5
    b "Not much? This is my first real programming class. But I was big into minecraft as a kid."   
    
    s "That’s not programming."

    b "It is if you do stuff with commands."
    
    s "Ok, so you’re a weak link. What about you Asterlayna?"
    show alien neutral:
        zoom 0.5
        xalign 0.5
    
    a "Just Lay is fine."

    a "I don’t have as much experience with programming, but I’ve built little Arduino projects before."
    
    if(project == "Watering System"):
        s "Alright, that could be useful."
    else:
        s "Not applicable to our projects."

    s "Alright, what about you [mc]?"

    menu beginnerornah:
        "I’m a beginner":
            s "So I’m the only one of us with any real programming experience."
        "I’ve done a bit here and there":
            s "Good at least two of us will have an idea."
            $ sterl += 1
    
    b "Judgey much. {i}Billee rolls their eyes.{/i}"
    show satellite angry:
        zoom 0.5
        xalign -0.5
    "Sterling would glare at Billee, but the group would get to work."
    show satellite neutral:
        zoom 0.5
        xalign -0.5
    "The group would spend their next hour breaking down their project into bits, and assigning each member a focus area."

    a "Alright then, lets get to work!"
    #Coding Minigame
    return

    
label c3:
    #Scene 3
    scene bg davis table:
        zoom 0.75
        yalign 0.5
    show star neutral:
        zoom 0.5
        xalign 1.5
    show alien neutral:
        zoom 0.5
        xalign 0.5
    show satellite neutral:
        zoom 0.5
        xalign -0.5
    "You’ve all been sitting in the same spot, hunched over computers for the last hour."
    show star upset:
        zoom 0.5
        xalign 1.5
    a "Uuuuggghhhh"
    show star neutral:
        zoom 0.5
        xalign 1.5
    s "{i}His face twitches in annoyance{/i} Asterlayna, that’s incredibly distracting."
    
    a "Good. We need a break."
    show alien upset:
        zoom 0.5
        xalign 0.5
    b "I agree. We’ve been sitting here, plunking away for the last hour."
    show alien neutral:
        zoom 0.5
        xalign 0.5
    show satellite angry:
        zoom 0.5
        xalign -0.5

    s "In case you don’t remember how Hackathons work, we’re on a very strict deadline."
    show satellite neutral:
        zoom 0.5
        xalign -0.5
    show alien angry:
        zoom 0.5
        xalign 0.5
    b "Yeah, but sitting here code blocked isn’t gonna help us be productive."
    show alien neutral:
        zoom 0.5
        xalign 0.5
    a "Y’all can do whatever you want. I’m going to go get food."
    
    show star neutral:
        xalign 100
    with move
    hide star neutral
    
    b "I need to stretch my legs."
    show alien neutral:
        xalign 100
    with move
    hide alien neutral

    menu lunchchoice:
        "What will you do with your lunchtime?"
        "Follow Asterlayna":
            jump c3_1
        "Follow Billee":
            jump c3_2
        "Stay with Sterling":
            jump c3_3

    return

label c3_1:
    #Scene 3.1
    scene bg hackathon:
        zoom 0.75
        yalign 0.5
    with dissolve
    "You follow Asterlayna to the tables full of free food provided to hackathon students. She’d notice you following behind her and would turn to you."
    show star happy:
        zoom 0.5
        xalign 0.5
    a "Oh hey [mcname]! Decided to come get lunch with me huh?"
    show star neutral:
        zoom 0.5
        xalign 0.5
    mc "You’re right, it’s no fun to code on an empty stomach."

    a "Exactly. Taking breaks is important for everyone."

    a "What do you think so far? Having fun?"

    menu enjoymentquestion:
        "{i}sarcastically{/i} Yeah, coding for an hour is lots of fun.":
            $ aster += 0
        "Not really.":
            $ sterl += 0
    show star upset:
        zoom 0.5
        xalign 0.5
    a "Well, maybe I can make our break more fun."
    hide star upset
    "The two of you would get your lunch, and then Asterlayna would drag you outside. Walking around campus, she’d bring you to a nice courtyard to eat outside."
    scene bg table close:
        zoom 0.5
        yalign 0.8
    with dissolve

    show star neutral:
        zoom 0.5
        xalign 0.5
    a "{i}Settling down on a bench, she’d pull you down next to her to eat.{/i}"

    "For a moment the two of you eat in silence, letting the peace of nature wash over you."
    show star upset:
        zoom 0.5
        xalign 0.5
    a "Do you care about winning?"

    menu winningquestion:
        "Of course!":
            $ aster -= 1
            a "{i}She’d nod, before continuing.{/i} Well then, I’ll take this more seriously."
        "Not really...":
            $ aster += 2
            show star happy:
                zoom 0.5
                xalign 0.5
            a "{i}She’d nod to you, smiling.{/i} That’s how I feel."
        "What’s this about?":
            $ aster += 1
    show star neutral:
        zoom 0.5
        xalign 0.5
    a "I came to the hackathon to make connections. I wanted to meet new people, make friends, you know the gist."
    show star upset:
        zoom 0.5
        xalign 0.5
    a "{i}She’d sigh. {/i}Though, we ended up with Princess Hackathon."

    menu aboutSterling:
        "Sterling isn’t that bad.":
            $ aster -= 1
            show star angry:
                zoom 0.5
                xalign 0.5
            a "Sure he isn’t. He’s just spent the entire time steam rolling us, and being a jerk."
            
            mc "Maybe he has his reasons."
            show star upset:
                zoom 0.5
                xalign 0.5
            a "I don’t care what his reasons are. There’s no reason for him to be rude."
        "He is a little up tight.":
            $ aster += 1
            show star angry:
                zoom 0.5
                xalign 0.5
            a "Exactly! He’s been mean this whole time."
    
    mc "Why don’t we talk to him about his attitude when we get back?"
    show star neutral:
        zoom 0.5
        xalign 0.5
    a "{i}She’d nod.{/i} Yeah that sounds good."

    "The two of your would continue to eat lunch, the sky slowly growing darker."
    show bg table close gloomy:
        zoom 0.5
        yalign 0.8
    with dissolve
        
    "You’d feel a drop of water fall on you, then another, and another"

    mc "I think it’s starting to rain."
    show star upset:
        zoom 0.5
        xalign 0.5
    a "{i}She’d frown {/i}Nooo.. I hate getting wet."
    
    mc "Lets head back inside then."
    show bg table close rain:
        zoom 0.5
        yalign 0.8
    with dissolve
    
    "The two of you collect your garbage, but before you get the chance to make it to shelter, the rain comes down hard."
    
    a "Ah!"

    menu rainchoice:
        "Run for it!":
            $ aster -= 1
            "You take off, running towards the nearest building. Asterlayna is stunned for a moment, before following you into the nearest building."
        "Come with me!":
            $ aster += 1
            "You grab Asterlayna’s hand, pulling her up from the bench and running towards the nearest building. You’re both wet, but not nearly as wet as you would be if you stayed at the bench any longer."
        "Give her your hoodie":
            $ aster += 2
            "You take your hoodie off, draping it over her head and shoulders to block the down pour."

            a "Wait, but what about you?"

            mc "A little rain never hurt no one. C’mon let’s get to cover."
            show star flustered:
                zoom 0.5
                xalign 0.5
            "You take her hand, running to the nearest building and taking cover."
    scene bg furnas front gloom:
        zoom 0.75
        yalign 0.5
    with fade
    show star upset:
        zoom 0.5
        xalign 0.5
    "Standing under the overhang of a nearby building the two of you watch the falling rain. It beats down upon the ground, and the two of you stand alone in the small dry pocket you’ve found."

    mc "Well what now?"

    a "{i}She’d take a deep breath, then another. {/i}I.. don’t know."

    "It was clear that she didn’t want to go out in the rain again. The wet feeling of her skin and clothes causing agitating her as is."

    if(aster >= 5):
        a "{i}She’d look around, and would see that there was no one else outside.{/i}"
        show star neutral:
            zoom 0.5
            xalign 0.5
        a "Guess we’re the only ones crazy enough to be outside in this rain."

        "For a moment, silence would stretch between you two. Then Asterlayna would look into your eyes."
        show star flustered:
            zoom 0.5
            xalign 0.5
        a "Hey MC… I just want to say.."

        a "{i}She’d take a deep breath, clearly nervous{/i}. Well… I’ve really enjoyed working with you so far."

        "It’s a bit of a strange comment. But you don’t think too much about it."

        mc "Thanks."

        a "Yeah.. I hope you’ve enjoyed working with me too."

        a "{i}She gulps before going settling back into her usual chill attitude.{/i}"
        show star neutral:
            zoom 0.5
            xalign 0.5
        a "We should probably get back to the Hackathon."

        "Despite her words, one problem weighs on both your minds. How to get back to the building without getting soaked by the rain."

        mc "I guess we’re braving the rain."
        show star upset:
            zoom 0.5
            xalign 0.5
        a "Alright. Let’s run."
    show star upset:
        zoom 0.5
        xalign 0.5
    "The two of you rush back to the Hackathon, trying not to get any more wet"
    hide star upset
    with moveoutleft
    return

label c3_2:
    #Scene 3_2
    scene bg davis entrance:
        zoom 0.75
        yalign 0.5
    "Billee walks outside, just wandering around for a moment before noticing you following them."
    show alien neutral:
        zoom 0.5
        xalign 0.5
    b "Heyya MC! Whatcha doing out here?"

    menu billiequestion:
        "Thought I’d see what you’re up to!":
            $bil += 1
            show alien happy:
                zoom 0.5
                xalign 0.5
            b "Well, I’m not up to much."
        "Wanted some fresh air.":
            show alien happy:
                zoom 0.5
                xalign 0.5
            b "Same!"
    show alien neutral:
        zoom 0.5
        xalign 0.5
    b "Thought I’d walk around and enjoy nature. We’ve been cooped up in that building waaayyy too long."

    mc "Agreed."

    "The two of you walk around campus for a bit, then Billee would stop for a second."
    
    "Their eyes would light up, and then a squeal."
    
    b "oh"

    b "My."
    show alien happy:
        zoom 0.5
        xalign 0.5
    b "GOSH!! IS THAT A CAT!!"

    "You’d see a set of paws coming from a creature squatting under a bush."

    b "We’ve got to go catch it!"
    hide alien happy
    with moveoutleft

    menu catchthecat:
        "Lets go!":
            $bil += 1
        "Hang on.. I don’t think we should try and catch a stray":
            $bil += 0

    b "{i}They’re already running towards the cat.{/i}"

    "You sigh, before deciding to follow them."
    call chase_cat
    
    return

label c3_2_1:
    #Scene 3_2_1
    $ inhoodie = false

    scene bg davis entrance:
        zoom 0.75
        yalign 0.5
    
    show alien neutral:
        zoom 0.5
        xalign 0.5
    
    "{i}You caught the stray kitty!{/i}"

    "{i}They hold the scared little cat, gently cooing at the kitty and petting it’s soft little head.{/i}"

    b "There there little guy.. Don’t be scared."

    "It’s unclear how soothing Billee’s methods are to the kitten but he stays put in Billee’s arms."

    mc "Not to be the bearer of bad news, but what are we gonna do with him?"

    show alien upset:
        zoom 0.5
        xalign 0.5

    b "..."

    b "I don’t know."
    show bg davis entrance gloom:
        zoom 0.75
        yalign 0.5
    with dissolve
    
    "The sky decided not to give you the time to really think about that. A drop of water would fall, then another."
    show alien neutral:
        zoom 0.5
        xalign 0.5
    b "shoot."

    b "We should start by finding cover."

    show bg davis entrance rain:
        zoom 0.75
        yalign 0.5
    with dissolve
    "Before you even have the chance, those few drops would turn to a downpour."

    "{i}They quickly cover the kitty with their body, shielding it from the rain.{/i}"

    b "C’mon!"

    "{i}They get up and would take off running for cover under the nearest building.{/i}"
    scene bg alley gloom:
        zoom 0.75
        yalign 0.5
    show alien neutral:
        zoom 0.5
        xalign 0.5 
    "Soon you two were huddled under a random over hang, with a scared kitty clutched to Billee’s chest."
    
    "Kitty" "Mrow…"

    b "Shhh, I’m sorry for scaring you again."

    "{i}You look at the rain, thinking about how it would be an issue for the kitty.{/i}"

    menu whattodowithkitty:
        "Wrap the kitty in your hoodie to keep it safe and warm":
            $bil += 1
            $inhoodie = true
            "The kitty would purr softly, being wrapped in the warm embrace of the hoodie."

            "Still, you and Billee were sitting under a random building overhang, with a cat wrapped in your hoodie."
        "Try to convince Billee to let the cat go":
            $bil -= 1
            show alien upset:
                zoom 0.5
                xalign 0.5
            b "No way! This poor little guy shouldn’t be out in the rain."

            "It’s clear Billee isn’t going to let the cat go."

            "But the problem is that you two are under a random building overhand, with a cat."

            mc "{i}sigh{/i} Alright."
    
    mc "what's the plan now?"
    show alien neutral:
        zoom 0.5
        xalign 0.5
    "{i} They blink, thinking before a smirk come across their face. {/i}"
    show alien happy:
        zoom 0.5
        xalign 0.5
    b "I’ll call my mom!"
    show alien neutral:
        zoom 0.5
        xalign 0.5
    "{i}They take out their phone, dialing their mother’s number.{/i}"
    
    b "I don’t live far from campus, and we already have 2 cats... What’s one more?"

    "Billee’s mom answers and they explain the situation to her over the phone."

    "A long sigh would come out of Billee’s speakers, but they’d smile. She was clearly coming to take the little kitten back to their house."
    show alien happy:
        zoom 0.5
        xalign 0.5
    b "Well, now we just wait for like, 10 minutes."

    "It seems that all’s well that ends well."
    show alien neutral:
        zoom 0.5
        xalign 0.5
    if(bil>=5):
        "A few minutes would pass. Billee glancing between you and the kitty cradled in their arms."
        
        b "{i}They grab your hand.{/i} You can sit down, no need to stand for this long."

        mc "{i}Convinced by their antics, you sit down next to Billee.{/i}"

        "Billee takes your hand, bringing it close to the kitten’s face."

        "The kitty would sniff your hand before butting it’s head against you. It’s soft fur tickling your skin."
        show alien happy:
            zoom 0.5
            xalign 0.5
        b "It seems like he likes you."
        show alien neutral:
            zoom 0.5
            xalign 0.5
        "You gently move your hand to pet the kitten’s head, enjoying the affection of a kitty."

        "You notice that Billee was staring more at you than at the kitten their arms."
        show alien flustered:
            zoom 0.5
            xalign 0.5
        "{i}They stare at you, a dopey smile and flushing cheeks crossing their cheeks.{/i}"

        b " You know [mcname].. I thought this hackathon would suck."

        "{i}They chuckle softly, but would scoot a little closer to you.{/i}"

        b "I only signed up because all my professors were pushing it so much. But I’m glad I came."

        "{i}they smile at [mcname]{/i}"

        b "I’m glad I met you, [mcname]. You’ve made all this such a wonderful experience."
    show alien neutral:
        zoom 0.5
        xalign 0.5
    "Ten minutes would pass in the blink of an eye. A car would pull up across from where you two were sitting on the road."
    
    "Billee stands up, walking over and sheltering the kitten from the rain."
    hide alien neutral
    with moveoutleft
    "They hand the kitty to their mom andthank her for coming, then they come back to where you were."
    show alien neutral:
        zoom 0.5
        xalign 0.5
    if(inhoodie):
        "Billee handsyour hoodie back to you, slightly covered in cat hair and damp"
    
    b "Alright, we better get back to the hackathon! Lunch is definitely over."

    mc "Definitely."
    show alien happy:
        zoom 0.5
        xalign 0.5
    b "Welp. Hope your ready to make a run for it!"
    hide alien happy
    with moveoutright
    "They take off into the rain, running towards the building the hackathon is in."
    
    mc "Hey! Wait up!"

    "Then you take off after them."

    return

label c3_2_2:
    #Scene 3_2_2
    scene bg davis entrance:
        zoom 0.75
        yalign 0.5
    
    show alien upset:
        zoom 0.5
        xalign 0.5
    b "{i}They’d flop over into the grass.{/i} Oh man! We lost him…"

    mc "Well, you win some you lose some."
    show alien neutral:
        zoom 0.5
        xalign 0.5
    b "I guess..."
    show alien upset:
        zoom 0.5
        xalign 0.5
    b "SIGH!"

    "Billee lays in the grass for a minute or two, before popping up and jumping to their feet."
    show alien neutral:
        zoom 0.5
        xalign 0.5
    b "No point in dwelling on it! We still have time before the warden demands us back in our cells!"

    mc "Warden???"
    show alien angry:
        zoom 0.5
        xalign 0.5
    b "Uh- DUHHH Sterling! He’s been soooo uptight this whole time."

    b "Ok, so you’re a weak link. {i}They say, mocking Sterling's voice{/i}"
    show alien neutral:
        zoom 0.5
        xalign 0.5
    mc "Why don’t we talk to him when we get back then?"
    show alien happy:
        zoom 0.5
        xalign 0.5
    b "{i}They smile.{/i} That sounds like a good plan"
    show bg davis entrance gloom
    with dissolve
    show alien neutral:
        zoom 0.5
        xalign 0.5
    "Before either of you really had the chance to say more, a drop then another would fall from the sky."

    b "I saw that it was overcast, but I didn’t think it would start raining."
    show bg davis entrance rain
    with dissolve
    "In an almost cartoonish fashion, the rain would suddenly begin to downpour."
    show alien upset:
        zoom 0.5
        xalign 0.5
    b "Yikes! Come on!"
    hide alien upset
    with moveoutleft
    "You’d follow them, also ducking under what seemed to be the only dry spot left outside."
    scene bg alley gloom
    with dissolve
    show alien happy:
        zoom 0.5
        xalign 0.5
    
    "Billee was panting besides you, before starting to laugh."
    
    b "Well, I guess our plans of eating outside got.. Washed down the drain??"

    "They had an almost too pleased smile on their face. Too happy about their own bad pun."

    menu reacttojoke:
        "That was terrible":
            $bil += 1
        "I think we just got flushed out.":
            $bil += 2
    show alien neutral:
        zoom 0.5
        xalign 0.5
    b "Well.. what to do now?"

    "A few minutes seemed to stretch an eternity as the two of you stood there, contemplating your next move."
    
    if(bil >= 5):
        show alien flustered:
            zoom 0.5
            xalign 0.5
        "{i}They stare at you, a dopey smile and flushing cheeks crossing their cheeks.{/i}"
        
        b "You know MC.. I thought this hackathon would suck."

        "{i}They chuckle softly, but still walk closer to you{/i}"

        b "I only signed up because all my professors were pushing it so much. But I’m glad I came."

        "{i}They smile at MC{/i}"
        
        b "I’m glad I met you, MC. You’ve made all this such a wonderful experience."

        "Their sudden confession would make your face split into a smile."
        
        mc "I’m glad I met you too Billee. Hopefully we’ll all make friends that will last us a while."

        "{i}Their face turns red{/i}"

        b "Yeah. Just friends..."
    show alien neutral:
        zoom 0.5
        xalign 0.5
    b "Well.. do you want to brave the storm and make it back inside?"

    mc"Yeah. Let’s get back to the Hackathon."
    hide alien neutral
    with moveoutright
    "{i}the two of you head back to the hall{/i}"
    
    return

label c3_3:
    #Scene 3_3
    "With the two, more chatty members of the group gone. Your table is quiet as you and Sterling sit there."

    "Sterling seems to get more and more frustrated with the code as he stares blankly at the document."
    
    s "Ugh! This is so stupid."

    "He slams his head down. Obvious to everyone but him, he needs a break."

    mc "Hey, why don’t we go get some food? Walk around a bit?"

    s "We don’t have time for that! If you don’t want to keep grinding away you should’ve left with the other two."

    #menu sassyreply:
        #"You’re being stupid.":
            #sterl += 0
        #"And what are you accomplishing right now?":
            #sterl += 0
    
    "{i}He fumes, glaring at you across the table.{/i}"
    
    s "What did you just say?!"

    mc "You heard me..."

    s "{i}he huffs{/i} I’m accomplishing a lot right now!!"

    "He’s very clearly not getting anything done. He’s just too proud to admit that."

    mc "C’mon you big baby. We’re gonna put the code away for 5 minutes and go get something to eat."

    s "What? What do you mean we?"

    "You walk around him, snatching his computer. You’d make sure his document was saved, before closing everything, including the computer."

    mc "There. C’mon."

    "You drag Sterling away from his computer long enough to go stand in the line for the free food being offered to you guys by the event organizers."

    s "This is a waste of our time. We have stuff to do."



    return
    

