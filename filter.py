import time



# =========================
# CONFIG
# =========================

COOLDOWN_SECONDS = 5



# =========================
# STORAGE
# =========================

last_messages = {}



# =========================
# IGNORE WORDS
# =========================

IGNORE_WORDS = {

    "wkwk",
    "wkwkwk",
    "wkwkwkw",

    "haha",
    "hahaha",

    "hehe",

    "lol",
    "LOL",

    "😂",
    "🤣",

    ".",
    "..",
    "..."

}



# =========================
# SPAM PHRASES
# =========================

IGNORE_PHRASES = {

    "inbox me",
    "dm me",
    "message me",

    "click here",
    "click link",

    "free gift",
    "giveaway"

}



# =========================
# CHAT FILTER
# =========================

def should_send_chat(
    username,
    message
):


    if not username:

        return False



    if not message:

        return False



    clean = message.strip()



    if clean == "":

        return False



    lower_text = clean.lower()



    # =========================
    # REACTION FILTER
    # =========================

    if lower_text in {

        x.lower()

        for x in IGNORE_WORDS

    }:

        return False



    # =========================
    # PHRASE FILTER
    # =========================

    for phrase in IGNORE_PHRASES:


        if phrase in lower_text:

            return False



    # =========================
    # TOO SHORT
    # =========================

    if len(clean) <= 1:

        return False



    # =========================
    # DUPLICATE SPAM
    # =========================

    key = (

        username.lower(),

        lower_text

    )



    now = time.time()



    if key in last_messages:


        elapsed = (

            now - last_messages[key]

        )


        if elapsed < COOLDOWN_SECONDS:

            return False



    last_messages[key] = now



    return True