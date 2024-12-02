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
pla=st.radio("test radio button",(axl.axelrod_first_strategies),format_func=lambda x: str(x).strip("<'>").split('.')[-1])

#https://github.com/Axelrod-Python/Axelrod/blob/dev/axelrod/strategies/axelrod_first.py implemento wiki
cont=st.container(border=True)
if repr(pla)=="FirstByDavis":
    cont.write("A player starts by cooperating for 10 rounds then plays Grudger,defecting if at any point the opponent has defected.")
    







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

lim=len(players)+1

data=pl.read_csv("summary.csv").with_columns((pl.col("Rank") +int(1)).alias("Rank"))#aggiungo come colonna score totale e forse anche match length ecc
st.write("DATAFRAME")    
st.dataframe(data)
st.write("datafram scritto con summary")
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
    .mark_point()
    .encode(alt.X(x_y[0]),alt.Y(x_y[1]),alt.Color("Name"))
)
st.altair_chart(chartInt)
col1,col2,col3=st.columns(3)
chart2=(
    alt.Chart(data)
    .mark_point()
    .encode(alt.X("Wins").scale(domain=[0,lim]),alt.Y("Cooperation_rating"),alt.Color("Name",legend=None)).properties(title="cooperation rate per wins")
)
with col1:
    st.altair_chart(chart2,use_container_width=True)

chart2_1=(
    alt.Chart(data)
    .mark_point()
    .encode(alt.X("Rank").scale(domain=[0,lim]),alt.Y("Cooperation_rating"),alt.Color("Name",legend=None)).properties(title="cooperation rate per rank"))
with col2:
    st.altair_chart(chart2_1,use_container_width=True)

container=st.container(border=True)
container.write("from the graphs above what can we conclude about winning the single match and cooperating rarely? does it payoff? does winning the single battle win u the war?or doesn't it? does being a jerk and not cooperating work ?") 
chart3=(
    alt.Chart(data)
    .mark_point()
    .encode(alt.X("Rank").scale(domain=[0,lim]),alt.Y("Wins").scale(domain=[0,lim]),alt.Color("Name")).properties(title="rank of player per wins")
)
with col3:
    st.altair_chart(chart3)

st.write("bozza perchè non ho la variabile di intresse score totale al posto di wins")
chart4=(
    alt.Chart(data)
    .mark_bar()
    .encode(alt.X("Wins"),alt.Y("Name"),alt.Color("Name"))
)
st.altair_chart(chart4)


#https://axelrod.readthedocs.io/en/stable/how-to/access_tournament_results.html#tournament-results
st.subheader("scores")
st.write(results.scores)#lungo n-1 ma sempre con 9 elementi dentro che non riesco a interpreatre
st.subheader("payoff_matrix")
st.write(results.payoff_matrix)#utilizzabile
st.subheader("wins")
st.write(results.wins)#lungo n-1 ma sempre con 9 elementi dentro che non riesco a interpreatre
st.subheader("normalised scores")    
st.write(results.normalised_scores)  #lungo n-1 ma sempre con 9 elementi dentro che non riesco a interpreatre                     
st.subheader("match length")    
st.write(results.match_lengths) #lungo n-1 e n-1 elementi per elemento




# domanda  come gestire grafici, implemeto wiki come? con tanti if?, aggiungere colonne oe scores al dataframe?con polars?,creare nuoa colonna rankings che parto da 1 e non da 0?, fare più grafici non interattivi?o solo uno ma interattivo on possibiliotà di cambiare asse x e y ?tengo grafici di axl?, come far funzionare Image?, for in match no funzionante,scores è sempre lungo 9 prchè?

#noin funziona radiobutton, aggiungere colonne (scores ) e capire cosa significano, faccio wiki a tendina con tutti o interattiva con tanti iof macchuinosi?
                          

