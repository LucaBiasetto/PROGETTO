import polars as pl
import streamlit as st
import axelrod as axl
from icecream import ic
import csv

#inizializzazione parametri
players=st.multiselect("scegli strategie che parteciperann al torneo",axl.strategies,placeholder="scegli tre o più alternative: ",
                       format_func=lambda x: str(x).strip("<'>").split('.')[-1])
players=[p()for p in players]
#trovare lista di strategie che mi interessa 
#st.write(type(players[0]))
players2=st.multiselect("scegli strategie che parteciperann al torneo",axl.basic_strategies,placeholder="scegli due alternative: ",max_selections=2,format_func=lambda x: str(x).strip("<'>").split('.')[-1])#trovare lista di strategie che mi interessa
players2=[p()for p in players2]
noise=st.slider("scegli il rumore : ", min_value=0.0,max_value=1.0)
prob_end=st.slider("scegli la probabilità che il singolo match finisca ogni turno: ", min_value=0.0,max_value=1.0)
turns=st.slider("scegli il numero di turni: ", min_value=0,max_value=1000)


#---------------Match--------------------
#match=axl.Match(players=players2,turns=turns,noise=noise)
#ic(match.play())
#ic((match.sparklines(c_symbol='🤝 ', d_symbol='❌ ')))
#ic(match.scores())
#ic(match.final_score())
#ic(match.final_score_per_turn())
#ic(match.winner())
#ic(match.cooperation())  # The count of cooperations
#ic(match.normalised_cooperation())  # The count of cooperations per turn


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
 
st.write("DATAFRAME")    
st.dataframe(summary)
st.write("TABLE") 
st.table(summary)

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





# domanda alias per visualizzazione(metodo format function), come gestire grafici

                          

