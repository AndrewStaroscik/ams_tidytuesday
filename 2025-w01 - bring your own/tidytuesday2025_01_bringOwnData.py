# setup

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# import and set data for time/date crosstab

df = pd.read_csv('../data/2025/accidentSM.csv')

# Adding a year column and converting to datetime, including the hour
df['year'] = 2022
df['date'] = pd.to_datetime(df[['year', 'MONTH', 'DAY']])
df.head()

# Create the crosstab for the heatmap

crossTab = pd.crosstab(index=df['HOUR'], columns=df['date'])
crossTab = crossTab[crossTab.index != 99]
crossTab.head()

# create the heatmap

full_date_range = pd.date_range(start='2022-01-01', end='2022-12-31', freq='D')

plt.figure(figsize=(16, 9))
sns.heatmap(crossTab, annot=False, cmap='YlOrRd', cbar=True, cbar_kws={'ticks': [0, 4, 8, 12, 16, 20]})

dateLabels = [date.strftime('%b') if pd.notnull(date) and date.day == 15 else '' for date in full_date_range]

ax = plt.gca()
ax.tick_params(axis='x', color='#dedede')  # Change color of tick marks only, not the labels
plt.xticks(ticks=range(len(dateLabels)), labels=dateLabels, rotation=0, color='black', fontsize=15)
plt.yticks(ticks=[0, 6, 12, 18, 24], labels=['12 am', '6 am', '12 pm', '6 pm', '12 am'], rotation=0, fontsize=15)

plt.gca().invert_yaxis() # flip orientation of y-axis (morning at the bottom)

# use text for title for better control (values are relative to x and y axes)
plt.title('')
plt.text( -10, 25.5, 'A Year of fatal traffic accidents in the US (2022)', fontsize= 25)
plt.text( 377, 10, 'Accidents (count)', ha='center', rotation=90, fontsize= 15)

signx = 385
signy= -3

plt.text( signx, signy, 'Andrew Staroscik', fontsize= 18, color='#898989', ha='center')
plt.text( signx, signy-0.7, '#tidytuesday', fontsize= 12, color='#898989', ha='center')
plt.text( 0.02, signy-0.7, 'Source: U.S. National Highway Traffic Safety Administration FARS data', fontsize= 10, color='#898989', ha='left')

plt.xlabel('Day', fontsize=20)
plt.ylabel('Hour', fontsize=20)
plt.tight_layout(rect=[0.025, 0.025, 1, 1])
plt.savefig('./fatalAccidentDayAndTime2022.png', dpi=120)
plt.show()  
