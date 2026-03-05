# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define o1 = Character("Josh")
define o2 = Character("Kyle")
define o3 = Character("Sebastian")
define kareoke = Character("Tristan")
define overflow = Character("Announcement")
define evil = Character("Evil Kyle")
define cbr = Character("Campfire Canberra")
define music = Character("Someones JBL Speaker")
define backgroundchatter = Character("Incoherent Yelling")

image proom:
    "images/room.png"
    zoom 1

image canberra:
    "images/canberra.png"
    zoom 0.5

image eroom:
    "images/room2.png"
    zoom 1

image fire:
    "images/evil1.png"
    zoom 0.5

image fire2:
    "images/evil2.png"
    zoom 0.5

image fire3:
    "images/evil3.png"
    zoom 0.5

image gridaklout:
    "images/grd.png"
    zoom 2

image evilkyle:
    "images/evilkyle.png"
    zoom 0.5

image kyle:
    "images/kyle.png"
    zoom 0.3

image josh:
    "images/josh.png"
    zoom 0.3

image snack:
    "images/snak.png"
    zoom 1

image orgroom:
    "images/org.jpeg"
    zoom 4


label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene proom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show josh
    # These display lines of dialogue.

    o1 "hi uh welcome to campfire"

    o1 "hi im josh and i like vibe coding"

    show kyle

    o2 "hi im kyle and im here too"

    hide kyle
    show josh

    o1 "follow the coc i guess, have fun"

    o1 "and DO NOT go in the organisers room"

    menu:
        "What should you do?"
        "Get a snack":
            jump snack
        "Work on game": 
            jump game
        "Look inside the organiser room":
            jump evil


label snack:
    scene snack
    "you head over to the snack station"
    "i dont feel like a snack at the moment."
    menu:
        "What should you do?"
        "Work on game": 
            jump game
        "Look inside the organiser room. its next to the snacks after all.":
            jump evil


label game:
    scene eroom
    backgroundchatter "SIX SEVEN!"
    backgroundchatter "I wonder who will get locked in the box at campfire"
    evil "*lighter sounds*"
    o1 "what was that?"
    o2 "eh probably nothing"
    show kyle
    o2 "hows your game going"
    menu:
        "i need some ideas, im stuck":
            jump cont
        "havent started":
            jump angry
    
label cont:
    scene eroom
    show kyle
    o2 "thats alright!"
    o2 "what about a game about a campfire event where everything goes wrong?"
    "like i havent heard that one before..."
    o2 "oh or a game about fighting "
    jump cont2


label angry:
    scene eroom
    show kyle at right
    o2 "its ok! youve still got 10 hours!"
    show evilkyle at left
    o2 "crap."
    evil "you thought you could get rid of me... pfft."
    o2 "i know your only weakness!"
    evil "crap."
    o2 "SIX SEVEN!!!"
    evil "SIX SEVEN SIX SEVEN SIX SEVEN"
    show fire3 at left zorder 10
    o2 "haha burn"
    evil "nooooooooooo"
    hide evilkyle
    hide kyle
    show kyle at right
    o2 "that was nearly a disaster.."
    hide fire3
    o2 "its ok now! continue on with your game!"

    menu:
        "What to do now?"
        "Work on game":
            jump cont2
        "Check the organiser room":
            jump noevil

label noevil:   
    scene orgroom
    "no ones down here. im going back to work on my game."

label cont2:
    scene eroom
    backgroundchatter "so what if... gambling game?"
    backgroundchatter "no thats for daydream"
    backgroundchatter "yeah but why not, like gambling beneath the surface or smth"
    backgroundchatter "hol'up you've got a point there"
    "i guess ill put on some headphones and like... make a game?"
    "but what to make..."
    overflow "Kareoke is starting in 3 minutes"

    menu:
        "Go to kareoke?"
        "sure why not":
            jump kareoke
        "no im good.":
            jump cont3

label cont3:
    scene eroom
    overflow "IIIII JUST WANNA TELL YOU HOW IM FEELING"
    overflow "DONT TELL ME YOURE TOO BLIND TO SEE"
    o1 "SEBASTIAN TURN OFF OVERFLOW"
    o3 "oops"
    kareoke "muffled kareoke noises"
    overflow "campfire canberra is in the other room! go say hello!!"
    o2 "which other room"
    jump cont4


label kareoke:
    scene eroom
    overflow "Kareoke has been cancelled, however you can go meet campfire canberra in the Projector room!"
    o2 "both rooms have projectors."
    jump cont4

label cont4:
    menu:
        "Do you want to go see campfire canberra?"
        "yes":
            jump call
        "no":
            jump cont5


label call:
    scene proom
    show canberra at center
    cbr "Hello."
    "hi canberra"
    cbr "hi auckland"
    "why do you have so many blahajs"
    cbr "we spent hack club money on these"
    "fair enough"
    cbr "ok bye"
    "byee"
    jump cont5

label cont5:
    scene proom
    show josh at left
    show kyle at right
    o1 "and the winner is"
    o2 "no one!"
    o1 "all the games were too good or smth"
return



label evil:
    scene orgroom
    show evilkyle

    evil "what."
    evil "you arent allowed in here."
    evil "thats it."
    evil "im turning campfire into a real campfire"

    scene eroom
    show evilkyle
    evil "you made me do this."
    o2 "EVIL KYLE NO—"
    evil "too late kyle."
    show fire at left
    o1 "well uhh"
    show fire2 at right 
    evil "fire!"
    show fire3 at center 
    scene gridaklout
    show fire at left
    show fire2 at truecenter 
    show fire3 at topleft 
    backgroundchatter "Oh no the venues on fire"
    "Bad Ending: Evil Kyle burnt down grid auckland"
    return
