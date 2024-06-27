import statistics
import math

def convert(temp_in_celsius):
  temp_in_far = temp_in_celsius * 1.8 + 32
  return temp_in_far

print(convert(20))

def do_some_math():
  numbers = [1, 2, 3, 4, 5, 6, 7 , 8, 9]

  print(statistics.mean(numbers))
  print(statistics.fmean(numbers))
  print(statistics.median(numbers))

do_some_math()