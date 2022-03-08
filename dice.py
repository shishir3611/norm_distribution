import random
import statistics as st
import plotly.figure_factory as ff

sums = []

for x in range(0,1000):
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    sums.append(die1+die2)

mean = st.mean(sums)
median = st.median(sums)
mode = st.mode(sums)
stdev = st.stdev(sums)
#print(mean,median,mode,stdev)

fig = ff.create_distplot([sums],['Dice Rolls'],show_hist = False)
#fig.show()

#mean = 7, stdev = 2
#1st stdev = 5, 9
#2nd stdev = 3, 11
#3rd stdev = 1, 13

first_stdev_start, first_stdev_end = mean-stdev , mean+stdev
second_stdev_start, second_stdev_end = mean-(stdev*2) , mean+(stdev*2)
third_stdev_start, third_stdev_end = mean-(stdev*3) , mean+(stdev*3)

list_first_stdev = [result for result in sums if result > first_stdev_start and result < first_stdev_end]
list_second_stdev = [result for result in sums if result > second_stdev_start and result < second_stdev_end]
list_third_stdev = [result for result in sums if result > third_stdev_start and result < third_stdev_end]

percent_in_first_stdev = (len(list_first_stdev)*100)/len(sums)
percent_in_second_stdev = (len(list_second_stdev)*100)/len(sums)
percent_in_third_stdev = (len(list_third_stdev)*100)/len(sums)
print(percent_in_first_stdev,percent_in_second_stdev,percent_in_third_stdev)

