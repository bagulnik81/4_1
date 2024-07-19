calls=0
def count_calls():
 global calls
 calls += 1
 #print(RR)
 return calls

def string_info():
 count_calls()
 string = input("Введите слово для функции string_info: ")
 string2 = len(string), string.upper(), string.lower()
 # string = (len(string), string.upper(), string.lower())
 return print(string2)


def is_contains():
    count_calls()
    list_to_search = ["Москва", "лОнДон", "сОфИЯ", "Париж", "рим"]
    string = input("Введите одну из столиц европейских государств: ")
    new_list_to_search = [x.lower() for x in list_to_search]
    for i in range(len(new_list_to_search)):
        if string.lower() == new_list_to_search[i]:
            aa = True
            break
        aa = False
    return print(aa)


string_info()
is_contains()
print(calls)
