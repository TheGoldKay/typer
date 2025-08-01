from arcade.types import Color

__all__ = [
    "SCREEN_WIDTH",
    "SCREEN_HEIGHT",
    "DEFAULT_WORD_LIST",
    "BG_COLOR", 
    "FONT_SIZE", 
    "FONT_COLOR", 
    "HIGHLIGHT_COLOR"
]


DEFAULT_WORD_LIST = ("pull", "limping", "thaw", "placid", "record", "untidy", "tested",
                     "heartbreaking", "hurt", "assorted", "servant", "stale", "talk",
                     "snake", "desk", "advertisement", "balance", "cut", "animated",
                     "loaf", "reading", "massive", "rhetorical", "reminiscent", "pig",
                     "ray", "wrestle", "upbeat", "person", "addition", "record", "left",
                     "lively", "rain", "tick", "knot", "remarkable", "neat", "yam", "sea",
                     "amuse", "whirl", "thoughtful", "painstaking", "dysfunctional",
                     "female", "threatening", "marked", "linen", "rinse", "word",
                     "perfect", "hallowed", "dangerous", "birth", "pumped", "available",
                     "coherent", "macabre", "early", "loss", "dam", "true", "berry",
                     "unaccountable", "drop", "righteous", "nest", "attack", "smoggy",
                     "lettuce", "crib", "mighty", "ratty", "short", "tall", "thankful",
                     "aunt", "haunt", "wild", "pull", "brave", "property", "vague", "stove",
                     "glass", "black-and-white", "floor", "cart", "blushing", "yellow",
                     "daffy", "can", "gruesome", "screw", "wonder", "minor", "rotten",
                     "exultant", "fearless", "box", "action", "probable", "verdant",
                     "warlike", "wrathful", "support", "cooing", "piquant", "instrument",
                     "development", "fire", "late", "rainstorm", "sad", "trust", "perform",
                     "press", "spotless", "lyrical", "yell", "finger", "purring", "load",
                     "vivacious", "parsimonious", "quack", "bury", "hellish", "selective",
                     "leather", "quilt", "deserve", "obsolete", "repeat", "prose", "real",
                     "chief", "delicious", "saw", "fold", "move", "pump", "size", "tart",
                     "cover", "pets", "wheel", "mate", "rate", "coach", "honorable", "shake",
                     "picture", "sprout", "mother", "toes", "interfere", "skinny", "alarm",
                     "authority", "questionable", "cub", "enthusiastic", "wistful", "organic",
                     "step", "behavior", "zonked", "dry", "alcoholic", "average", "stomach",
                     "trade", "street", "panicky", "creepy", "relieved", "use", "animal",
                     "distance", "soggy", "part", "worthless", "ball", "precious", "quiet",
                     "arithmetic", "excited", "festive", "unequaled", "sincere", "hissing",
                     "bruise", "pin", "key", "modern", "pigs", "foregoing", "attempt", "continue",
                     "horse", "beautiful", "miscreant", "boorish", "book", "dress", "grey",
                     "children", "bustling", "super", "secret", "message", "lock", "giants",
                     "squash", "funny", "kindhearted", "classy", "mountain", "boil", "far",
                     "hand", "curly", "hysterical", "thirsty", "attraction", "neighborly",
                     "experience", "mellow", "knife", "woebegone", "rambunctious", "provide",
                     "fragile", "obedient", "power", "jagged", "scrawny", "flag", "government",
                     "unruly", "skip", "mess", "incandescent", "bucket", "bird", "desire",
                     "nod", "shiny", "spotty", "care", "basin", "coat", "cave", "robin",
                     "slippery", "mushy", "hand", "stormy", "fill", "phone", "scale", "unequal",
                     "tightfisted", "attend", "nice", "lavish", "cough", "black", "request",
                     "embarrassed", "absent", "kick", "tomatoes", "imaginary", "blue-eyed", "shirt",
                     "blood", "misty", "shelf", "sulky", "onerous", "resolute", "salty", "sweater",
                     "owe", "boring", "adjoining", "lacking", "separate", "shoes", "thread",
                     "highfalutin", "ritzy", "apparel", "matter", "existence", "educated", "shocking",
                     "rough", "food", "prefer")
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR: Color = Color(1, 50, 32, 255) # DARK_GREEN
FONT_SIZE: int = 22
FONT_COLOR: Color = Color(255, 255, 255, 255)
HIGHLIGHT_COLOR: Color = Color(255, 0, 0, 255)