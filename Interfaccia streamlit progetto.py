import polars as pl
import streamlit as st
import axelrod as axl
from icecream import ic

st.multiselect("scegli strategie che parteciperann al torneo",axl.axelrod_first_strategies)
