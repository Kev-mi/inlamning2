import argparse
import datahandler


def main(data_flag, country1, country2):
    country_plotting = DataHandler('vaccine_data_plotting')
    country_1_Df, country_2_Df = country_plotting._extract_country_data(country1, country2, data_flag)
    country_plotting.plot_vaccinations(country_1_Df, country_2_Df,country1, country2, data_flag)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='select from 2 countries and then select from this list of options: daily_vaccinations_per_million, daily_vaccinations_raw , total_vaccinations , daily_vaccinations',)
    parser.add_argument('--country1', help="enter first country", required=True, type=str)
    parser.add_argument('--country2',help="enter second country", required=True, type=str)
    parser.add_argument('--data_flag',help="enter what you want the program to do", required=True, type=str)
    args = parser.parse_args()
    args.country1, args.country2
    main(args.data_flag, args.country1, args.country2)
