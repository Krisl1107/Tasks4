2=input("Рост собаки менее 50 см ? ")
    if answer_2 =="да":
        answer_3 = input("У собаки короткий хвост? ")
        if answer_3 =="да":
          print("английский бульдог")
        else: answer_4=input("У собаки длинные уши? ")
        if answer_4=="да":
            print("гончая")
        else:
            answer_5=input("У собаки коротное тело? ")
            if answer_5 == "да":
                print("мопс")
            else:
                print("чихуахуа")
    else:
        answer_3_1 = input("Собака весит больше 50 кг? ")
        if answer_3_1 =="да":
            print("датский дог")
        else:
            print("фоксхаунд")

else:
    answer_2 = input("Рост собаки менее 50 см ? ")
    if answer_2 == "да":
        answer_3 = input("У собаки доброжелательный характер? ")
        if answer_3 == "да":
            print("кокер спаниэль")
        else:
            print("ирландский сеттер")
    else:
        answer_3_1 = input("У собаки рост менее 70 см? ")
        if answer_3_1 == "да":
            answer_4 = input("У собаки длинные уши? ")
            if answer_4 == "да":
                print("большой вандейский грифон")
            else:
                print("колли")
        else:
            answer_4_1 = input("Окрас рыжий с белыми отметинами? ")
            if answer_4_1 == "да":
                print("сенбернар")
            else:
                answer_5 = input("Белоснежный окрас? ")
                if answer_5 == "да":
                    print("ирландский волкодав")
                else:
                    print("ньюфаундлент")
