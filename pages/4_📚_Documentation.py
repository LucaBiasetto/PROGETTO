import streamlit as st


st.set_page_config(page_title="Documentation",page_icon="📚")
st.sidebar.success("select a page above")

st.title("📚DOCUMENTATION📚 ")



st.title("Game theory introduction")
con1 = st.container(border=True)
con1.write("On the 3rd of september 1949 an american weather monitoring plane collected traces of radioactive isotopes(cerium 141 and yttrium 91 ) in the area beetween japan and URSS .\n  But those isotopes have an half life of only one/two months and they could havce been produced only from a nuclear explosion, so they concluded that the soviets where on the point of developing a strong nuclear  plan. \n and that's why in 1950 the RAND Corporation developed  '𝒯𝐻𝐸 𝒢𝒜𝑀𝐸 𝒯𝐻𝐸𝒪𝑅𝒴'   ")

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("C:\\Users\Luca Biasetto\\OneDrive\Desktop\\3zo anno\Sistemi 2\progetto\\neumann.png",caption="Famous von Neumann phrase ")

con2 = st.container(border=True)
con2.write("Game theory is a brench of mathematichs that tries to explain the strategic actions of two or more players in a given situation with set rules and outcomes. Any time a situation with two or more players involves known payouts or quantifiable consequences. \n In this app we care mostly about the famous 'prisoners dilemma' a problem in game theory where 2 players can either cooperate and earn each 3 coins, if both detect the payoff is 1 coin each, if one defects and the other cooperates the defector gets 5 coins and the other 0    . \nThat in fact resembled a lot the US-soviet conflict, except for the fact that the dilemma presented is a single encounter, in fact in that case u are better off detecting no matter what the opponent does, given ur goal to earn more money as possible(if enemy defects u earn 1 coin by defecting and 0 by cooperating, if he cooperates u earn 5 by defecting and 3 by cooperating).\n That's why both nations ended up producing tons of nuclear weapons and wasting close to 10 trillion dollars that they could have kept by cooperating. \n So it seems like acting solely on ur own interests and caring only about one situation not considering the environment they both ended up in a situation where everyone was worse off. \n That's exactly what the '𝐼𝒯𝐸𝑅𝒜𝒯𝐸𝒟 𝒫𝑅𝐼𝒮𝒪𝒩𝐸𝑅𝒮 𝒟𝐼𝐿𝐸𝑀𝑀𝒜' wants to study")

st.title("Iterated prisoners dilemma")
con3 = st.container(border=True)
con3.write("a") 
#riassunto fino a min 4:20