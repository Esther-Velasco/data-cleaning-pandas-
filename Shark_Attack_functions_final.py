#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[1]:


def run_all():
    global shark_attacks_dropped
    shark_attacks_df = pd.read_excel("GSAF5.xls")
    shark_attacks_df
    #dropping unnesseccary columns and assigning it to a new dataname
    shark_attacks_dropped = shark_attacks_df.drop(["Name", "Sex", "Age", "Type", "Source", "pdf", "href formula","Unnamed: 11", "href", "Case Number", "Activity","Case Number.1", "original order","Unnamed: 21","Unnamed: 22"], axis=1)
    #checking the column names
    shark_attacks_dropped.columns
    #lowercase the column names
    new_shark_attacks_dropped = pd.Series(shark_attacks_dropped.columns).apply(lambda col:col.lower())
    shark_attacks_dropped.columns = new_shark_attacks_dropped
    shark_attacks_dropped
    #strip whitespaces from column names
    shark_attacks_dropped.columns = shark_attacks_dropped.columns.str.strip()
    shark_attacks_dropped.columns
    # cleaning the year column
    shark_attacks_dropped['year'] = pd.to_datetime(shark_attacks_dropped['year'], format='%Y', errors='coerce')
    shark_attacks_dropped['year'] = shark_attacks_dropped['year'].dt.strftime('%Y')
    shark_attacks_dropped["year"].ffill(inplace = True)
    shark_attacks_dropped["year"] = shark_attacks_dropped["year"].map(int)
    shark_attacks_dropped =  shark_attacks_dropped.loc[shark_attacks_dropped['year'] >= 1900]
    countries = {
    'USA': 'usa',
    'AUSTRALIA': 'australia',
    'Coral Sea': 'australia',
    'EGYPT': 'egypt',
    'PHILIPPINES': 'philippines',
    'BAHAMAS': 'bahamas',
    'SPAIN': 'spain',
    'PORTUGAL': 'portugal',
    'COLOMBIA': 'colombia',
    'SOUTH AFRICA': 'south africa',
    'ECUADOR': 'ecuador',
    'FRENCH POLYNESIA': 'french polynesia',
    'NEW CALEDONIA': 'new caledonia',
    'TURKS and CaICOS': 'uk',
    'MEXICO': 'mexico',
    'BRAZIL': 'brazil',
    'SEYCHELLES': 'seychelles',
    'ARGENTINA': 'argentina',
    'FIJI': 'fiji',
    'MeXICO': 'mexico',
    'Maldives': 'maledives',
    'South Africa': 'south africa',
    'ENGLAND': 'uk',
    'JAPAN': 'japan',
    'INDONESIA': 'indonesia',
    'JAMAICA': 'jamaica',
    'BELIZE': 'belize',
    'MALDIVES': 'maledives',
    'THAILAND': 'thailand',
    'COLUMBIA': 'colombia',
    'NEW ZEALAND': 'new zealand',
    'COSTA RICA': 'costa rica',
    'New Zealand': 'new zealand',
    'British Overseas Territory': 'uk',
    'CANADA': 'canada',
    'JORDAN': 'jordan',
    'ST KITTS / NEVIS': 'uk',
    'ST MARTIN': 'netherlands',
    'PAPUA NEW GUINEA': 'papua new guinea',
    'REUNION ISLAND': 'france',
    'ISRAEL': 'israel',
    'CHINA': 'china',
    'SAMOA': 'samoa',
    'IRELAND': 'ireland',
    'ITALY': 'italy',
    'MALAYSIA': 'malaysia',
    'LIBYA': 'libya',
    'nan': 'australia',
    'CUBA': 'cuba',
    'MAURITIUS': 'mauritius',
    'SOLOMON ISLANDS': 'solomon islands',
    'ST HELENA, British overseas territory': 'uk',
    'COMOROS': 'comoros',
    'REUNION': 'france',
    'UNITED KINGDOM': 'uk',
    'UNITED ARAB EMIRATES': 'uae',
    'CAPE VERDE': 'cape verde',
    'Fiji': 'fiji',
    'DOMINICAN REPUBLIC': 'dominican republic',
    'CAYMAN ISLANDS': 'cayman islands',
    'ARUBA': 'aruba',
    'MOZAMBIQUE': 'mozambique',
    'PUERTO RICO': 'puerto rico',
    'ATLANTIC OCEAN': 'australia',
    'GREECE': 'greece',
    'ST. MARTIN': 'netherlands',
    'FRANCE': 'france',
    'TRINIDAD & TOBAGO': 'trinidad and tobago',
    'KIRIBATI': 'kiribati',
    'DIEGO GARCIA': 'diego garcia',
    'TAIWAN': 'taiwan',
    'PALESTINIAN TERRITORIES': 'palestina',
    'GUAM': 'usa',
    'NIGERIA': 'nigeria',
    'TONGA': 'tonga',
    'SCOTLAND': 'scotland',
    'CROATIA': 'croatia',
    'SAUDI ARABIA': 'saudi arabia',
    'CHILE': 'chile',
    'ANTIGUA': 'antigua barbuda',
    'KENYA': 'kenya',
    'RUSSIA': 'russia',
    'TURKS & CAICOS': 'uk',
    'UNITED ARAB EMIRATES (UAE)': 'uae',
    'AZORES': 'portugal',
    'SOUTH KOREA': 'south korea',
    'MALTA': 'malta',
    'VIETNAM': 'vietnam',
    'MADAGASCAR': 'madagascar',
    'PANAMA': 'panama',
    'SOMALIA': 'somalia',
    'NEVIS': 'saint kits and nevis',
    'BRITISH VIRGIN ISLANDS': 'uk',
    'NORWAY': 'norway',
    'SENEGAL': 'senegal',
    'YEMEN': 'yemen',
    'GULF OF ADEN': 'yemen',
    'Sierra Leone': 'sierra leone',
    'ST. MAARTIN': 'netherlands',
    'GRAND CAYMAN': 'uk',
    'Seychelles': 'seychelles',
    'LIBERIA': 'liberia',
    'VANUATU': 'vanatu',
    'MEXICO ': 'mexico',
    'HONDURAS': 'honduras',
    'VENEZUELA': 'venezuela',
    'SRI LANKA': 'sri lanka',
    ' TONGA': 'tonga',
    'URUGUAY': 'uruguay',
    'INDIA': 'india',
    'MICRONESIA': 'micronesia',
    'CARIBBEAN SEA': 'caribbean',
    'OKINAWA': 'japan',
    'TANZANIA': 'tanzania',
    'MARSHALL ISLANDS': 'marshall islands',
    'EGYPT / ISRAEL': 'egypt',
    'NORTHERN ARABIAN SEA': 'uae',
    'HONG KONG': 'china',
    'EL SALVADOR': 'el salvador',
    'ANGOLA': 'angola',
    'BERMUDA': 'uk',
    'MONTENEGRO': 'montenegro',
    'IRAN': 'iran',
    'TUNISIA': 'tunesia',
    'NAMIBIA': 'namibia',
    'NORTH ATLANTIC OCEAN': 'usa',
    'SOUTH CHINA SEA': 'china',
    'BANGLADESH': 'bangladesh',
    'PALAU': 'palau',
    'WESTERN SAMOA': 'samoa',
    'PACIFIC OCEAN ': 'usa',
    'BRITISH ISLES': 'uk',
    'GRENADA': 'grenada',
    'IRAQ': 'irak',
    'TURKEY': 'turkey',
    'SINGAPORE': 'singapore',
    'NEW BRITAIN': 'papua new guinea',
    'SUDAN': 'sudan',
    'JOHNSTON ISLAND': 'usa',
    'SOUTH PACIFIC OCEAN': 'australia',
    'NEW GUINEA': 'papua new guinea',
    'RED SEA': 'egypt',
    'NORTH PACIFIC OCEAN': 'usa',
    'FEDERATED STATES OF MICRONESIA': 'micronesia',
    'MID ATLANTIC OCEAN': 'usa',
    'ADMIRALTY ISLANDS': 'papua new guniea',
    'BRITISH WEST INDIES': 'uk',
    'SOUTH ATLANTIC OCEAN': 'ocean',
    'PERSIAN GULF': 'ocean',
    'RED SEA / INDIAN OCEAN': 'ocean',
    'PACIFIC OCEAN': 'australia',
    'NORTH SEA': 'ireland',
    'NICARAGUA ': 'nicaragua',
    'MALDIVE ISLANDS': 'maldive islands',
    'AMERICAN SAMOA': 'american samoa',
    'ANDAMAN / NICOBAR ISLANDAS': 'india',
    'GABON': 'gabon',
    'MAYOTTE': 'mayotte',
    'NORTH ATLANTIC OCEAN ': 'usa',
    'THE BALKANS': 'slovenia',
    'SUDAN?': 'sudan',
    'MARTINIQUE': 'france',
    'INDIAN OCEAN': 'ocean',
    'GUATEMALA': 'guatemala',
    'NETHERLANDS ANTILLES': 'netherlands',
    'NORTHERN MARIANA ISLANDS': 'northern mariana islands',
    'IRAN / IRAQ': 'iran',
    'JAVA': 'indonesia',
    'SIERRA LEONE': 'sierra leone',
    ' PHILIPPINES': 'philippines',
    'NICARAGUA': 'nicaragua',
    'CENTRAL PACIFIC': 'australia',
    'SOLOMON ISLANDS / VANUATU': 'solomon islands',
    'SOUTHWEST PACIFIC OCEAN': 'usa',
    'BAY OF BENGAL': 'india',
    'MID-PACIFC OCEAN': 'australia',
    'SLOVENIA': 'slovenia',
    'CURACAO': 'curazao',
    'ICELAND': 'iceland',
    'ITALY / CROATIA': 'italy',
    'BARBADOS': 'barbados',
    'MONACO': 'monaco',
    'GUYANA': 'guyana',
    'HAITI': 'haiti',
    'SAN DOMINGO': 'dominican republic',
    'KUWAIT': 'kuwait',
    'YEMEN ': 'yemen',
    'FALKLAND ISLANDS': 'falkland islands',
    'CRETE': 'greece',
    'CYPRUS': 'cyprus',
    'EGYPT ': 'egypt',
    'WEST INDIES': 'west indies',
    'BURMA': 'myanmar',
    'LEBANON': 'lebanon',
    'PARAGUAY': 'paraguay',
    'BRITISH NEW GUINEA': 'british new guinea',
    'CEYLON': 'sri lanka',
    'OCEAN': 'ocean',
    'GEORGIA': 'georgia',
    'SYRIA': 'syria',
    'TUVALU': 'tuvalu',
    'INDIAN OCEAN?': 'indian ocean',
    'GUINEA': 'papua new guinea',
    'ANDAMAN ISLANDS': 'india',
    'EQUATORIAL GUINEA / CAMEROON': 'cameroon',
    'COOK ISLANDS': 'cook islands',
    'TOBAGO': 'trinidad and tobago',
    'PERU': 'peru',
    'AFRICA': 'africa',
    'ALGERIA': 'algeria',
    'Coast of AFRICA': 'africa',
    'TASMAN SEA': 'australia',
    'GHANA': 'ghana',
    'GREENLAND': 'greenland',
    'MEDITERRANEAN SEA': 'australia',
    'SWEDEN': 'sweden',
    'ROATAN': 'honduras',
    'Between PORTUGAL & INDIA': 'portugal',
    'DJIBOUTI': 'djibouti',
    'BAHREIN': 'bahrein',
    'KOREA': 'korea',
    'RED SEA?': 'egypt',
    'ASIA?': 'japan',
    'CEYLON (SRI LANKA)': 'sri lanka',
    }
    shark_attacks_dropped['country']= list(map(lambda x: countries.get(x,x),shark_attacks_dropped['country']))
    return shark_attacks_dropped

