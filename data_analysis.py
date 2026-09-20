import numpy as np
import pandas as pd

df=pd.read_csv('export.csv')

class DS:
    def maximum_member_of_car(self):
        self.brand=df['Make'].value_counts().idxmax()
        print(f"{self.brand} has the largest number of vehicles.")
        self.amout=df['Make'].count()
        self.max_brand=122981
        self.percentage=((self.max_brand)/self.amout)*100
        print(f"\n{self.percentage:.2f} percent of these vehicles belong to this brand")

my_ds=DS()

my_ds.maximum_member_of_car()