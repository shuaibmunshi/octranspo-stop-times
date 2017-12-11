example_time='15:10'
example_adjustment_time='6'

string_hour,string_minutes=example_time.split(":") #Splits the time stamp into two variables

int_hour=int(string_hour)
int_minutes=int(string_minutes)
int_example_adjustment_time=int(example_adjustment_time)
print("schedule hours:", int_hour)
print("schedule minutes:", int_minutes)
print("adjustment age:", example_adjustment_time)

sum_minutes_adjusted_minutes = int_minutes + int_example_adjustment_time

print("sum of minutes and adjustment age:", sum_minutes_adjusted_minutes)

if sum_minutes_adjusted_minutes > 60:
    sum_minutes_adjusted_minutes = sum_minutes_adjusted_minutes - 60
