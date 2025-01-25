#Rohit Praveen Nair
#BL.EN.U4AIE3028
#1
import numpy as np
V1= np.random.rand(100)
V1_sorted_asc=np.sort(V1)
print("Sorted vector In Ascending Order:", V1_sorted_asc)

#2
V1_scale=V1*3

#3
mean= np.mean(V1)
std_dev= np.std(V1)
print("Mean:",mean)
print("Standard Deviation:", std_dev)

#4
matrix= np.random.rand(4,3)
print("Matrix:", matrix)

flattened_matrix=matrix.flatten()
print("Flattened Matrix:", flattened_matrix)

#5
S1= "I am a great learner. i am going to have an awesome life"
count= S1.lower().count("am")
print("Occurence of 'am'  is:", count)

#6
S2="I work hard and shall be rewarded well."
S3= S1 + " " + S2
print("Combined string S3:", S3)

#7
import re

words = re.split(r"[ .]", S3)
words = [word for word in words if word]  
print("Array:", words)
print("Array Length:", len(words))

#8
filtered_words = [word for word in words if word.lower() not in ["i", "am", "to", "and"] and len(word) <= 6]
print("Filtered Words:", filtered_words)
print("Filtered Array Length:", len(filtered_words))

#9
from datetime import datetime

date_str = "01-JUN-2021"
date_obj = datetime.strptime(date_str, "%d-%b-%Y")
print("Day:", date_obj.day)
print("Month:", date_obj.month)
print("Year:", date_obj.year)

#10
import pandas as pd

data = {
    "City": ["BENGALURU", "CHENNAI", "MUMBAI", "MYSURU", "PATNA", "JAMMU", "GANDHI NAGAR", "HYDERABAD", "ERNAKULAM", "AMARAVATI"],
    "State": ["KA", "TN", "MH", "KA", "BH", "JK", "GJ", "TS", "KL", "AP"],
    "PIN Code": [560001, 600001, 400001, 570001, 800001, 180001, 382001, 500001, 682001, 522001],
}

df = pd.DataFrame(data)
df["City, State"] = df["City"] + ", " + df["State"]
df.to_excel("cities.xlsx", index=False)
print("Excel File Created!")

#11
import matplotlib.pyplot as plt

plt.plot(V1_sorted, color="red")
plt.title("Sorted V1")
plt.show()

#12
V2 = V1 ** 2

plt.plot(V1_sorted, label="V1", color="blue")
plt.plot(np.sort(V2), label="V2", color="green")
plt.legend()
plt.title("V1 and V2")
plt.show()

