"""
This module contains some utility functions.
"""

def prettyprint(c, n):
    """
    This function pretty prints a character n times.
    """
    print(c*n)
    
    
emodict = {
    "smile": " 🙂 ",
    "grin": " 😀 ",
    "boy": " 👦 ",
    "girl": " 👧 ",
    "india": " 🇮🇳 ",
    "walk": " 🚶‍♂️ ",
    "dance": " 💃 ",
    "run": " 🏃‍♂️ ",
    "food": " 🥪 ",
    "play": " 🤾 "
}

def emoji(name, n):
    
    e = emodict.get(name)
    print(e*n)
    
def emotrans(text):
    
    items = text.split()
    
    e = []
    for i in items:
        e.append(emodict.get(i, i))
        
    return e