CHARACTERS = {
    "player": ("@", False),
    'tree': ('♣', False),
    "trainer": ("$", False),
    "grass": (" ", True),
    "path": ("_", True),
    "item": ("o", False),
    # "wild_grass": ("w", True),
    "wild_grass": (".", True),
    "town": ("#", True)
}

PROBABILITIES = {
    "wild_grass": {
        "spawn": 0.15,
        "grow": 0.3
    }
}

LIMITS = {
    "trees": (0.05, 0.25),
    # 'trees': (0.1, 0.4),
    "items": (0, 3),
    "trainers": (0, 5)
}

CARDINALS = [(0,1), (0,-1), (1,0), (-1,0)]