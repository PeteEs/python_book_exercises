favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

should_take_list = ["ann","edward","mike","sarah","john"]



for person in should_take_list:
    if person in favorite_languages.keys():
        print(f"{person.title()}, thank you for taking the pool!")
    else:
        print(f"{person.title()}, please take the pool!")