# The time complexity of this is N^2 because for each value you compute the distance from all other points. The space complexity is number of points. I choose this solution because it was conceptually the only one I could think of.
import math
# Get inputs and make dictionary of coordinates
r = float(input())
num = int(input())
arr = []
for x in range(num):
    y = input()
    temp = y.split(" ")
    arr.append(temp)

my_dict = {}
for i in range(len(arr)):
    temp = {}
    temp["x"]=float(arr[i][0])
    temp["y"]=float(arr[i][1])
    temp["z"]=float(arr[i][2])
    my_dict[i]=temp

# hard-coded for testing
# r = 1.0
# num_points = 9
# my_dict = {0: {'x': 0.0, 'y': 0.0, 'z': 0.0}, 1: {'x': 1.0, 'y': 0.0, 'z': 0.0}, 2: {'x': 0.0, 'y': 1.0, 'z': 0.0}, 3: {'x': 0.0, 'y': 0.0, 'z': 1.0}, 4: {'x': 1.0, 'y': 1.0, 'z': 0.0}, 5: {'x': 0.0, 'y': 1.0, 'z': 1.0}, 6: {'x': 1.0, 'y': 0.0, 'z': 1.0}, 7: {'x': 1.0, 'y': 1.0, 'z': 1.0}, 8: {'x': 0.5, 'y': 0.5, 'z': 0.5}}
# print(my_dict)

# Find neighbors less than r
answers = {}
for i in my_dict:
    answers[i]=[]
for i in my_dict:
    for j in my_dict:
        if not i == j:
            distance = math.sqrt((my_dict[i]["x"]-my_dict[j]["x"])**2+(my_dict[i]["y"]-my_dict[j]["y"])**2+(my_dict[i]["z"]-my_dict[j]["z"])**2)
            if distance <= r:
                answers[i].append(j)
print(answers)