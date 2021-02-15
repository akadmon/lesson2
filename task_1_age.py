print()
print ("Введите возраст и узнаете чем обычно занят человек на разных этапах жизни. Только цифры пожалуйста!")
print()
question = 1
while question == True: 
    
    try:    
        userage = float(input('Введите ваш возраст: '))

        def age_separator (age):
            if age <=0:
                return 'Увы, для начала нужно родиться!'
            elif age > 0 and age <= 5:
                return 'Сдают в детский сад или ясли'
            elif age > 5 and age <= 17:
                return 'Ходит в школу'  
            elif age > 17 and age <= 23:
                return 'Учится в ВУЗе' 
            elif age > 23 and age <= 60:
                return 'Работает'
            elif age > 60 and age <= 120:
                return 'Отдыхает на пенсии'    
            else:
                return 'Дункану Маклауду плевать на это ваше "время"'          

        print(age_separator(userage))
    
    except ValueError:
        print()
        print ('Неверный формат, только цифры пожалуйста. Вон же выше написано! Вы что читать не умеете?')
        print()