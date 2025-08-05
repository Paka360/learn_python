from collections import OrderedDict

fav_languages = OrderedDict()

fav_languages['jen'] = 'python'
fav_languages['may'] = 'php'
fav_languages['max'] = 'javascript'
fav_languages['phil'] = 'c++'
fav_languages['edward'] = 'python'

for name, language in fav_languages.items():
    print(name.title() + "'s favourite language is " + language.title() + '.')
    