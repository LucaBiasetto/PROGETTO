import polars as pl
import streamlit as st
import axelrod as axl
from icecream import ic
import csv
import pandas as pd

st.set_page_config(page_title="Match",page_icon="⚔️")
st.sidebar.success("select a page above")

st.title("⚔️MATCH⚔️ ")
#inizializzazione parametri
st.sidebar.header("Please filter here: ")

players2=st.sidebar.multiselect("scegli strategie che parteciperann al match",axl.strategies,placeholder="scegli due alternative: ",max_selections=2,format_func=lambda x: str(x).strip("<'>").split('.')[-1])#trovare lista di strategie che mi interessa
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

