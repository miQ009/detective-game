# memory.py - what each suspect remembers (kept separately for every player).
import os
import re
import sqlite3

DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "game.db")

STOP = {"that", "this", "with", "have", "what", "when", "where", "were", "your",
        "about", "there", "they", "them", "from", "does", "would", "could", "their",
        "which", "been", "will", "know", "detective", "told", "said"}


def run(sql, params=()):
    conn = sqlite3.connect(DB)
    rows = conn.execute(sql, params).fetchall()
    conn.commit()
    conn.close()
    return rows


def init():
    run("CREATE TABLE IF NOT EXISTS memories (id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "player TEXT, who TEXT, kind TEXT, importance INTEGER, text TEXT)")


def words(text):
    found = re.findall(r"[a-z0-9]+", text.lower())
    return {w for w in found if len(w) >= 4 and w not in STOP}


def add(player, who, kind, importance, text):
    if not run("SELECT 1 FROM memories WHERE player = ? AND who = ? AND text = ?",
               (player, who, text)):
        run("INSERT INTO memories (player, who, kind, importance, text) VALUES (?, ?, ?, ?, ?)",
            (player, who, kind, importance, text))


def remember(player, who, question, relay=None):
    """Save what the suspect only HEARD. relay = (other_name, their_line)."""
    if relay:
        other, line = relay
        add(player, who, "heard", 0, f'The detective told me that {other} said: "{line[:150]}"')


def recall(player, who, question, limit=4):
    """At most `limit` relevant memories as (kind, text). Zero-score ones are skipped."""
    q = words(question)
    rows = run("SELECT id, kind, importance, text FROM memories WHERE player = ? AND who = ?",
               (player, who))
    scored = [(len(q & words(text)) * 3 + imp, mid, kind, text)
              for mid, kind, imp, text in rows]
    scored.sort(reverse=True)
    return [(kind, text) for score, _mid, kind, text in scored[:limit] if score > 0]