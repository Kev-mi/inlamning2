import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#df = pd.read_csv(url,index_col=0)

class DataHandler:
    def __init__(self, plotting_goal : str) -> None:
        ''' Inititialiser that reads the csv file and puts it into a pandas dataframe

        Args:
            plotting_goal(str) just a name to make it work

        Returns:
            None

    '''

        self.plotting_goal = plotting_goal
        self.url = 'https://github.com/NordAxon/ec-python-course/blob/master/assignments/01_inlamningsuppgift_2_data.csv?raw=true'

    def plot_vaccinations(self,row,column):
        '''Function that plots groupby on selected row and column

        Args:
            row(str): selected row
            column(str): selected column

        returns:
            None

        '''

        df = pd.read_csv(for_test.url)
        vaccinated_per_day_per_million_by_country = df.groupby([row])[[column]].mean()
        print(vaccinated_per_day_per_million_by_country)
        df_2 = vaccinated_per_day_per_million_by_country
        df_2.plot()
        plt.show()
        #df.plot()
        #plt.show()

    def _extract_country_data(self,selected_country_1,selected_country_2):
        df = pd.read_csv(for_test.url, index_col="country")
        country_1 = df.loc[selected_country_1]
        country_2 = df.loc[selected_country_2]
        print(country_1.groupby(['country'])[['daily_vaccinations_per_million']].mean())



for_test = DataHandler('vaccine_per_million')

#for_test.plot_vaccinations('country','daily_vaccinations_per_million')
for_test._extract_country_data('Norway',"Peru")

#parser = argparse.ArgumentParser(description='Sum range')
#parser.add_argument('--country1', help="enter first country", required=True, type=str)
#parser.add_argument('--country2', help="enter second country", required=True, type=str)
#parser.add_argument('--data-flag', help="enter what you want the program to do", required=True, type=str)
#args = parser.parse_args()
#args.country1, args.country2

#extract data from 2 countries and then plot it
