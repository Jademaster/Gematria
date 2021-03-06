from milon import dictionaries, transliteration


MAP = (
    (1, u'א'),
    (2, u'ב'),
    (3, u'ג'),
    (4, u'ד'),
    (5, u'ה'),
    (6, u'ו'),
    (7, u'ז'),
    (8, u'ח'),
    (9, u'ט'),
    (10, u'י'),
    (20, u'כ'),
    (30, u'ל'),
    (40, u'מ'),
    (50, u'נ'),
    (60, u'ס'),
    (70, u'ע'),
    (80, u'פ'),
    (90, u'צ'),
    (100, u'ק'),
    (200, u'ר'),
    (300, u'ש'),
    (400, u'ת'),
    (20, u'ך'),
    (40, u'ם'),
    (50, u'ן'),
    (80, u'ף'),
    (90, u'ץ')
)
MAP_DICT = dict([(k, v) for v, k in MAP])
GERESH = set(("'", '׳'))


def gematria_to_int(string):
    res = 0
    for i, char in enumerate(string):
        if char in GERESH and i < len(string)-1:
            res *= 1000
        if char in MAP_DICT:
            res += MAP_DICT[char]
    return res

a=dictionaries.DictionaryHeEn(limit=0)
word=input("enter word")
value=gematria_to_int(word)
print("gematria is "+ str(value) +" and so are the words")
matches=[]
for w in a.words:
  parsed=transliteration.remove_vowels(w.get('translated'))
  if gematria_to_int(parsed)==value:
    matches.append((w.get('translated'),w.get('translation')))
print(matches)
  


