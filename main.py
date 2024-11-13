import polars as pl
import streamlit as st
import axelrod as axl
from icecream import ic

def format_function(list):
    print(list)

players=st.multiselect("scegli strategie che parteciperann al torneo",axl.basic_strategies,placeholder="scegli tre o più alternative: ")#trovare lista di strategie che mi interessa 
noise=st.slider("scegli il rumore : ", min_value=0.0,max_value=1.0)
prob_end=st.slider("scegli la probabilità che il singolo match finisca ogni turno: ", min_value=0.0,max_value=1.0)
turns=st.slider("scegli il numero di turni: ", min_value=0,max_value=1000)
#tournament=axl.Tournament(players=players,noise=noise,prob_end=prob_end,turns=turns)
#results=tournament.play()


#summary = results.summarise()
#ic(summary)
                          

