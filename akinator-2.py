answers = ["Да Да Да Нет Нет Нет ",
           "Да Да Нет Нет Нет Нет ",
           "Да Нет Нет Нет Нет Нет ",
           "Нет Нет Нет Да Да Да  ",
           "Нет Нет Нет Да Да Нет ",
           "Нет Нет Нет Да Нет Нет ",]

answers_10 = []

color = ["крастный", "розовый", "фиолетовый", "черный", "белый", "серый" ]

for i in range(len(answers)):
    answers[i] = answers[i].replace("Да", "1")
    answers[i] = answers[i].replace("Нет", "0")
    answers[i] = answers[i].replace(" ", "")

print(answers)

for i in range(len(answers)):
    new_number = int(answers[i], 16)
    answers_10.append(new_number)
 
print(answers_10)