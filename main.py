import polars as pl
import streamlit as st
import axelrod as axl
from icecream import ic

players=st.multiselect("scegli strategie che parteciperann al torneo",axl.axelrod_first_strategies)
tournament=axl.Tournament(players=players,noise=0.1,prob_end=0.15,turns=20)
results=tournament.play()


summary = results.summarise()
ic(summary)
                          

