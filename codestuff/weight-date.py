# imports to use

import os
import pandas as pd
import plotly as pt
import numpy as np
import plotly.express as px

# extract weights and dates from records and populate list of lists

weightdate = [
    ["taryn_text_records", "2019-08-31.pdf", 296.6, "2019-08-31"],
    ["taryn_text_records", "2018-09-14.pdf", 322.7, "2018-09-14"],
    ["taryn_text_records", "2018-09-07.pdf", 320.6, "2018-09-07"],
    ["taryn_text_records", "2018-08-17.pdf", 325.4, "2018-08-17"],
    ["taryn_text_records", "2018-08-10.pdf", 318.0, "2018-08-10"],
    ["taryn_text_records", "2018-08-03.pdf", 317.3, "2018-08-03"],
    ["taryn_text_records", "2018-07-27.pdf", 322.0, "2018-07-27"],
    ["taryn_text_records", "2018-06-15.pdf", 315.2, "2018-06-15"],
    ["taryn_text_records", "2018-06-08.pdf", 317.5, "2018-06-08"],
    ["taryn_text_records", "2018-06-01.pdf", 319.3, "2018-06-01"],
    ["taryn_text_records", "2018-05-25.pdf", 318.0, "2018-05-25"],
    ["taryn_text_records", "2018-08-30.pdf", 321.3, "2018-08-30"],
    ["pahuja_records", "20230413-pahuja-records_weightChart.pdf", 337.8, "2019-02-20"],
    ["pahuja_records", "20230413-pahuja-records_weightChart.pdf", 343.8, "2019-03-06"],
    ["pahuja_records", "20230413-pahuja-records_weightChart.pdf", 353.6, "2019-04-29"],
    ["pahuja_records", "20230413-pahuja-records_weightChart.pdf", 355.2, "2019-05-22"],
    ["pahuja_records", "20230413-pahuja-records_weightChart.pdf", 357.7, "2019-07-01"],
    ["pahuja_records", "20230413-pahuja-records_weightChart.pdf", 345.4, "2019-07-10"],
    ["pahuja_records", "20230413-pahuja-records_weightChart.pdf", 354.0, "2019-07-24"],
    ["pahuja_records", "20230413-pahuja-records_weightChart.pdf", 322.7, "2019-08-07"],
    ["pahuja_records", "20230413-pahuja-records_weightChart.pdf", 304.9, "2019-08-28"],
    ["pahuja_records", "20230413-pahuja-records_weightChart.pdf", 263.9, "2019-11-27"],
    ["pahuja_records", "20230413-pahuja-records_weightChart.pdf", 232.8, "2020-10-14"],
]

cols = ["data_src", "data_src_filename", "weight_in_lbs", "date_measured"]


# create pandas dataframe from weightdate data and cols columns

weightdate_df = pd.DataFrame(data=weightdate, columns=cols)
print(weightdate_df)

# cast 'date_measured' data as datetime
# sort dataframe in-place by 'date_measured'

weightdate_df["date_measured"] = pd.to_datetime(weightdate_df["date_measured"])
weightdate_df.sort_values(by="date_measured", ascending=False, inplace=True)
weightdate_df["date_measured"]


# extract 'year', 'month', and 'day' data into respective columns from 'date_measured' col

weightdate_df["year"] = weightdate_df["date_measured"].dt.year
weightdate_df["month"] = weightdate_df["date_measured"].dt.month
weightdate_df["day"] = weightdate_df["date_measured"].dt.day

print(weightdate_df)

# Generate plotly.express linechart of weights over time

names = {"Date Measured": "date_measured"}

fig = px.line(
    weightdate_df,
    x=weightdate_df["date_measured"],
    y=weightdate_df["weight_in_lbs"],
    title="Tyler M. Neher - Measured Weight Over Time",
    markers=True,
    render_mode="svg",
    labels={"date_measured": "Date Measured", "weight_in_lbs": "Weight (lbs)"},
)

fig.show()

fig.write_image("weight-date.svg")
fig.write_image("weight-date.png")
fig.write_html("index.html", include_plotlyjs="cdn")
