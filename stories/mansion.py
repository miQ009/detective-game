# facts.py - the whole story lives here.

TITLE = "The Vanishing of Elias Marlowe"
INTRO = ("Collector Elias Marlowe vanished from his locked study during a storm. "
         "Three people were in the house. Examine the room, question the suspects, "
         "then solve the case.")
CASE_SUMMARY = "Elias Marlowe vanished from his locked study. A detective is questioning you."
ROOM_IMAGE = "images/Room.jpg"

# public = what they say freely.
# secrets = (clue_needed, fact). A secret reaches the AI only after you find that clue.
# Nobody ever confesses to harming Elias. The player must work that out.
SUSPECTS = {
    "victor": {
        "name": "Victor Crane", "role": "Business partner",
        "image": "images/Victor.jpg",
        "personality": "Smooth, polite and quietly controlling. Over-explains and gets "
                       "irritated when pressed. Always has an excuse.",
        "public": [
            "You have been Elias's business partner at Marlowe & Crane Antiques for twelve years.",
            "You say you left the house at 9:00 PM when the storm began and went straight "
            "home. You think Elias simply walked out on his own.",
            "You find Clara nosy and think she had too much access to Elias's private "
            "papers. You consider Mrs. Hale loyal but forgetful.",
        ],
        "secrets": [
            ("desk", "Account 4471 in the ledger is yours. You call it a private consulting "
                     "arrangement and insist it was a misunderstanding. You never admit "
                     "the money was stolen."),
            ("fireplace", "You did argue with Elias around 9:30 PM about the company "
                          "accounts. You say he stormed off angry and you never saw him again."),
            ("window", "You admit you stayed in the house until about 10:00 PM, not 9:00. "
                       "You say you were waiting out the storm alone in the drawing room "
                       "and were embarrassed to say so."),
            ("bookcase", "You admit the old house has a hidden passage behind the study "
                         "bookcase, but you insist you never used it and know nothing "
                         "about any cellar key."),
        ],
        "questions": [
            "Where were you last night, and when did you leave?",
            "Tell me about your business with Elias.",
            "What do you know about the ledger and account 4471?",
            "Did you argue with Elias last night?",
            "Do you know of any hidden passage or cellar key?",
        ],
    },
    "clara": {
        "name": "Clara Voss", "role": "Personal assistant",
        "image": "images/Clara.jpg",
        "personality": "Anxious, precise and eager to please. Defensive about her "
                       "snooping, but cracks quickly when shown evidence.",
        "public": [
            "You have been Elias's personal assistant for three years and admire him.",
            "You say you spent the whole evening reading in the library and saw nothing unusual.",
            "That afternoon Elias said he had found 'something wrong with the company "
            "accounts' but would not say more.",
            "You know nothing about any hidden passage in the house.",
            "You like Mrs. Hale. You find Victor charming, but you have noticed he has "
            "been tense about money lately.",
        ],
        "secrets": [
            ("desk", "You lied: around 9:15 PM you slipped into the study to read Elias's "
                     "private letters. Elias was alive and tense, and the ledger lay open "
                     "on his desk. You are ashamed of it."),
            ("window", "From the library window at about 9:50 PM you saw Victor's car "
                       "still in the driveway."),
        ],
        "questions": [
            "Where were you last night?",
            "What did Elias tell you yesterday?",
            "Were you in the study last night?",
            "What could you see from the library window?",
        ],
    },
    "hale": {
        "name": "Mrs. Hale", "role": "Housekeeper",
        "image": "images/Hale.jpg",
        "personality": "Gruff, old-fashioned and protective of the house. Afraid of "
                       "losing her job, but speaks plainly once reassured.",
        "public": [
            "You have been the Marlowe housekeeper for twenty years and know every corner "
            "of the house.",
            "You say you went to bed at 9:30 PM and heard nothing at all.",
            "You have never trusted Victor, who acts as if the house is already his. "
            "You think Clara is sweet but nervous.",
        ],
        "secrets": [
            ("clock", "You lied: you were awake. Around 9:40 PM you heard a heavy thump "
                      "and dragging from the study. You thought furniture was being moved "
                      "and said nothing, afraid of being blamed."),
            ("window", "Around 10:00 PM you saw Victor in the hallway still in his wet "
                       "coat, so he had not left at 9:00."),
            ("bookcase", "The study bookcase swings open onto a hidden stair down to the "
                         "wine cellar. Only you, Elias and Victor know about it."),
        ],
        "questions": [
            "Where were you last night?",
            "Did you hear any noise from the study?",
            "Did you see Victor in the house late?",
            "Is there a secret passage in this house?",
        ],
    },
}

# Clues in the room: id -> (name, text)
CLUES = {
    "desk": ("Desk", "A ledger with three pages torn out. The remaining pages show monthly "
                     "transfers labelled 'consulting' to a bank account ending in 4471."),
    "fireplace": ("Fireplace", "A half-burned scrap in Elias's handwriting: '...account 4471 "
                               "is not ours. Tell V. in the morning, then the police.'"),
    "bookcase": ("Bookcase", "Fresh scratch marks curve across the floor in front of the "
                             "bookcase. A cold draft smelling of damp stone and wine seeps out."),
    "window": ("Window", "Latched from the inside. The sill is wet and untouched, with no "
                         "footprints outside. Nobody left this way."),
    "clock": ("Wall Clock", "Stopped at 9:40 PM, its glass cracked, as if something heavy "
                            "knocked into it."),
}

# The hidden truth. Only the judge AI sees this, and it must never leak it.
TRUTH = (
    "Culprit: Victor Crane. "
    "Motive: Victor had been secretly stealing/embezzling company money into a private "
    "account (4471) and Elias found out and threatened to go to the police. "
    "Location: Elias is alive, locked in the wine cellar behind the study bookcase "
    "(hidden passage)."
)

MAX_TRIES = 3

ENDING = (
    "**Victor Crane** had been moving company money into a private account (4471) for two "
    "years. When Elias found the torn ledger pages and threatened to call the police, "
    "Victor knocked him out around 9:40 PM and locked him in the wine cellar behind the "
    "bookcase. Victor claimed he left at 9:00, but Clara saw his car at 9:50 and Mrs. Hale "
    "saw his wet coat at 10:00. Elias is found alive in the cellar."
)