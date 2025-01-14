import streamlit as st


st.set_page_config(page_title="Documentation",page_icon="📚")
st.sidebar.success("select a page above")
st.sidebar.image("logo.png",use_container_width=True)
st.title("📚DOCUMENTATION📚 ")


st.title("Game theory introduction")

con1 = st.container(border=True)
con1.write("On the 3rd of september 1949 an american weather monitoring plane collected traces of radioactive isotopes(cerium-141 and yttrium-91) in the area beetween japan and URSS .\n  These isotopes, with a half-life of only one to two months, could only have been produced by a recent nuclear explosion. This discovery led to the conclusion that the Soviets were on the verge of developing a robust nuclear program. As a result, in 1950, the RAND Corporation developed the foundation of 𝗚𝗮𝗺𝗲 𝗧𝗵𝗲𝗼𝗿𝘆.")

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("neumann.png",caption="Famous von Neumann phrase ")

con2 = st.container(border=True)

con2.write("Game theory is a branch of mathematics that seeks to explain the strategic interactions of two or more players in a given situation with defined rules and outcomes. It applies whenever a scenario involving two or more participants has known payouts or quantifiable consequences.\n\n In this app, we focus primarily on the famous 𝗣𝗿𝗶𝘀𝗼𝗻𝗲𝗿 𝘀 𝗗𝗶𝗹𝗲𝗺𝗺𝗮, a classic problem in game theory. In this scenario, two players can either cooperate or defect. If both cooperate, each earns 3 coins. If both defect, the payoff is 1 coin each. If one defects while the other cooperates, the defector earns 5 coins, and the cooperator earns 0.\n\nThis dilemma closely mirrors the US-Soviet conflict, except that the presented dilemma assumes a single encounter. In such a case, defecting is always the better option, regardless of what the opponent does. If the opponent defects, you earn 1 coin by defecting and 0 by cooperating. If the opponent cooperates, you earn 5 coins by defecting and 3 by cooperating. This reasoning explains why both nations ended up producing massive stockpiles of nuclear weapons, wasting nearly 10 trillion dollars that could have been saved through cooperation. Acting solely in self-interest, without considering the broader environment, often results in a worse outcome for all parties involved.\n\nThis leads us to the Iterated 𝗣𝗿𝗶𝘀𝗼𝗻𝗲𝗿 𝘀 𝗗𝗶𝗹𝗲𝗺𝗺𝗮, which aims to explore the dynamics of repeated interactions.")

st.title("Iterated prisoners dilemma")

con3 = st.container(border=True)
con3.write("This specific problem relates to many real-life situations, from the Cold War and international relations to impalas grooming one another and biological ecosystems.\n\nBut what is the best strategy to use?\n\nThis is precisely what Professor Robert Axelrod sought to understand in 1980 by hosting a tournament of strategies in a simulated ecosystem. Various game theorists submitted strategies, which competed in a computer-simulated tournament under specific conditions:\n\nEach strategy played against all others (and itself) in games lasting 200 turns.\n\n The payoffs were identical to those in the standard Prisoner's Dilemma (C/C = 3,3; D/D = 1,1; C/D = 0,5; D/C = 5,0).\n\nThe ultimate goal was to accumulate as many points as possible. For this first tournament (which you can simulate in the _Tournament_ section), Axelrod received 14 strategies, adding a random one himself.") 



st.title("Analysis and adjustments")
con4 = st.container(border=True)
con4.write("After the tournament ended, Axelrod observed that the top-performing strategies shared some common traits:\n\n1.Being Nice – They were not the first to defect.\n\n2.Being Forgiving – Past defections did not overly influence future choices.\n\nBased on these results, Axelrod organized a second tournament, introducing a critical change. In the first tournament, players knew exactly when the final turn would occur. This knowledge made cooperation in the last round irrational since defecting was always the better option. However, this logic cascaded backward, discouraging cooperation even in earlier rounds (a concept tied to von Neumann's backward induction principle).\n\nTo address this, Axelrod introduced a probabilistic end, where the game would last an average of 200 turns but could end unexpectedly. This change prompted more cooperative behavior. In the second tournament, with 62 submitted strategies plus a random one, Axelrod identified two additional key traits:\n\n3,Being Retaliatory – Immediate retaliation against defections.\n\n4.Being Clear – Strategies that were too opaque or unpredictable were harder to understand, leading opponents to default to defection.\n\nFinally, Axelrod added noise to the ecosystem, meaning that decisions (C/D) had a chance of being misinterpreted by the opponent.")

st.title("Conclusions")
con5 = st.container(border=True)
con5.write("The conclusions were somewhat surprising: rarely do we hear that being nice and forgiving is the optimal strategy. Of course, these conclusions depend heavily on the surrounding environment. However, in a balanced environment, such as Axelrod's first tournament (with 7 nice and 7 nasty strategies), the nice strategies consistently outperformed the rest.\n\nThis simple game mirrors real-world conflicts. Cooperation often begins, but once one side defects, revenge follows. If noise causes a peace gesture to be misinterpreted as hostile, escalation can lead to war, with devastating consequences for both sides. In such cases, cooperation from the start would have been far more beneficial for all involved.")

l,m,m,m,r= st.columns(5)
with r:
    st.write("𝓑𝓲𝓪𝓼𝓮𝓽𝓽𝓸 𝓛𝓾𝓬𝓪 ,  𝓪.𝓪.𝟐𝟎𝟐𝟒/𝟐𝟓, 𝟐𝟎𝟔𝟕𝟏𝟖𝟔")