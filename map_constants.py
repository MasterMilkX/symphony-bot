characters = {
    "player": ("@", False),
    'tree': ('♣', False),
    "trainer": ("$", False),
    "grass": (".", True),
    "path": ("_", True),
    "item": ("o", False),
    "wild_grass": ("w", True),
    "town": ("#", True)
}

probabilities = {
    "trees": 0.4,
    "grass": {
        "spawn": 0.3,
        "grow": 0.8
    }
}

limits = {
    "items": (0, 3),
    "trainers": (0, 5)
}