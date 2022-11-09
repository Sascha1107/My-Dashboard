import streamlit as st
import pandas as pd
import plotly.express as px

import streamlit as st
#from pathlib import Path
#from streamlit_chat import message
import os
import time
import locale

locale.setlocale(locale.LC_ALL, 'de_DE.utf-8')



df = pd.read_excel("Rohdaten.xlsx")






st.set_page_config(layout="wide",page_title="ARGE-Dashboard")



df['Auftragswert'].round(decimals =0)

print(df["Auftragswert"])


st.title(":bar_chart: ARGE-Dashboard")




#st.sidebar.header("Bitte hier filtern")
#my_bar = st.progress(0)

#for percent_complete in range(100):
    #time.sleep(0.05)
    #my_bar.progress(percent_complete + 1)


Region = st.sidebar.multiselect("Region",
                                    options=df["Region"].unique(),
                                    default=df["Region"].unique(),
                                    )

Projektkategorie = st.sidebar.multiselect("Projektkategorie",
                                              options=df["Projektkategorie"].unique(),
                                              default=df["Projektkategorie"].unique(),
                                              )


df_choice = df.query("Region == @Region & Projektkategorie== @Projektkategorie")




st.markdown("---")

revenue_per_region = df_choice.groupby(["Region"]).sum()[["Auftragswert"]].sort_values(by="Auftragswert")
cost_per_region = df_choice.groupby(["Region"]).sum()[["Kalkulationswert"]].sort_values(by="Kalkulationswert")
products_cost = df_choice.groupby(["Produkte"]).sum()[["Kalkulationswert"]].sort_values(by="Kalkulationswert")
products_revenue = df_choice.groupby(["Produkte"]).sum()[["Auftragswert"]].sort_values(by="Auftragswert")

#----Alle Diagramme---#

fig_revenue_values = px.bar(
        revenue_per_region,
        x="Auftragswert",
        y=revenue_per_region.index,
        orientation="h",
        title ="<b> Auftragswert ARGE je Region </b>",
        color_discrete_sequence=["#1CE5C3"] * len(revenue_per_region),
        template="simple_white",
        text_auto=True,
    )

fig_cost_values = px.bar(
        cost_per_region,
        x="Kalkulationswert",
        y=cost_per_region.index,
        orientation="h",
        title ="<b> Kalkulationswert ARGE je Region </b>",
        color_discrete_sequence=["#1CE5C3"] * len(cost_per_region),
        template="simple_white",
        text_auto=True,
    )


fig_product_values = px.bar(
        products_revenue,
        x="Auftragswert",
        y=products_revenue.index,
        orientation="h",
        title ="<b> Auftragswert je Produkt </b>",
        color_discrete_sequence=["#1CE5C3"] * len(products_revenue),
        template="simple_white",
        text_auto=True,
    )


fig_product_cost = px.bar(
        products_cost,
        x="Kalkulationswert",
        y=products_cost.index,
        orientation="h",
        title ="<b> Kalkulationswert je Produkt </b>",
        color_discrete_sequence=["#1CE5C3"] * len(products_cost),
        template="simple_white",
        text_auto=True,
    )


total_value = int(df_choice["Auftragswert"].sum())
total_value_final = locale.format('%d', total_value, 1)
total_cost = int(df_choice["Kalkulationswert"].sum())
total_cost_final = locale.format('%d', total_cost, 1)

number_of_projects = len(df_choice.index)

col1, col2,col3 = st.columns(3)




with col1:
        st.subheader("Auftragswert in ARGEN")
        st.subheader(f"{total_value_final} €")

with col2:
        st.subheader("Kalkulationswert in ARGEN")
        st.subheader(f"{total_cost_final} €")

with col3:
    st.subheader("Anzahl Projekte in ARGEN")
    st.subheader(f" # {number_of_projects}")


my_bar_chart = px.bar(revenue_per_region, y=["Auftragswert"], color_discrete_sequence=["#1CE5C3"],text_auto=True, title ="<b> Kalkulationswert je Produkt </b>", )


my_bar_chart.update_xaxes(showgrid=False, zeroline=False)
my_bar_chart.update_yaxes(showgrid=False, zeroline=False)

my_bar_chart.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)


first_column, second_column  = st.columns(2)

first_column.plotly_chart(my_bar_chart,use_container_width=True)
second_column.plotly_chart(my_bar_chart,use_container_width=True)

third_column, fourth_column  = st.columns(2)

third_column.plotly_chart(my_bar_chart,use_container_width=True)
fourth_column.plotly_chart(my_bar_chart,use_container_width=True)

st.markdown("---")

st.subheader("ARGE-Projektübersicht")

st.dataframe(df_choice)

st.markdown("---")

st.header("Haben Sie Fragen zu dem Bericht? Fragen Sie unseren Bot")





st.markdown("---")



# creating a new chatbot
#chatbot = Chatbot('Edureka')
#trainer = ListTrainer(chatbot)
#trainer.train(
    #['hi, can I help you find a course', 'sure I'd love to find you a course', 'your course have been selected'])

     # getting a response from the chatbot
     #response = chatbot.get_response("I want a course")
#print(response)



hide_style = """
            <style>
             #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

st.markdown(hide_style,unsafe_allow_html=True)