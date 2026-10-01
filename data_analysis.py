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
        self.Mean_of_electric_range=df['Electric Range'].mean()
        self.The_series_of_modelyear_Electricrange=df.groupby('Model Year')['Electric Range'].mean()
        self.The_series_of_modelyear_Electricrange_bigger_than_1001=df.groupby('Model Year')['Electric Range'].mean()>self.Mean_of_electric_range
        self.The_series_of_modelyear_Electricrange_bigger_than_100=self.The_series_of_modelyear_Electricrange_bigger_than_1001[self.The_series_of_modelyear_Electricrange_bigger_than_1001==True].index
        print("The list:")
        print(','.join(map(str,self.The_series_of_modelyear_Electricrange_bigger_than_100)))
        print(f"The year {self.The_year_highest_car} has the highest of car.")

    def ten_cars_has_highest_electric_range(self):
        self.ten_cars=df['Electric Range'].dropna().sort_values().tail(10).index
        print("The index of ten cars has highest electric range:")
        print(','.join(map(str,self.ten_cars)))
        self.information_of_ten_car=df.loc[self.ten_cars,['Make','Model','Model Year','Electric Vehicle Type']]
        print("The dataframe of something information of ten cars:")
        print(self.information_of_ten_car)

    def state_of_vehicles(self):
        self.maximum_of_vehicles_at_states=df['State'].value_counts().idxmax()
        print(f"The {self.maximum_of_vehicles_at_states} has the highest of vehicles:")

    def City(self):
        self.The_five_highest_city_car=df['City'].value_counts()[:5].index
        print("These five cities has the maximum members of cars:")
        print(','.join(self.The_five_highest_city_car))

    def County(self):
        self.counts_county=df['County'].value_counts()
        self.Onehundred_at_least_cars_in_county=df[df['County'].isin(self.counts_county[self.counts_county>=100].index)].groupby('County')['Electric Range'].mean()
        print(f"The list of Vehicles of County and Mean of Electric Range\n {self.Onehundred_at_least_cars_in_county}")

    def Model_of_vehicles(self):
        self.maximum_of_make_model=df.groupby('Make')['Model'].value_counts().idxmax[0]
        print(f"The {self.maximum_of_model} has the highest Model")

    def Has_the_highest_of_Meanelectricrange(self):
        self.list_cars=df[df['Electric Range'] > df['Electric Range'].mean()]
        print(f"{self.list_cars} has the highest of cars in list.") 

    def Electric_Utility(self):
        self.Five_highest_cars=df['Electric Utility'].value_counts().sort_values().tail(5).index
        print(f"The five Electric utilities has highest cars:")
        print(','.join(self.Five_highest_cars))

    def The_brand_has_the_unique_vehicles(self):
        self.Max_unique_vehicles=df.groupby('Make')['Model'].nunique().idxmax()
        print(f"Brand {self.Max_unique_vehicles} has the widest variety of models.")

    def In_state_Make_has_highest_car(self):
        self.bishtarin=df.groupby(['State','Make']).size().groupby(level=0).idxmax()
        print("List of states make has highest car:")
        print(f"{self.bishtarin}")

    def every_Model_year_has_highest_car(self):
        self.bishtarin=df.groupby(['Model Year','Make']).size().groupby(level=0).idxmax()
        print("list for every model year has highest cars:")
        print(f"{self.bishtarin}")
    def zero_electric_range(self):
        self.list_zero_electric_range_cars=df[df['Electric Range']==0]
        self.make_has_biggest_cars=self.list_zero_electric_range_cars['Make'].value_counts().idxmax()
        print(f"{self.make_has_biggest_cars} has the highest cars in list of zero electric range")
    def divide_range_cars(self):
        self.high_list=df[df['Electric Range']>=112]
        self.mid_list=df[(df['Electric Range']<112) & (df['Electric Range']>36)]
        self.low_list=df[df['Electric Range']<=36]
    
    def save_file(self):
        print("Saving..")
        pd.DataFrame(self.high_list).to_excel('high_list.xlsx',index=False)
        pd.DataFrame(self.mid_list).to_excel('mid_list.xlsx',index=False)
        pd.DataFrame(self.low_list).to_excel('low_list.xlsx',index=False)
my_ds=DS()
my_ds.maximum_member_of_car()
my_ds.max_model()
my_ds.Electric_range()
my_ds.Model_year()
my_ds.ten_cars_has_highest_electric_range()
my_ds.state_of_vehicles()
my_ds.City()
my_ds.County()
my_ds.Electric_Utility()
my_ds.The_brand_has_the_unique_vehicles()
my_ds.In_state_Make_has_highest_car()
my_ds.every_Model_year_has_highest_car()
my_ds.zero_electric_range()
my_ds.divide_range_cars()
my_ds.save_file()