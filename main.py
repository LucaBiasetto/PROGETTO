import polars as pl
import streamlit as st
import axelrod as axl
from icecream import ic
import csv
import pandas as pd

#TUTORIAL   https://www.youtube.com/watch?v=Sb0A9i6d320&list=PL7QI8ORyVSCaejt2LICRQtOTwmPiwKO2n&index=2


#inizializzazione parametri
st.sidebar.header("Please filter here: ")
players=st.sidebar.multiselect("scegli strategie che parteciperann al torneo",axl.strategies,placeholder="scegli tre o più alternative: ",
                       format_func=lambda x: str(x).strip("<'>").split('.')[-1])
players=[p()for p in players]
#trovare lista di strategie che mi interessa 
#st.write(type(players[0]))
players2=st.sidebar.multiselect("scegli strategie che parteciperann al torneo",axl.strategies,placeholder="scegli due alternative: ",max_selections=2,format_func=lambda x: str(x).strip("<'>").split('.')[-1])#trovare lista di strategie che mi interessa
players2=[d()for d in players2]
noise=st.sidebar.slider("scegli il rumore : ", min_value=0.0,max_value=1.0)
prob_end=st.sidebar.slider("scegli la probabilità che il singolo match finisca ogni turno: ", min_value=0.0,max_value=1.0)
turns=st.sidebar.slider("scegli il numero di turni: ", min_value=0,max_value=1000)


#---------------Match--------------------


match=axl.Match(players=players2,turns=turns,noise=noise)

results2=match.play()

st.subheader("results")
st.write(results2)
st.subheader("sparklines")
st.write((match.sparklines(c_symbol='🤝 ', d_symbol='❌ ')))
st.subheader("scores")
st.write(match.scores())
st.subheader("final score")
st.write(match.final_score())
st.subheader("final score per turn")
st.write(match.final_score_per_turn())
st.subheader("winner")
st.write(match.winner())
st.subheader("cooperation")
st.write(match.cooperation())  # The count of cooperations
st.subheader("normalised cooperation")
st.write(match.normalised_cooperation())  # The count of cooperations per turn
st.subheader("state distribution")
st.write(match.state_distribution())

#parte grafica di un match (breve) simulato




#------------------Torneo--------------------------------
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





st.write("DATAFRAME")    
st.dataframe(summary)
#st.write(type(st.dataframe(summary)))
st.write("TABLE") 
st.table(summary)
#st.write(type(st.table(summary)))

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





# domanda  come gestire grafici

                          

