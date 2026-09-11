# =========================
# CHAT FORMAT
# =========================

def format_chat(
    username,
    message
):

    return (
        f'💬 [TikTok] {username}: "{message}"'
    )



# =========================
# FOLLOW FORMAT
# =========================

def format_follow(
    username
):

    return (
        f'⭐ [TikTok] {username} followed the host'
    )



# =========================
# GIFT FORMAT
# =========================

def format_gift(
    username,
    gift_name,
    count=1
):


    gift_icons = {


        # Popular TikTok Gifts

        "Rose": "🌹",

        "Heart Me": "❤️",

        "Finger Heart": "🫰",

        "Coffee": "☕",

        "GG": "🎮",

        "TikTok": "🎵",

        "Lion": "🦁",

        "Golden Gamepad": "🎮",

        "Ice Cream": "🍦",

        "Perfume": "🌸",

        "Love You": "❤️",

        "Cap": "🧢",

        "Galaxy": "🌌",

        "Money Gun": "💸",

        "Diamond": "💎",

        "Panda": "🐼",

        "Fireworks": "🎆",

        "Crown": "👑",

        "Money Rain": "💰",

        "TikTok Universe": "🌎",


    }



    # fallback untuk gift yang belum dikenal

    icon = gift_icons.get(
        gift_name,
        "🎁"
    )



    if count > 1:

        return (
            f'🎁 [TikTok] {username} sent '
            f'{gift_name} {icon} x{count}'
        )



    return (
        f'🎁 [TikTok] {username} sent '
        f'{gift_name} {icon}'
    )