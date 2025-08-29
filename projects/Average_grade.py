# NS 1st 🔨 Average Grade

cs_grade = input("what is your grade in CS class? : ")
math_grade = input("what is your grade in Math class? : ")
biology_grade = input("what is your grade in Biology class? : ")
advisory_grade = input("what is your grade in Advisory class? : ")
drawing_grade = input("what is your grade in Drawing class? : ")
english_grade = input("what is your grade in English class? : ")
worldcivi_grade = input("what is your garde in Wolrd civilizations class? : ")

average = (cs_grade + math_grade + biology_grade + advisory_grade + drawing_grade + english_grade + worldcivi_grade) / 7

print("Your average grade is:", round(average, 2))
