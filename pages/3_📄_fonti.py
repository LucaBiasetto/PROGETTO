import streamlit as st
from streamlit_player import st_player


st.set_page_config(page_title="Fonti",page_icon="📄")
st.sidebar.success("select a page above")


st.title("📄 Fonti 📄")
st.write("https://axelrod.readthedocs.io/en/stable/")

st.subheader("video di ispirazione")
st.video("https://www.youtube.com/watch?v=mScpHTIi-kM&list=WL&index=2&t=1416s/?embed=true")
#st.components.v1.iframe


#st.html("<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>")
#st.html("<iframe width="560" height="315" src="https://www.youtube.com/embed/mScpHTIi-kM?si=JSvc0Jbs-qtJUWKA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>")
