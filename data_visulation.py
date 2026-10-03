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