grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print grade

## 求和函数
def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total

##求平均数函数    
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input)) #按照公式
  return average

##求方差函数
def grades_variance(scores):
  average = grades_average(scores)
  variance = 0
  for score in scores:
    variance = variance + (average - score)**2
  variance = variance / len(scores)
  return variance
  
  print grades_variance(grades)
  
print grades_variance(grades)

## A function that returns the standard deviation of the list of grades
def grades_std_deviation(variance):
  return variance ** 0.5
variance = grades_variance(grades)
print grades_std_deviation(variance)