# We create the dataframe for the final function

def make_a_sexy_dataframe(cleaned_data):
    
    cleaned_data['country'].value_counts().head(10)
    # Plotting top 10 countries for shark attacks

    # First, we create a list of the top 10 countries with shark attacks

    top10_countries = cleaned_data['country'].value_counts().head(10).reset_index()

    top10_countries = pd.DataFrame(top10_countries)

    top10_countries = top10_countries.rename(columns={"country": "shark attack count", "index": "country"})

    return top10_countries


# We make a function to create a plot with the top 10 countries for shark attacks

def make_a_sexy_plot(cleaned_data):
    
    cleaned_data['country'].value_counts().head(10)
    # Plotting top 10 countries for shark attacks

    # First, we create a list of the top 10 countries with shark attacks

    top10_countries = cleaned_data['country'].value_counts().head(10).reset_index()

    top10_countries = pd.DataFrame(top10_countries)

    top10_countries = top10_countries.rename(columns={"country": "shark attack count", "index": "country"})

    # We then plot

    shark_country_plot = sns.barplot(x=top10_countries['country'], y=top10_countries['shark attack count'], palette='viridis', data=top10_countries)

    shark_country_plot.set_xticklabels(shark_country_plot.get_xticklabels(), rotation=45,  horizontalalignment='right')
    
    plt.xlabel("country".upper(), fontsize=10, fontweight='bold')
    
    plot1 = plt.ylabel("shark attack count".upper(), fontsize=10, fontweight='bold')

    plt.title('Top 10 Countries for Getting Shark-Attacked'.upper(), fontsize=15, fontweight='bold', y=1.07)
    
    # We save the figure in our directory
    # transparent = True stand for transparent background
    # bbox_inches='tight' needs to be specified; otherwise, when saving the figure, there are parts that are cut
    
    plt.savefig('shark_attack_count_per_country.png', transparent=True, bbox_inches='tight')

    return plot1
    
 

