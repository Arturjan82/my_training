calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    tup = (len(string), string.upper(), string.lower())
    return tup


def is_contains(string, list_to_search):
    count_calls()
    prov = False
    for elem in list_to_search:
        if elem.lower() == string.lower():
            prov = True
            break
    return prov


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
