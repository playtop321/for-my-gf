import time

def sing_just_the_way_you_are():
    lyrics_with_timing = [
        ("Oh, her eyes, her eyes,", 3),
        ("Make the stars looke like they're not shinin", 4),
        ("Her hair, her hair", 3),
        ("Falls perfectly without her trin", 4),
        ("She's so beautiful", 2),
        ("And i tell her everyday", 2)
    ]
    for lyric, timing in lyrics_with_timing:
        print(lyric)
        time.sleep(timing)

if __name__ == "__main__":
    sing_just_the_way_you_are()
