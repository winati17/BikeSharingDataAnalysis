import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# Memuat data dan melakukan preprocessing
all_df = pd.read_csv("dataset/data_hour.csv")
all_df["dteday"] = pd.to_datetime(all_df["dteday"])

# Visualisasi menggunakan Streamlit
st.header("Bike-Sharing Dataset Analysis Dashboard :sparkles:")

# Visualisasi Number of Orders per Year
st.subheader("Number of Orders per Year")
col1, col2 = st.columns(2)
with col1:
    df_2011 = all_df[all_df['dteday'].dt.year == 2011]
    st.metric("Total orders in 2011", value=df_2011.cnt.sum())
with col2:
    df_2012 = all_df[all_df['dteday'].dt.year == 2012]
    st.metric("Total orders in 2012", value=df_2012.cnt.sum())

# Visualisasi Number of Orders per Month
st.subheader("Number of Orders per Month")
# Untuk tahun 2011
monthly_orders_df_2011 = df_2011.resample(rule='M', on='dteday').agg({
    "cnt": "sum"
})
monthly_orders_df_2011.index = monthly_orders_df_2011.index.strftime('%B')
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    monthly_orders_df_2011["cnt"],
    marker='o', 
    linewidth=2,
    color="#FFAAB9"
)
ax.set_title("In 2011", loc="center", fontsize=50)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15, rotation=30)
st.pyplot(fig)

# Untuk tahun 2012
monthly_orders_df_2012 = df_2012.resample(rule='M', on='dteday').agg({
    "cnt": "sum"
})
monthly_orders_df_2012.index = monthly_orders_df_2012.index.strftime('%B')
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    monthly_orders_df_2012["cnt"],
    marker='o', 
    linewidth=2,
    color="#FFAAB9"
)
ax.set_title("In 2012", loc="center", fontsize=50)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15, rotation=30)
st.pyplot(fig)

# Visualisasi Most & Least Rent by Hour
st.subheader("Most & Least Rent by Hour")
hourly_order_df = all_df.groupby('hr')['cnt'].mean().reset_index()
col1, col2 = st.columns(2)
 
with col1:
    dfcol1 = hourly_order_df.sort_values(by="cnt", ascending=False).head(5).reset_index()
    colors = ["#FFAAB9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
        y="cnt", 
        x=dfcol1.index,
        data=dfcol1,
        palette=colors,
        ax=ax
    )
    ax.set_title("Most Rent by Hour", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    ax.set_xticklabels(dfcol1["hr"])
    st.pyplot(fig)
 
with col2:
    dfcol2 = hourly_order_df.sort_values(by="cnt").head(5).reset_index()
    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
        y="cnt", 
        x=dfcol2.index,
        data=dfcol2,
        palette=colors,
        ax=ax
    )
    ax.set_title("Least Rent by Hour", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    ax.set_xticklabels(dfcol2["hr"])
    st.pyplot(fig)

# Visualisasi Most & Least Rent by Season
st.subheader("Most & Least Rent by Season") 
seasonal_order_df = all_df.groupby('season')['cnt'].mean().reset_index()
seasonal_order_df['season'] = ['spring', 'summer', 'fall', 'winter']
col1, col2 = st.columns(2)
 
with col1:
    colors = ["#FFAAB9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
        y="cnt", 
        x="season",
        data=seasonal_order_df.sort_values(by="cnt", ascending=False),
        palette=colors,
        ax=ax
    )
    ax.set_title("Most Rent by Season", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)
 
with col2:
    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
        y="cnt", 
        x="season",
        data=seasonal_order_df.sort_values(by="cnt"),
        palette=colors,
        ax=ax
    )
    ax.set_title("Least Rent by Season", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

# Menampilkan caption
min_date = all_df["dteday"].min()
max_date = all_df["dteday"].max()
start_date, end_date = st.date_input(
    label='Time span',
    min_value=min_date,
    max_value=max_date,
    value=[min_date, max_date]
)
st.caption('Made by Winati Mutmainnah')
