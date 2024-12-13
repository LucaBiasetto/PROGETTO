import streamlit as st


st.set_page_config(page_title="Documentation",page_icon="📚")
st.sidebar.success("select a page above")

st.title("📚DOCUMENTATION📚 ")



st.title("Game theory introduction")
con1 = st.container(border=True)
con1.write("On the 3rd of september 1949 an american weather monitoring plane collected traces of radioactive isotopes(cerium 141 and yttrium 91 ) in the area beetween japan and URSS .\n  But those isotopes have an half life of only one/two months and they could have been produced only from a nuclear explosion, so they concluded that the soviets where on the point of developing a strong nuclear  plan. \n and that's why in 1950 the RAND Corporation developed  '𝒯𝐻𝐸 𝒢𝒜𝑀𝐸 𝒯𝐻𝐸𝒪𝑅𝒴'   ")

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("C:\\Users\Luca Biasetto\\OneDrive\Desktop\\3zo anno\Sistemi 2\progetto\\neumann.png",caption="Famous von Neumann phrase ")

con2 = st.container(border=True)
con2.write("Game theory is a brench of mathematics that tries to explain the strategic actions of two or more players in a given situation with set rules and outcomes. Any time a situation with two or more players involves known payouts or quantifiable consequences. \n In this app we care mostly about the famous 'prisoners dilemma' a problem in game theory where 2 players can either cooperate or defect,if both cooperate both earn each 3 coins, if both defect the payoff is 1 coin each, if one defects and the other cooperates the defector gets 5 coins and the other 0. \nThat in fact resembled a lot the US-soviet conflict, except for the fact that the dilemma presented is a single encounter, in that case u are better off detecting no matter what the opponent does, given ur goal to earn more money as possible(if enemy defects u earn 1 coin by defecting and 0 by cooperating, if he cooperates u earn 5 by defecting and 3 by cooperating).\n That's why both nations ended up producing tons of nuclear weapons and wasting close to 10 trillion dollars that they could have kept by cooperating. \n So it seems like acting solely on your own interests and caring only about one situation not considering the environment will take both ends in a situation where everyone is worse off. \n That's exactly what the '𝐼𝒯𝐸𝑅𝒜𝒯𝐸𝒟 𝒫𝑅𝐼𝒮𝒪𝒩𝐸𝑅𝒮 𝒟𝐼𝐿𝐸𝑀𝑀𝒜' wants to study")

st.title("Iterated prisoners dilemma")
con3 = st.container(border=True)
con3.write("This specific problem is relatable to many real life situation, starting from the cold war and international relations to impalas grooming each other and biological ecosystems.\n\n But what's the best strategy to use?\n\n That's what professor Axelrod in 1980 wanted to understand by hosting a tournament of strategies(computer algorithms) that can be used in a simulated ecosystem with costum payoffs. Many game theorists sent their strategy that was gonna compete in a computer simulated tournament with specific settings: \n\n 1.each strategy would play all the other strategies and itself in a game of 200 turns \n\n2. the payoffs were the same of the prisoners dilemma so (C/C=3,3;D/D=1,1;C/D=0,5;D/C=5,0) \n\n The ultimate goal was to have more points as possible at the end of the tournament. For this first Tournament, that u can simulate by yourself in the 'Tournament section', Axelrod received 14 strategies adding a random one by himself. ") 


st.title("Analisis and adjustments")
con4 = st.container(border=True)
con4.write("After the tournament ended the top performing strategies all shared some qualities:\n\n 1. Being Nice --> not the first to defect \n\n 2. Being Forgiving --> defection from before last round don't affect the choice of the current round \n\n After those results he announced a new tournament changing a simple thing that was a bit odd, in fact if the strategy knew when the last turn exactly was why cooperate in the last round?; It was like a non iterated prisoners dilemma, u are better off defecting in any case,but also it comes back to Von Neumann phrase, if u know u both defect last round there is no reason to cooperate in the second last round and so on to the first round.\n So a probabilistic end was added where on average it was 200 round but u never know when it was gonna end. \n After the 2nd tournament with 62 strategies sent + random he identified 2 more qualities: \n\n 3.Being Retaliatory --> if opponent defects strike back immediately \n\n 4. Being Clear --> too opaque strategies where too hard to understand so it couldn't predict the next move and so it was better to defect anyway. \n\n The last adjustment made was adding noise to the ecosystem, noise made that every time a decision was taken(C/D) there was a chance that the opponent understood the opposite.   ")

st.title("Conclusions")
con5 = st.container(border=True)
con5.write("The conclusions were kind off shocking,rarely we hear that being nice and forgiving is the best strategy. Of course the conclusions were chained to the surrounding environment but we can say that in a balanced environment where 7 strategies are good and 7 nasty(like axelrod first tournament), all the nice strategies were at the top. \n\n And this little game is also very relatable to reality like conflicts, u start by cooperating but after the first time the enemy nation does something wrong revege comes in, and if an accident happens and a peace message is mistaken for a nasty one(noise) it's war on both sides and many lives end, when it was better to cooperate togheter in the first place.")

l,m,m,m,r= st.columns(5)
with r:
    st.write("𝓑𝓲𝓪𝓼𝓮𝓽𝓽𝓸 𝓛𝓾𝓬𝓪 ,  𝓪.𝓪.𝟐𝟎𝟐𝟒/𝟐𝟓, 𝟐𝟎𝟔𝟕𝟏𝟖𝟔")