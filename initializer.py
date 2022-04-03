import pandas as pd

phone_df = pd.DataFrame({"name":[], "phone_no": [], "lat": [], "long": []})
phone_df.to_csv("./data/phone_no.csv", index=False, mode="w")
data_df = pd.DataFrame({"comment":[], "lat":[], "long": []})
data_df.to_csv("./data/user_data.csv", index=False, mode="w")
rating_df = pd.DataFrame({"rating": [], "lat": [], "long": []})
rating_df.to_csv("./data/user_ratings.csv", index=False, mode="w")