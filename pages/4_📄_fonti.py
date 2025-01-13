import streamlit as st



st.set_page_config(page_title="Fonti",page_icon="📄")
st.sidebar.success("select a page above")


st.title("📄 Fonti 📄")
st.write("https://axelrod.readthedocs.io/en/stable/")

st.subheader("video di ispirazione")
st.video("https://www.youtube.com/watch?v=mScpHTIi-kM&list=WL&index=2&t=1416s/?embed=true")


#https://github.com/Axelrod-Python/Axelrod/blob/dev/axelrod/strategies/axelrod_first.py  wikidoc
#https://axelrod.readthedocs.io/en/stable/how-to/access_tournament_results.html#tournament-results help func



l,m,m,m,r= st.columns(5)
with r:
    st.write("𝓑𝓲𝓪𝓼𝓮𝓽𝓽𝓸 𝓛𝓾𝓬𝓪 ,  𝓪.𝓪.𝟐𝟎𝟐𝟒/𝟐𝟓, 𝟐𝟎𝟔𝟕𝟏𝟖𝟔")