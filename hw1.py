"""
Created on Thu Aug 26 11:28:09 2021

@author: Kathy Kang
Computing ID: kck3due
"""
def log_formatter(question_num, label, to_print):
    print("Question " + str(question_num))
    print(label + ": " + str(to_print))
    print()


# 1
gradebook = {"Jon": 95, "Mike": 84, "Jaime": 99}
log_formatter(1, "gradebook", gradebook)
# Solution: gradebook: {'Jon': 95, 'Mike': 84, 'Jaime': 99}

# 2
log_formatter(2, "Mike's Grade", gradebook["Mike"])
# Solution: Mike's Grade: 84

# 3
# print(gradebook["Jeff"])
# Solution: KeyError: 'Jeff'


# 4
names_list = ["Alex", "Patrick", "Tom", "Joe", "Alex"]
log_formatter(4, "Names List", names_list)
# Solution: Names List: ['Alex', 'Patrick', 'Tom', 'Joe', 'Alex']

# 5
sorted_names = sorted(names_list)
log_formatter(5, "Sorted Names", names_list)
# Solution: Sorted Names: ['Alex', 'Patrick', 'Tom', 'Joe', 'Alex']

# 6
names_set = set(["Alex", "Patrick", "Tom", "Joe", "Alex"])
log_formatter(6, "Names Set", names_set)
# Solution: Names Set: {'Tom', 'Alex', 'Patrick', 'Joe'}

# 7a
td = [2, 4, 1, 3, 1]
log_formatter("7a", "td", td)
# Solution: td: [2, 4, 1, 3, 1]

# 7b
odd_scores = [score for score in td if score%2 == 1]
log_formatter("7b", "Odd Touchdowns", odd_scores)
# Solution: Odd Touchdowns: [1, 3, 1]

# 7c
not_one = [score for score in td if score > 1]
# print("Values in td >1: " + str(not_one))
log_formatter("7c", "Values in td >1", not_one)
# Solution: Values in td >1: [2, 4, 3]

