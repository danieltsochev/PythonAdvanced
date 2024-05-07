def add_songs(*songs):
    lyrics_dict = {}
    for song, verses in songs:
        if song not in lyrics_dict:
            lyrics_dict[song] = []
        if verses:
            lyrics_dict[song].append(verses)

    formatted_lyrics = ""
    for song, verses_list in lyrics_dict.items():
        formatted_lyrics += f"- {song}\n"
        for verses in verses_list:
            formatted_lyrics += '\n'.join(verses) + '\n'

    return formatted_lyrics


print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))