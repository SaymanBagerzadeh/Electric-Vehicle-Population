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
        counts=df['Make'].value_counts()
        self.list_of_brand_at_least_one_hundred=df[df['Make'].isin(counts[counts>=100].index)][['Make','Electric Range']]
        print(f"Brand {self.list_of_brand_at_least_one_hundred['Make'].max()} has the highest average Electric Range.")

    def Model_year(self):
        self.The_year_highest_car=df['Model Year'].value_counts().idxmax()
        self.The_series_of_modelyear_Electricrange=df.groupby('Model Year')['Electric Range'].mean()
        print(f"The year {self.The_year_highest_car} has the highest of car.")

    def ten_cars_has_highest_electric_range(self):
        self.ten_cars=df['Electric Range'].dropna().sort_values().tail(10).index
        print("The index of ten cars has highest electric range:")
        print(','.join(map(str,self.ten_cars)))
        self.information_of_ten_car=df.loc[self.ten_cars,['Make','Model','Model Year','Electric Vehicle Type']]
        print("The dataframe of something information of ten cars:")
        print(self.information_of_ten_car)

my_ds=DS()

my_ds.maximum_member_of_car()
my_ds.max_model()
my_ds.Electric_range()
my_ds.Model_year()
my_ds.ten_cars_has_highest_electric_range()