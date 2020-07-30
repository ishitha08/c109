import random
#import plotly.express as px
import plotly.figure_factory as ff
import statistics

dice_result = []
for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1+dice2)
mean = sum(dice_result)/len(dice_result)
std_deviation = statistics.stdev(dice_result)
median = statistics.median(dice_result)
mode = statistics.mode(dice_result)
print(mean)
print(std_deviation)
print(median)
print(mode)


#fig = px.bar(x = dice_result,y = count)
#fig.show()
fig = ff.create_distplot([dice_result],['Result'])
fig.show()