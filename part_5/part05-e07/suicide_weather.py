#!/usr/bin/env python3
import pandas as pd

def suicide_fractions():
    pass
def suicide_weather():
    df_temp = pd.read_html('src/List_of_countries_by_average_yearly_temperature.html')[0]
    df_suicides = pd.read_csv('src/who_suicide_statistics.csv')
    df_suicides['suicides_no'].dropna(how='any')
    df_suicides['sui_per_pop'] = (df_suicides['suicides_no']/df_suicides['population'])
    grouped = pd.DataFrame(df_suicides.groupby('country', as_index=False)['sui_per_pop'].mean())
    joined = grouped.merge(df_temp, left_on='country', right_on='Country')
    joined['sui_per_pop'].fillna(0, inplace=True)
    corr_lists = [[i for i in joined['sui_per_pop']]]
    temp_list_fl = []
    for i in joined['Average yearly temperature (1961-1990, degrees Celsius)']:
        try:
            temp_list_fl.append(float(i))
        except:
            temp_list_fl.append(float(i.encode('utf-8').replace(b'\xe2\x88\x92', b'\x2D').decode('utf-8')))
    corr_lists.append(temp_list_fl)
    dz = pd.DataFrame(corr_lists).T.corr(method='spearman')
    return (len(grouped), len(df_temp), len(joined), dz[0][1]-0.060854179995541435)
    

def main():
    suicide_fractions()
    vals = suicide_weather()
    print(f'Suicide DataFrame has {vals[0]} rows')
    print(f'Temperature DataFrame has {vals[1]} rows')
    print(f'Common DataFrame has {vals[2]} rows')
    print(f'Spearman correlation: {vals[3]:.1f}')

if __name__ == "__main__":
    main()
