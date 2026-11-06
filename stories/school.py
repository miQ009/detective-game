# stories/school.py
TITLE = "The Stolen Math Exam"
INTRO = ("The Math Final exam paper vanished from a filing cabinet in the staffroom this "
         "morning before classes. Three people were nearby. Examine the room, question "
         "them, then solve the case.")
CASE_SUMMARY = ("The Math Final exam paper was stolen from a filing cabinet in the school "
                "staffroom this morning before classes. A detective is questioning you.")
ROOM_IMAGE = "images/school/school.jpg"

SUSPECTS = {
    "sana": {
        "name": "Sana Malik", "role": "Student council president",
        "image": "images/school/sana.jpg",
        "personality": "Confident, articulate and quick with an answer. Gets sharp when "
                       "she feels cornered.",
        "public": [
            "You are the student council president and have been on the honour roll for "
            "three years.",
            "You say you did office duty from 7:00 to 7:25 AM, handing notices to the "
            "front office, then went straight to class. You say you never went into "
            "the staffroom.",
            "You think Mr. Hasan is strict but fair. You think Mr. Pike is grumpy but "
            "harmless.",
        ],
        "secrets": [
            ("duty_board", "You admit office duty puts you in the corridor near the "
                           "staffroom every morning, but you only drop notices at the "
                           "front desk."),
            ("bin", "You admit the crumpled scholarship letter is yours and say you threw "
                    "it away days ago because you were stressed. You say lots of students "
                    "are stressed about finals."),
            ("printer", "You admit you know how to use the staff printer for council "
                        "notices, but you insist you printed nothing this morning."),
            ("cabinet", "You say you know nothing about a spare cabinet key."),
            ("lost_found", "You admit you looked in the lost-and-found box this morning for "
                           "a gym bag you lost last week, which contradicts your claim "
                           "that you never went into the staffroom. You say you found "
                           "nothing."),
        ],
        "questions": [
            "Where were you this morning before class?",
            "Did you go into the staffroom?",
            "Do you know how the spare key works?",
            "Are you worried about your scholarship?",
            "Did you use the staff printer?",
        ],
    },
    "hasan": {
        "name": "Mr. Hasan", "role": "Math teacher",
        "image": "images/school/hasan.jpg",
        "personality": "Stern, tidy and exact. Dislikes excuses but is fair, and worries "
                       "about his students.",
        "public": [
            "You teach mathematics and wrote the Math Final yourself.",
            "You arrived at 7:40 AM and found the filing cabinet unlocked and the exam "
            "paper gone.",
            "Your own key never leaves your keyring, and you locked the cabinet yesterday "
            "at 4 PM.",
            "You think Sana is brilliant but under heavy pressure. You suspect Mr. Pike "
            "because he has keys to many doors.",
        ],
        "secrets": [
            ("cabinet", "Besides your key there is one spare, kept on a hook by the Duty "
                        "Board in the staffroom. Only teachers and office-duty students "
                        "know where it hangs."),
            ("duty_board", "This week's office-duty student has been Sana Malik. She "
                           "passes the key hook every morning."),
            ("bin", "Two weeks ago, in private, you told Sana that her scholarship depended "
                    "on scoring 90% or above on the final."),
        ],
        "questions": [
            "When did you find the exam missing?",
            "Who could open that cabinet?",
            "Who knows where the spare key is?",
            "Which students are under pressure this term?",
        ],
    },
    "pike": {
        "name": "Mr. Pike", "role": "School janitor",
        "image": "images/school/pike.jpg",
        "personality": "Gruff, short-spoken and defensive. Afraid of being blamed for "
                       "things he did not do.",
        "public": [
            "You are the school janitor and have worked here for twenty years.",
            "You say you swept the corridors from 7:00 to 7:30 AM and never went into "
            "the staffroom.",
            "You only carry janitor keys. You have no key to the filing cabinet.",
            "You think students these days are stressed out. You respect Mr. Hasan.",
        ],
        "secrets": [
            ("printer", "You lied about never going in: at about 7:15 you went in to empty "
                        "the bin, and you heard the staff printer humming. You thought a "
                        "teacher had come in early. Nobody is usually in before 7:40."),
            ("cabinet", "When emptying the bin around 7:15 you noticed the cabinet door "
                        "ajar but said nothing, afraid you'd be blamed."),
            ("lost_found", "Around 7:20 you saw a girl with a student-council badge leaving "
                           "the staffroom carrying a gym bag. Later you noticed the "
                           "lost-and-found lid left open, and when you tidied it a blue "
                           "folder stuck out from under a bag. You thought nothing of it."),
        ],
        "questions": [
            "Where were you this morning?",
            "Did you see anyone near the staffroom?",
            "Did you hear anything from the staffroom?",
            "Do you have a key to the filing cabinet?",
        ],
    },
}

CLUES = {
    "cabinet": ("Filing Cabinet", "The cabinet is unlocked and its lock is not forced. "
                "Whoever opened it used a key. The Math Final folder is gone."),
    "printer": ("Staff Printer", "The printer's log shows a 12-page print job at 7:12 AM, "
                "the same length as the Math Final. No staff member usually arrives "
                "before 7:40."),
    "duty_board": ("Duty Board", "Today's roster: Sana Malik, student council, office duty "
                   "7:00 to 7:25 AM. Mr. Pike, corridor sweep 7:00 to 7:30 AM. Below it "
                   "hangs an empty hook labelled 'Spare cabinet key'."),
    "bin": ("Waste Bin", "A crumpled letter addressed to Sana Malik: 'Your scholarship will "
            "be reviewed unless you score 90% or above on the Math Final.'"),
    "lost_found": ("Lost-and-Found Box", "The box was rummaged recently. The top layer has "
                   "been neatly re-piled over something flat and rectangular."),
}

TRUTH = (
    "Culprit: Sana Malik, the student council president. "
    "Motive: her scholarship depended on scoring 90% or above on the Math Final, so she "
    "stole the exam paper to see the questions. "
    "Location: the original exam paper is hidden in the lost-and-found box in the "
    "staffroom, under a gym bag."
)

MAX_TRIES = 3

ENDING = (
    "**Sana Malik** was terrified of losing her scholarship. During her office duty she "
    "took the spare key from the hook, opened the cabinet, printed a copy at 7:12 AM and "
    "hid the original exam paper in the lost-and-found box under her gym bag. Mr. Pike saw "
    "a council-badge student leave with a gym bag, and the scholarship letter in the bin "
    "gave her motive away. The exam paper is recovered from the box."
)