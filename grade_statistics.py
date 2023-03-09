def splitting_nums_exam(initial_data: str): 
    exam = []
    my_list = initial_data.split()
    exam.append(my_list[0])
    return exam

def splitting_nums_exer(initial_data: str): 
    exer = []
    my_list = initial_data.split()
    exer.append(my_list[1])
    return exer

def grading(set1: list, set2: list): #set1 is exam pts and set2 is exercise nums
    grades = 0
    for i in set1:
        if int(i) < 10:
            grades = int(set2[set1.index(i)]) // 10 + int(i) + 40
        else:
            grades = int(set2[set1.index(i)]) // 10 + int(i)
    return grades

def mean(grades: list): #tested
    total = 0
    for i in grades:
        if i <= 30:
            total += i
        elif i > 30:
            total += i - 40
    mean = total / len(grades)
    return ("{:.1f}".format(mean))

def grades(grades: list): #tested??
    grades_num = [0, 0, 0, 0, 0, 0]
    for i in grades:
        if i >= 0 and i <= 14:
            grades_num[5] += 1
        elif i >= 15 and i <= 17:
            grades_num[4] += 1
        elif i >= 18 and i <= 20:
            grades_num[3] += 1
        elif i >= 21 and i <= 23:
            grades_num[2] += 1
        elif i >= 24 and i <= 27:
            grades_num[1] += 1
        elif i >= 28 and i <= 30:
            grades_num[0] += 1
        else:
            grades_num[5] += 1
    return grades_num

def pass_percent(grades: list): #tested
    passing = 0
    for i in grades[0:5]:
        passing += i
    if grades[5] == 0:
        pass_percentage = 100.0
    else:
        pass_percentage = passing / (passing + grades[5]) * 100
    return ("{:.1f}".format(pass_percentage))

def main():
    points = []
    while True:
        initial_data = input("Exam points and exercises completed:")
        if initial_data == "":
            break
        else:
            points.append(grading(splitting_nums_exam(initial_data), splitting_nums_exer(initial_data)))
    
    grade = grades(points)
    print("Statistics:")
    print(f"Points average: {mean(points)}")
    print(f"Pass percentage: {pass_percent(grade)}")
    print("Grade distribution:")
    ast = ""
    i = 5
    for item in grade:
        for item2 in range(item):
            ast += "*"
        print(f"  {i}: {ast}")
        i -= 1        
        ast = ""


main()
            



            


