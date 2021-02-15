userfirst_str = input('Введите первое слово. Только кирилица пжлста!' + '\n') 
usersecond_str = input('Введите первое слово. Только кирилица пжлста!' + '\n') 

trigger_words = ['learn']
def compare_string (first, second):
    for word in trigger_words:
        if len(first) == len(second):
            return '1' 
        elif len(first) > len(second):
            return '2'
        elif len(first) != len(second) and second == word:
            return '3'
        else:
            return '0'
print (compare_string(userfirst_str, usersecond_str))