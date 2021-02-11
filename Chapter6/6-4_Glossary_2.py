glossary = {'for': 'loop an action.', 'print': 'print anything you want.',
            'input': 'get a value entered by user.', 'in': 'if anything is in something.',
            'not in': 'if anything is in something.', 'int': 'transform a value in a integer.',
            'float': 'transform a value in a float.', 'sort':'order a list in alphabetical.',
            'title': 'print the first letter of a value in uppercase.',
            'lower': 'print the first letter of a value in lowercase.'}

for key, value in glossary.items():
    print('\n',key.title()+':', value)