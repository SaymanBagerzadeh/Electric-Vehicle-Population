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
    def max_model(self):
        print(f"Model {df['Model'].value_counts().idxmax()} has the highest number of vehicles and belongs to {df['Make'][df['Model']=='MODEL Y'].unique()[0]} Make")
        self.Electric_Vehicle_Type_of_car=df['Electric Vehicle Type'].value_counts()
        self.maximum_Electric_Vehicle_Type_of_car=df['Electric Vehicle Type'].value_counts().idxmax()
        print(f"\n{self.maximum_Electric_Vehicle_Type_of_car} has the largest number of vehicles.")
    def Electric_range(self):
        self.Electric_range_of_make=df.groupby('Make')['Electric Range'].mean()
        self.Mean_of_electric_range=df['Electric Range'].mean()
        self.Highest_of_mean=self.Electric_range_of_make>self.Mean_of_electric_range
        self.list_of_highest=self.Highest_of_mean[self.Highest_of_mean==True].index
        print("The list of the highest Electric Range of mean is:")
        print(','.join(self.list_of_highest))

my_ds=DS()

my_ds.maximum_member_of_car()
my_ds.max_model()
my_ds.Electric_range()