# WARTOŚCI PODANE W centrymetrach
KNOWN_WIDTHS = {
    'cell phone': 7.0,
    'person': 46.0,
    'tv': 110.0,
}

# Odległość od kamery (cm - taka jak zmierzono na zdjęciu referencyjnym)
KNOWN_DISTANCES = {
    'cell phone': 60.0,
    'person': 60.0,
    'tv': 60.0,
}

# Ścieżki do obrazów referencyjnych
REFERENCE_IMAGES = {
    'cell phone': './assets/person_ref.png',
    'person': './assets/person_ref.png',
    'tv': './assets/person_ref.png',
}

# Słownik do przechowywania obliczonych ogniskowych dla każdego typu obiektu
focal_lengths = {}
