import pandas as pd

data = {
    'Player': ['Eric Garcia', 'Pau Cubarsi', 'Jules Kounde', 'Lamine Yamal', 
               'Ferran Torres', 'Pedri', 'Alejandro Balde', 'Gerard Martin', 
               'Frankie De Jong', 'Raphinha', 'Dani Olmo', 'Robert Lewandowski', 
               'Fermin Lopez', 'Ronaldo Araujo', 'Roony Bardghji', 'Marcus Rashford',
               'Marc Casado', 'Marc Bernal', 'Andreas Christensen', 'Dro Fernandez',
               'Joao Cancelo', 'Jofre Torrents', 'Gavi', 'Joan Garcia', 
               'Marc-Andre ter Stegen', 'Wojciech Szczesny'],
    
    'Position': ['DEF, MID', 'DEF', 'DEF', 
                 'FWD', 'FWD', 'MID', 'DEF', 
                 'DEF', 'MID', 'FWD', 'MID', 
                 'FWD', 'MID', 'DEF', 'FWD', 
                 'FWD', 'MID', 'MID', 'DEF', 
                 'MID', 'DEF', 'DEF', 'MID', 
                 'GK', 'GK', 'GK'],
    
    'Apperances': [29, 25, 28, 24, 
                   26, 23, 24, 27, 
                   23, 18, 21, 21, 
                   21, 16, 14, 28, 
                   19,12, 17, 5, 
                   0, 4, 2, 19, 
                   1, 9],
    
    'Goals': [1, 0, 3, 10, 
              15, 2, 0, 0, 
              0, 11, 5, 10, 
              8, 2, 2, 7, 
              0, 0, 1, 0, 
              0, 0, 0, 0, 
              0, 0],
    
    'xG': [2.5, 0.3, 1.5, 7.1,
           10.9, 1.3, 0.3, 0.1,
           0.7, 6.0, 3.8, 8.5,
           3.8, 0.4, 1.0, 5.1,
           0.3, 0.0, 0.1, 0.0,
           0.0, 0.0, 0.0, 0.0,
           0.0, 0.0],
    
    'xAG': [1.4, 0.3, 1.8, 7.5,
           1.9, 3.4, 1.7, 0.5,
           2.3, 3.0, 2.4, 1.1,
           4.1, 0.0, 1.1, 4.6,
           0.2, 0.0, 0.0, 0.3,
           0.0, 0.0, 0.2, 0.0,
           0.0, 0.0],
    
    'Assists': [1, 0, 2, 11, 
                1, 7, 3, 0, 
                4, 5, 2, 2, 
                10, 0, 4, 11, 
                1, 1, 0, 1, 
                0, 0, 1, 0,
                0, 0],
    
    'Progessive Carries': [23, 17, 34, 135,
                           9, 62, 45, 16,
                           43, 45, 21, 7,
                           29, 11, 13, 64,
                           8, 1, 4, 1,
                           0, 0, 1, 0,
                           0, 0],
    
    'Progessive Passes': [154, 92, 102, 108,
                          22, 176, 77, 93,
                          146, 37, 60, 13,
                          56, 36, 14, 57,
                          37, 8, 16, 8,
                          0, 1, 11, 0,
                          0, 0],
    
    'Progessive Passes Received': [33, 1, 91, 208,
                                   100, 66, 133, 46,
                                   28, 119, 66, 52,
                                   92, 5, 40, 201,
                                   10, 4, 0, 7,
                                   0, 0, 3, 0,
                                   0, 0],
    
 
    'Yellow Cards': [2, 1, 4, 3,
                     2, 1, 3, 5,
                     4, 2, 1, 1,
                     4, 2, 0, 2,
                     2, 2, 1, 0,
                     0, 0, 0, 1,
                     0, 0],
    
    'Red Cards': [0, 0, 0, 0,
                  0, 1, 0, 0,
                  2, 0, 0, 0,
                  0, 1, 0, 0,
                  0, 0, 0, 0,
                  0, 0, 0, 0,
                  0, 0
                  ],
    
    'PPG': [2.45, 2.44, 2.43, 2.46,
            2.38, 2.52, 2.33, 2.41,
            2.3, 2.72, 2.38, 2.38,
            2.55, 2.31, 2.43, 2.43,
            2.58, 2.75, 2.35, 3.0,
            0.0, 3.0, 3.0, 2.74,
            3.0, 1.78],
    
    'Mins Played': [2195, 2043, 2139, 1974,
                    1569, 1669, 1754, 1373,
                    1705, 1124, 1094, 1030,
                    1348, 887, 413, 1718,
                    871, 273, 515, 148,
                    0, 110, 66, 1710,
                    90, 810],
    
    'GWs Missed (Inj & Susp)': [0, 0, 0, 4,
                                  1, 4, 4, 0,
                                  3, 6, 5, 3,
                                  5, 5, 0, 1,
                                  0, 3, 17, 2,
                                  0, 0, 23, 6,
                                  16, 0]
    
}

df = pd.DataFrame(data)
df['Goals per 90'] = df['Goals'] / df['Mins Played'] * 90
df['xG per 90'] = df['xG'] / df['Mins Played'] * 90
df['xAG per 90'] = df['xAG'] / df['Mins Played'] * 90
df['Assists per 90'] = df['Assists'] / df['Mins Played'] * 90
df['Progressive Carries per 90'] = df['Progessive Carries'] / df['Mins Played'] * 90
df['Progressive Passes per 90'] = df['Progessive Passes'] / df['Mins Played'] * 90
df['Progressive Passes Received per 90'] = df['Progessive Passes Received'] / df['Mins Played'] * 90
df['Yellow Cards per 90'] = df['Yellow Cards'] / df['Mins Played'] * 90
df['Red Cards per 90'] = df['Red Cards'] / df['Mins Played'] * 90

#df.groupby('Position')['Goals per 90'].mean() 
print(df.iloc[1:4, 0])
#print (df['Mins Played'].mean())

#print(df[df['Mins Played'] > 500].sort_values(by='xG per 90', ascending=False)[['Player', 'Position', 'Mins Played', 'Goals per 90', 'xG per 90']])
df.to_csv('BarcelonaPlayerStats.csv', index=False)