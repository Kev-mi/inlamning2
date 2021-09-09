import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#df = pd.read_csv(url,index_col=0)
class DataHandler:
    def __init__(self,placeholder):
        self.placeholder = placeholder

    def plot_vaccinations(self):
        return None

    def __extract__country__data(self,country):
        return None




url = 'https://github.com/NordAxon/ec-python-course/blob/master/assignments/01_inlamningsuppgift_2_data.csv?raw=true'
df = pd.read_csv(url)

vaccinated_per_day_per_million_by_country = df.groupby(['country'])[['daily_vaccinations_per_million']].mean()
print(vaccinated_per_day_per_million_by_country)

df_2 = vaccinated_per_day_per_million_by_country
df_2.plot()
plt.show()
df.plot()
plt.show()

#parser.add_argument('--country1', help="enter first country", required=True, type=str)
#parser.add_argument('--country2', help="enter second country", required=True, type=str)
#parser.add_argument('--data-flag', help="enter what you want the program to do", required=True, type=str)