# We make a function to create a plot with the shark attack density per coastline km


def make_another_sexy_plot(top10_countries):

    # We create a dictionary with the Wikipedia values for cosatline length in km for the top 5 countries

    country_coastline = {
        'country': ['usa', 'australia', 'south africa', 'papua new guinea', 'bahamas'],
        'coastline length (km)': [19929, 35877, 2800, 5152, 3542]
    }

    # We need a new data frame

    top5_countries = pd.DataFrame.from_dict(country_coastline)

    
    top5_countries_density = pd.concat([top5_countries, top10_countries], axis=1, join="inner")

    top5_countries_density['shark attacks per 1 km coastline'] = top5_countries_density['shark attack count']/top5_countries_density['coastline length (km)']

    top5_countries_density['shark attacks per 100 km coastline'] = (top5_countries_density['shark attacks per 1 km coastline']*100).round(2)

    top5_countries_density = top5_countries_density.T.drop_duplicates().T

    # We then plot

    density_plot = sns.barplot(x='country', y='shark attacks per 100 km coastline', palette = 'viridis', data=top5_countries_density)
    
    plt.title('Shark Attack Density per Country Coastline Length')

    plot2 = density_plot.set_xticklabels(density_plot.get_xticklabels(), rotation=45,  horizontalalignment='right')
    
    plt.xlabel("country".upper(), fontsize=10, fontweight='bold')
    
    plot2 = plt.ylabel("shark attacks per 100 km coastline".upper(), fontsize=10, fontweight='bold')
    
    plt.title('Shark Attack Density per Country'.upper(), fontsize=15, fontweight='bold', y=1.07)

    # We save the figure in our directory
    # transparent = True stand for transparent background
    # bbox_inches='tight' needs to be specified; otherwise, when saving the figure, there are parts that are cut
    
    plt.savefig('shark_attack_density_per_country.png', transparent=True, bbox_inches='tight')
    
    
    return plot2


# In[ ]:





# In[ ]:




