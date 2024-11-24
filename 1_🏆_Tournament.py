import polars as pl
import streamlit as st
import axelrod as axl
from icecream import ic
import csv
import pandas as pd
import altair as alt

#TUTORIAL   https://www.youtube.com/watch?v=Sb0A9i6d320&list=PL7QI8ORyVSCaejt2LICRQtOTwmPiwKO2n&index=2


st.set_page_config(page_title="Tournament",page_icon="🏆")
st.sidebar.success("select a page above")

#inizializzazione parametri
st.sidebar.header("Please filter here: ")
players=st.sidebar.multiselect("scegli strategie che parteciperann al torneo",axl.axelrod_first_strategies,placeholder="scegli tre o più alternative: ",
                       format_func=lambda x: str(x).strip("<'>").split('.')[-1])
players=[p()for p in players]
#trovare lista di strategie che mi interessa 
#st.write(type(players[0]))
noise=st.sidebar.slider("scegli il rumore : ", min_value=0.0,max_value=1.0)
prob_end=st.sidebar.slider("scegli la probabilità che il singolo match finisca ogni turno: ", min_value=0.0,max_value=1.0)
turns=st.sidebar.slider("scegli il numero di turni: ", min_value=0,max_value=1000)


#------------------Torneo--------------------------------
st.radio("test radio button",(axl.axelrod_first_strategies),format_func=lambda x: str(x).strip("<'>").split('.')[-1])

#https://github.com/Axelrod-Python/Axelrod/blob/dev/axelrod/strategies/axelrod_first.py implemento wiki








tournament=axl.Tournament(players=players,noise=noise,prob_end=prob_end,turns=turns)
results=tournament.play()
summary = results.summarise()
st.title('Risultati torneo')
st.write(summary)


plot = axl.Plot(results)
p = plot.boxplot()
p2 = plot.winplot()
p3 = plot.payoff()
st.subheader("Boxplot")
st.write(p)
st.subheader("Winplot")
st.write(p2)
st.subheader("Payoffplot")
st.write(p3)




results.write_summary('summary.csv')
"""
with open('summary.csv', 'r') as outfile:
    csvreader = csv.reader(outfile)
    for row in csvreader:
        st.write(row)

df=pd.read_csv("summary.csv")

st.subheader("prova dataframe pandas")
st.dataframe(df)

ct=st.radio("test radio button",(players))
#df1=df[df["Name"]==ct]
#count=df1["wins"].value_counts().head(20)

#st.bar_chart(count)
#video https://www.youtube.com/watch?v=hRPt4r_xVIg

"""


data=pl.read_csv("summary.csv")
st.write("DATAFRAME")    
st.dataframe(summary)


chart=(
    alt.Chart(data)
    .mark_circle()
    .encode(alt.X("Wins"),alt.Y("Median_score"),alt.Color("Name"))
)
st.altair_chart(chart)
x_y=st.multiselect("choose what x and y axes will represent",data.columns,placeholder="choose 2 : ",max_selections=2)
st.write(x_y)
chartInt=(
    alt.Chart(data)
    .mark_circle()
    .encode(alt.X(x_y[0]),alt.Y(x_y[1]),alt.Color("Name"))
)
st.altair_chart(chartInt)
chart2=(
    alt.Chart(data)
    .mark_circle()
    .encode(alt.X("Wins"),alt.Y("Cooperation_rating"),alt.Color("Name"))
)
st.altair_chart(chart2)

chart3=(
    alt.Chart(data)
    .mark_circle()
    .encode(alt.X("Wins"),alt.Y("Rank"),alt.Color("Name"))
)
st.altair_chart(chart3)



st.subheader("scores")
st.write(results.scores)
st.subheader("payoff_matrix")
st.write(results.payoff_matrix)
st.subheader("ranking")
st.write(results.ranking)
st.subheader("ranked_names")
st.write(results.ranked_names)
st.subheader("progress_bar")
st.write(results.progress_bar)
st.subheader("wins")
st.write(results.wins)                           





# domanda  come gestire grafici, implemeto wiki come? con tanti if?, aggiungere colonne oe scores al dataframe?con polars?,creare nuoa colonna rankings che parto da 1 e non da 0?, fare più grafici non interattivi?o solo uno ma interattivo on possibiliotà di cambiare asse x e y ?tengo grafici di axl?, come far funzionare Image?, for in match no funzionante


                          

