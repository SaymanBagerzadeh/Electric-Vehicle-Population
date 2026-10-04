import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df=pd.read_csv('export.csv')

class Data_visulation:
        
        def BEV_cars_for_any_model_year(self):
            self.list_of_bev=df[df['Electric Vehicle Type']=='Battery Electric Vehicle (BEV)']
            self.members_of_bev_vehicle=self.list_of_bev['Model Year'].value_counts()
            plt.bar(self.members_of_bev_vehicle.index,self.members_of_bev_vehicle.values,color='Green')
            plt.xlabel('Model Year')
            plt.ylabel('Members of cars')
            plt.title('Members of cars by Model Year')
            plt.tight_layout()

        def ten_high_members_of_cars(self):
            self.list_of_ten_biggest=df['Make'].value_counts().sort_values().tail(10)
            plt.barh(self.list_of_ten_biggest.index,self.list_of_ten_biggest.values,color='red')
            plt.xlabel('Car members of brand')
            plt.ylabel('Brand')
            plt.title('Car members of brand')
            plt.tight_layout()    

        def Electric_range(self):
            plt.hist(self.Electric_Range,edgecolor='black')
            plt.xlabel('Electric Range')
            plt.ylabel('Count')
            plt.title('Electric Range counts')
            plt.tight_layout()  

        def Electric_vehicle_types(self):
            plt.bar(self.Electric_vehicle_type.index,self.Electric_vehicle_type.values,color='yellow')
            plt.xlabel('Electric Vehicle Type')
            plt.ylabel('Counts')
            plt.title('Electric Vehicle cars')
            plt.tight_layout()
            plt.savefig('Electric Vehicle cars.png')

        def Every_year_car(self):
            sns.lineplot(self.Cars_in_any_year)
            plt.savefig('Members_car every year.png')

        def Number_of_cars_100_electric_range(self):
            list_of_biggest_100=df[df['Electric Range']>100]
            members_of_car=list_of_biggest_100['Make'].value_counts()
            plt.bar(self.members_of_car.index,self.members_of_car.values)
            plt.gcf().autofmt_xdate()
            plt.xlabel('Make')
            plt.ylabel('Members of cars')
            plt.title('Number of cars by Make')
            plt.tight_layout()

        def Mean_Electric_Range(self):
            mean_of_electric_range=df.groupby('Make')['Electric Range'].mean().sort_values().tail(10)
            plt.bar(self.mean_of_electric_range.index,self.mean_of_electric_range.values,color='green')
            plt.gcf().autofmt_xdate()
            plt.xlabel('Make')
            plt.ylabel('Mean of Electric Range')
            plt.title('Mean of Electric Range by Make')
            plt.tight_layout()
            plt.legend()
            plt.show()

        def Electricrange_by_model_year(self):
            series_of_electric_range_by_model_year=df.groupby('Model Year')['Electric Range'].mean()
            sns.lineplot(self.series_of_electric_range_by_model_year)

        def Electric_vehicle_type(self):
            Count_of_vehicle_types_car=df['Electric Vehicle Type'].value_counts()
            sns.barplot(self.Count_of_vehicle_types_car,color='red')

        def Ten_high_county(self):
            Ten_high_County=df['County'].value_counts().sort_values().tail(10)
            sns.barplot(self.Ten_high_County,color='yellow')
            plt.gcf().autofmt_xdate()