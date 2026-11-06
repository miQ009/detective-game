# stories/museum.py
TITLE = "The Star of Lisbon Heist"
INTRO = ("During tonight's gala, the priceless Star of Lisbon diamond vanished from its "
         "locked display case. Three people had access to the gallery. Examine the room, "
         "question them, then solve the case.")
CASE_SUMMARY = ("The Star of Lisbon diamond was stolen from a locked display case in the "
                "museum gallery during tonight's gala. A detective is questioning you.")
ROOM_IMAGE = "images/museum/museum.jpg"

SUSPECTS = {
    "marco": {
        "name": "Marco Bell", "role": "Night security guard",
        "image": "images/museum/marco.jpg",
        "personality": "Friendly and chatty at first, but sweaty and evasive when pressed. "
                       "Always has a casual excuse.",
        "public": [
            "You are the night security guard at the museum and have worked here for six years.",
            "You say you stood at your post by the gallery door all evening and never left "
            "it, apart from the usual half-hourly rounds.",
            "You say the alarm never went off and you saw nothing unusual.",
            "You think Tessa the caterer wanders around too much. You think Dr. Walsh is a "
            "perfectionist who hides her nerves.",
        ],
        "secrets": [
            ("alarm_panel", "The log shows the alarm was disarmed at 8:10 PM with your "
                            "personal code, 2207. You say it was a routine disarm for a "
                            "delivery cart and that you re-armed it four minutes later. "
                            "You say nothing more."),
            ("camera", "You admit you were in the control room from 8:10 to 8:14 'fixing a "
                       "flickering monitor', which contradicts your claim that you never "
                       "left your post. You insist you never touched the footage."),
            ("guard_desk", "You admit the loan notice is yours and that you have money "
                           "troubles. You say plenty of honest people have debts and it "
                           "proves nothing."),
            ("extinguisher", "You say you check the extinguisher cabinet on every round "
                             "because the safety log requires it, and that you know "
                             "nothing about what is inside it."),
        ],
        "questions": [
            "Where were you all evening?",
            "Did you leave your post at any time?",
            "Who has the alarm codes?",
            "Do you have money problems?",
            "Why do you check the fire extinguisher?",
        ],
    },
    "irene": {
        "name": "Dr. Irene Walsh", "role": "Chief curator",
        "image": "images/museum/irene.jpg",
        "personality": "Polished, precise and a little proud. Speaks in complete sentences "
                       "and hates being doubted.",
        "public": [
            "You have been the museum's chief curator for fifteen years.",
            "You gave your gala speech in the main hall from 8:00 to 8:30 PM in front of "
            "eighty guests, so you were never alone in the gallery.",
            "You have a second alarm code, 4118, but you did not use it tonight.",
            "You think Marco is reliable but has seemed jumpy lately. You trust Tessa completely.",
        ],
        "secrets": [
            ("alarm_panel", "You recognise the code in the log: 2207 is Marco's personal "
                            "code, not yours."),
            ("camera", "During a pause in your speech at about 8:12 you glanced at the hall "
                       "monitor and noticed the gallery camera picture looked frozen. You "
                       "thought it was a glitch and told no one."),
            ("guard_desk", "Last month Marco asked you for a salary advance. You refused, "
                           "and he looked desperate."),
        ],
        "questions": [
            "Where were you during the gala?",
            "Whose code is in the alarm log?",
            "Did you notice anything strange tonight?",
            "Does anyone here have money problems?",
        ],
    },
    "tessa": {
        "name": "Tessa Quinn", "role": "Caterer",
        "image": "images/museum/tessa.jpg",
        "personality": "Warm, quick-talking and nervous around authority. Over-explains "
                       "when she feels watched.",
        "public": [
            "You run Quinn Catering and have worked the museum's galas for three years.",
            "You say you stayed in the kitchen and the main hall all evening and never "
            "entered the gallery, since catering staff aren't allowed there.",
            "You like Dr. Walsh. You find Marco friendly but a bit secretive about his "
            "private life.",
        ],
        "secrets": [
            ("display_case", "You lied: around 8:05 PM you stepped into the gallery to "
                             "bring Marco a coffee and saw the Star of Lisbon still safely "
                             "in its case. Admitting it breaks the rules, so you hid it."),
            ("extinguisher", "At about 8:20 PM, leaving the hall, you glimpsed Marco kneeling "
                             "by the fire extinguisher cabinet, tapping the canister. You "
                             "thought it was odd but assumed he was checking it."),
            ("camera", "A small monitor in the kitchen corridor shows the gallery. Around "
                       "8:12 PM the picture froze for a few minutes. You assumed it was lag."),
        ],
        "questions": [
            "Did you ever go into the gallery?",
            "What did you see in the gallery corridor tonight?",
            "Did you notice anything odd on the monitors?",
            "What do you think of Marco?",
        ],
    },
}

CLUES = {
    "display_case": ("Display Case", "The Star of Lisbon's case is empty. The glass is "
                     "intact and the lock was opened, not forced."),
    "alarm_panel": ("Alarm Panel", "The log shows the gallery alarm was disarmed at 8:10 PM "
                    "with code 2207 and re-armed at 8:14 PM."),
    "camera": ("Security Camera", "The footage freezes on an empty gallery from 8:10 to "
               "8:14 PM, then resumes. The control room next door opens only with a guard's "
               "keycard."),
    "extinguisher": ("Fire Extinguisher", "The cabinet's safety seal is broken. The canister "
                     "is oddly light and something rattles inside it."),
    "guard_desk": ("Guard's Desk", "Under the blotter is a bank notice: 'FINAL WARNING: loan "
                   "overdue, $40,000.' Beside it lies a betting slip."),
}

TRUTH = (
    "Culprit: Marco Bell, the night security guard. "
    "Motive: heavy debts and gambling; he needed money and was refused a salary advance. "
    "Location: the Star of Lisbon diamond is hidden inside the emptied fire extinguisher "
    "canister in the gallery's extinguisher cabinet."
)

MAX_TRIES = 3

ENDING = (
    "**Marco Bell** was drowning in gambling debts. At 8:10 PM he disarmed the alarm with his "
    "own code, froze the camera feed from the control room, and took the diamond from the "
    "case. He hid it inside an emptied fire extinguisher canister to collect later. Tessa saw "
    "the diamond at 8:05 and saw Marco at the extinguisher cabinet at 8:20, and Dr. Walsh "
    "confirmed that code 2207 was his. The Star of Lisbon is recovered from the canister."
)