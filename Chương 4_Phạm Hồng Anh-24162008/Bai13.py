def chuyen_doi(s):
    words = s.split()
    new_words = []

    for w in words:
        w = w.lower()
        w = w.capitalize()
        new_words.append(w)

    return " ".join(new_words)
