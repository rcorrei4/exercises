favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
    
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

languages_poll = ['jen', 'sarah', 'edward', 'phil', 'erick', 'ricardo', 'sabrina']

for name_poll in sorted(languages_poll):
    if name_poll in favorite_languages:
        print(f'\n{name_poll.title()}, thanks for responding the poll!')
    else:
        print(f'\n{name_poll.title()}, you should take the poll!')
