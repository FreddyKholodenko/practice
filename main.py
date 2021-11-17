import inline as inline
import matplotlib

from functions import*
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# print(max_of_three(3, 39, 5))
# print(my_sum([4, 7, 9, 41]))
# print(my_mul([4, 7, 2]))
# print(my_mean([1, 2, 3, 4]))
# print(my_stars([3, 9, 7]))
# print(second_best([1, 2, 3, 4]))
# print(my_sort(['a', 'c', 'v', 'b', 'b', 'a']))
# print(my_char_2_num(['a', 'c', 'z', 'b', 'b', 'a']))
# print(my_list_2_text([1, ' cow, ', 2, ' geese ', 3, ' chickens ', 5.5, ' Sandwiches ', 3, 2.0, ' Liters ', 'of ',
#                       'hell', '.']))
# my_list_mean([1.0, 'abc', 12, 'aaa', '1000', 'hello', 'aaaaa', 2, '1223'])

df = pd.read_csv('F:\\Computer Science\\שנה ג\\מבוא למדעי נתונים\\Bike_sharing_data.csv')
df.info()
print(df['mnth'].value_counts(normalize=True))
print(df['mnth'].value_counts())
pd.cut(df["temp"],bins=5).value_counts()
df.cnt.describe() #ממוצע וסטיית תקן
%matplotlib inline
plt.scatter(df.registered, df.cnt)
df.cnt[df.cnt > 5000].count() #probability THING
df.cnt[df.cnt > 5000].count()/df.cnt.count() # probability THING TWO