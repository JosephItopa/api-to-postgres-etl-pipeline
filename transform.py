import pandas as pd

def transformation(df):
    # enforce correct datatype and maintain consistent letter case
    df['id'] = df['id'].astype('str')
    df['name'] = df['name'].str.lower()
    df['status'] = df['status'].str.lower()
    df['species'] = df['species'].str.lower()
    df['type'] = df['type'].str.lower()
    df['gender'] = df['gender'].str.lower()
    df['created'] = pd.to_datetime(df['created'])

    # feature engineering
    #df_origin = pd.json_normalize(df["origin"])
    #df = df.join(df_origin)
    df["origins"] = df["origin"].apply(lambda x: x["name"])
    df["locations"] = df["location"].apply(lambda x: x["name"])
    data = df[['id', 'name', 'status', 'species', 'type',
         'gender', 'created', 'origins', 'locations', 'episode', 'url']]
    #data = data.drop_duplicates(inplace=True)
    return data.drop_duplicate(inplace=True)

# db-postgres; tbl-rickyandmorty