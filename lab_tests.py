import pandas as pd

def test_activity_1a(df):
    if df['failure'].sum() == 6:
        print("Passed!")
    else:
        print("Check your implementation. You should have 6 failures.")
        
        
def test_activity_1b(df):
    if df['failure'].sum() == 0:
        print("[Case 1: Mask failures] Passed!")
    else: 
        print("[Case 1: Mask failures] You should have 0 records where `failure == 1`.")
        
    if df['willFailIn24Hours'].sum() == 48:
        print("[Case 2: Lagged target] Passed!")
    else: 
        print("[Case 2: Lagged target] You should have 48 records where `willFailIn24Hours == 1`.")
        
    first = df.groupby(['SN', 'willFailIn24Hours']).first().reset_index()
    timestamps = first.sort_values('TS')['TS'].values[2:]
    
    if timestamps[0].astype('datetime64[M]').astype(int) % 12 + 1 == 5 and \
        timestamps[1].astype('datetime64[M]').astype(int) % 12 + 1 == 6:
        print("[Case 3: Timestamps] Passed!")
    else:
        print("[Case 3: Timestamps] Check the actual failure timestamp and the first shifted timestamp.")
        
def test_activity_2a(df):
    if sum(df['switch'].unique()) == 1:
        print("Passed!")
    else:
        print("Make sure your encoding is correct and check the signs of the resulting values.")
        
def test_activity_2b(df):
    if df['switch_count'].unique().max() == 191:
        print("Passed!")
    else:
        print("You should have 191 total switches recorded.")
        
        
def test_activity_3a(df):
    if df['hour_sin'].values[1].round(4) == .2588 and df['hour_sin'].values[0] == 0:
        print("Passed!")
    else:
        print("The sine transformation is incorrect. Check the period.")
        
def test_activity_3b(df):
    if df['hour_cos'].values[1].round(4) == .9659 and df['hour_cos'].values[0] == 1:
        print("Passed!")
    else:
        print("The sine transformation is incorrect. Check the period.")