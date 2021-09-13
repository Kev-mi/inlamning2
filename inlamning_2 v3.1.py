import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class DataHandler:
    def __init__(self, plotting_goal: str) -> None:
        ''' Inititialiser that stores the url to use
        Args:
            plotting_goal(str) just a name to make it work
        Returns:
            None
        '''

        self.plotting_goal = plotting_goal
        self.url = 'https://github.com/NordAxon/ec-python-course/blob/master/assignments/01_inlamningsuppgift_2_data.csv?raw=true'

    def plot_vaccinations(self, country_1: pd.DataFrame, country_2: pd.DataFrame) -> None:
        '''Function that plots using the df arguments
        Args:
            country_1(pd.DataFrame): selected country
            country_2(pd.DataFrame): other selected country
        returns:
            None
        '''

        #country_1.plot.hist(color='g', label='daily_vaccinations_per_million')
        plt.hist(country_1, label='Norway')
        plt.hist(country_2, label='Peru')
        plt.legend(loc='upper right')
        plt.xlabel('daily_vaccinations_per_million')
        plt.ylabel('frequency')
        plt.show()
        return None

    def _extract_country_data(self, selected_country_1: str, selected_country_2: str,
                              selected_stat: str) -> pd.DataFrame:
        '''
        Args:
            selected_country_1(str): string that selected what country the user wants stat from
            selected_country_2(str): string that selected what country the user wants stat from
            selected_stat(str): string that selects what stat the user selected to view
        return:
            country_1_Df(pd.DataFrame):
            country_2_Df(pd.DataFrame):
        '''

        df = pd.read_csv(self.url, index_col="country")
        country_1 = df.loc[selected_country_1]
        country_2 = df.loc[selected_country_2]
        country_1_Df = (country_1[[selected_stat]])
        country_2_Df = (country_2[[selected_stat]])
        return country_1_Df, country_2_Df


def main():
    for_test = DataHandler('vaccine_per_million')
    country_1_Df, country_2_Df = for_test._extract_country_data('Norway', "Peru", 'daily_vaccinations_per_million')
    for_test.plot_vaccinations(country_1_Df, country_2_Df)


if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description='select from 2 countries and then select from this list of options: daily_vaccinations_per_million , source_website , daily_vaccinations')
    # parser.add_argument('--country1', help="enter first country", required=True, type=str)
    # parser.add_argument('--country2', help="enter second country", required=True, type=str)
    # parser.add_argument('--data-flag', help="enter what you want the program to do", required=True, type=str)
    # args = parser.parse_args()
    # args.country1, args.country2
    main()
