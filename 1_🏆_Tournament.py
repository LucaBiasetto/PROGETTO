import polars as pl
import streamlit as st
import axelrod as axl
from icecream import ic
import csv
import pandas as pd
import altair as alt

#TUTORIAL   https://www.youtube.com/watch?v=Sb0A9i6d320&list=PL7QI8ORyVSCaejt2LICRQtOTwmPiwKO2n&index=2


st.set_page_config(page_title="Tournament",page_icon="🏆")
st.sidebar.success("select a page above")

#inizializzazione parametri
st.sidebar.header("Please filter here: ")
players=st.sidebar.multiselect("scegli strategie che parteciperann al torneo",axl.axelrod_first_strategies,placeholder="scegli tre o più alternative: ",
                       format_func=lambda x: str(x).strip("<'>").split('.')[-1])
players=[p()for p in players]
#trovare lista di strategie che mi interessa 
#st.write(type(players[0]))
noise=st.sidebar.slider("scegli il rumore : ", min_value=0.0,max_value=1.0)
prob_end=st.sidebar.slider("scegli la probabilità che il singolo match finisca ogni turno: ", min_value=0.0,max_value=1.0)
turns=st.sidebar.slider("scegli il numero di turni: ", min_value=0,max_value=1000)


#------------------Torneo--------------------------------
pla=st.radio("test radio button",(axl.axelrod_first_strategies),format_func=lambda x: str(x).strip("<'>").split('.')[-1])

#https://github.com/Axelrod-Python/Axelrod/blob/dev/axelrod/strategies/axelrod_first.py implemento wiki
cont=st.container(border=True)
if repr(pla).strip("<'>").split('.')[-1]=="FirstByDavis":
    cont.write("A player starts by cooperating for 10 rounds then plays Grudger,defecting if at any point the opponent has defected.")
    
if repr(pla).strip("<'>").split('.')[-1]=="FirstByDowning":
    cont.write(" This rule selects its choice to maximize its own longterm expected payoff on the assumption that the other rule cooperates with a fixed probability which depends only on whether the other player cooperated or defected on the previous move. These two probabilities estimates are continuously updated as the game progresses. Initially, they are both assumed to be .5, which amounts to the pessimistic assumption that the other player is not responsive. This rule is based on an outcome maximization interpretation of human performances proposed by Downing (1975).")

if repr(pla).strip("<'>").split('.')[-1]=="FirstByFeld":
    cont.write("This rule starts with tit for tat and gradually lowers its probability of cooperation following the other's cooperation to .5 by the two hundredth move. It always defects after a defection by the other. This strategy plays Tit For Tat, always defecting if the opponent defects but cooperating when the opponent cooperates with a gradually decreasing probability until it is only .5. Note that the description does not clearly indicate how the cooperation probability should drop. This implements a linear decreasing function.")    


if repr(pla).strip("<'>").split('.')[-1]=="FirstByGraaskamp":
    cont.write("This rule plays tit for tat for 50 moves, defects on move 51, and then plays 5 more moves of tit for tat. A check is then made to see if the player seems to be RANDOM, in which case it defects from then on. A check is also made to see if the other is TIT FOR TAT, ANALOGY (a program from the preliminary tournament), and its own twin, in which case it plays tit for tat. otherwise it randomly defects every 5 to 15 moves, hoping that enough trust has been built up so that the other player will not notice these defections. This is implemented as: \n 1. Plays Tit For Tat for the first 50 rounds; \n 2. Defects on round 51;\n 3. Plays 5 further rounds of Tit For Tat;\n 4. A check is then made to see if the opponent is playing randomly in which case it defects for the rest of the game. This is implemented with a chi squared test. \n5. The strategy also checks to see if the opponent is playing Tit For Tat or a clone of itself. If so it plays Tit For Tat. If not it cooperates and randomly defects every 5 to 15 moves.")

if repr(pla).strip("<'>").split('.')[-1]=="FirstByGrofman":
    cont.write("If the players did different things on the previous move, this rule cooperates with probability 2/7. Otherwise this rule always cooperates.")

if repr(pla).strip("<'>").split('.')[-1]=="FirstByJoss":
    cont.write("This rule cooperates 90% of the time after a cooperation by the other. It always defects after a defection by the other.")    

if repr(pla).strip("<'>").split('.')[-1]=="FirstByNydegger":
    cont.write("The program begins with tit for tat for the first three moves, except that if it was the only one to cooperate on the first move and the only one to defect on the second move, it defects on the third move. After the third move, its choice is determined from the 3 preceding outcomes in the following manner. Let A be the sum formed by counting the other's defection as 2 points and one's own as 1 point, and giving weights of 16, 4, and 1 to the preceding three moves in chronological order. The choice can be described as defecting only when A equals 1, 6, 7, 17, 22, 23, 26, 29, 30, 31, 33, 38, 39, 45, 49, 54, 55, 58, or 61. Thus if all three preceding moves are mutual defection, A = 63 and the rule cooperates.  This rule was designed for use in laboratory experiments as a stooge which had a memory and appeared to be trustworthy, potentially cooperative, but not gullible  (Nydegger, 1978). \n The program begins with tit for tat for the first three moves, except that if it was the only one to cooperate on the first move and the only one to defect on the second move, it defects on the third move. After the     third move, its choice is determined from the 3 preceding outcomes in the following manner. \n .. math::A = 16 a_1 + 4 a_2 + a_3 \nWhere :math:`a_i` is dependent on the outcome of the previous :math:`i` th round.  If both strategies defect, :math:`a_i=3`, if the opponent only defects: \n:math:`a_i=2` and finally if it is only this strategy that defects then :math:`a_i=1`.\nFinally this strategy defects if and only if:\n.. math:: A \\in \\{1, 6, 7, 17, 22, 23, 26, 29, 30, 31, 33, 38, 39, 45, 49, 54, 55, 58, 61\\}\n Thus if all three preceding moves are mutual defection, A = 63 and the rule cooperates. This rule was designed for use in laboratory experiments as a stooge which had a memory and appeared to be trustworthy, potentially cooperative, but not gullible.")  

if repr(pla).strip("<'>").split('.')[-1]=="FirstByShubik":
    cont.write("This rule cooperates until the other defects, and then defects once. If the other defects again after the rule's cooperation is resumed, the rule  defects twice. In general, the length of retaliation is increased by one for each departure from mutual cooperation. This rule is described with its strategic implications in Shubik (1970). Further treatment of its is given in. \n There is some room for interpretation as to how the strategy reacts to a defection on the turn where it starts to cooperate once more. In Shubik (1970) the strategy is described as: \nI will play my move 1 to begin with and will continue to do so, so long as my information shows that the other player has chosen his move 1. If my information tells me he has used move 2, then I will use move 2 for the immediate k subsequent periods, after which I will resume using move 1. If he uses his move 2 again after I have resumed using move 1, then I will switch to move 2 for the k + 1 immediately subsequent periods . . . and so on, increasing my retaliation by an extra period for each departure from the (1, 1) steady state.\n\n This is interpreted as: \n The player cooperates, if when it is cooperating, the opponent defects it defects for k rounds. After k rounds it starts cooperating again and   increments the value of k if the opponent defects again.") 

if repr(pla).strip("<'>").split('.')[-1]=="FirstByTullock":
    cont.write("This rule cooperates on the first eleven moves. It then cooperates 10% less than the other player has cooperated on the preceding ten moves. This     > rule is based on an idea developed in Overcast and Tullock (1971). Professor Tullock was invited to specify how the idea could be implemented, and he did so out of scientific interest rather than an expectation that it would be a likely winner. \nThis is interpreted as:\nCooperates for the first 11 rounds then randomly cooperates 10% less often than the opponent has in the previous 10 rounds.") 

if repr(pla).strip("<'>").split('.')[-1]=="FirstByAnonymous":
    cont.write("This rule has a probability of cooperating, P, which is initially 30% and is updated every 10 moves. P is adjusted if the other player seems random, very cooperative, or very uncooperative. P is also adjusted after move 130 if the rule has a lower score than the other player. Unfortunately, the complex process of adjustment frequently left the probability of cooperation in the 30% to 70% range, and therefore the rule appeared random to many other players. Given the lack of detail this strategy is implemented based on the final sentence of the description which is to have a cooperation probability that is uniformly random in the 30 to 70% range.")

if repr(pla).strip("<'>").split('.')[-1]=="FirstBySteinAndRapoport":
    cont.write("This rule plays tit for tat except that it cooperates on the first four moves, it defects on the last two moves, and every fifteen moves it checks to see if the opponent seems to be playing randomly. This check uses a chi-squared test of the other's transition probabilities and also checks for alternating moves of CD and DC. \nThis is implemented as follows:\n1. It cooperates for the first 4 moves.\n2. It defects on the last 2 moves.\n 3. Every 15 moves it makes use of a `chi-squared test http://en.wikipedia.org/wiki/Chi-squared_test` to check if the opponent is playing randomly. If so it defects.") 

if repr(pla).strip("<'>").split('.')[-1]=="FirstByTidemanAndChieruzzi":
    cont.write("This rule begins with cooperation and tit for tat. However, when the other player finishes his second run of defec- tions, an extra punishment is instituted, and the number of punishing defections is increased by one with each run of the other's defections. The other player is given a fresh start if he is 10 or more points behind, if he has not just started a run of defections, if it has been at least 20 moves since a fresh start, if there are at least 10 moves remaining, and if the number of defections differs from a 50-50 random generator by at least 3.0 standard deviations. A fresh start involves two cooperations and then play as if the game had just started. The program defects automatically on the last two moves.\nThis is interpreted as:\n1. Every run of defections played by the opponent increases the number of defections that this strategy retaliates with by 1.\n2. The opponent is given a ‘fresh start’ if:\n  - it is 10 points behind this strategy\n  - and it has not just started a run of defections\n   - and it has been at least 20 rounds since the last ‘fresh start’\n   - and there are more than 10 rounds remaining in the match\n   - and the total number of defections differs from a 50-50 random sample by at least 3.0 standard deviations.\n A ‘fresh start’ is a sequence of two cooperations followed by an assumption that the game has just started (everything is forgotten).\n3. The strategy defects on the last two moves..")    

if repr(pla).strip("<'>").split('.')[-1]=="Random":
    cont.write("Randomly chooses beetwen cooperation and defection wirh a 50% chance")

if repr(pla).strip("<'>").split('.')[-1]=="TitForTat":
    cont.write("Starts by cooperating, then it copies what the opponent did last turn ")    

if repr(pla).strip("<'>").split('.')[-1]=="Grudger":
    cont.write("Start by cooperating and if at any point the opponent defects  grudger will defect fot all the game") 


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

lim=len(players)+1

data=pl.read_csv("summary.csv").with_columns((pl.col("Rank") +int(1)).alias("Rank"))#aggiungo come colonna score totale e forse anche match length ecc
st.write("DATAFRAME")    
st.dataframe(data)
st.write("datafram scritto con summary")
st.dataframe(summary)


chart=(
    alt.Chart(data)
    .mark_circle()
    .encode(alt.X("Wins"),alt.Y("Median_score"),alt.Color("Name"))
)
st.altair_chart(chart)
x_y=st.multiselect("choose what x and y axes will represent",data.columns,placeholder="choose 2 : ",max_selections=2)
st.write(x_y)
chartInt=(
    alt.Chart(data)
    .mark_point()
    .encode(alt.X(x_y[0]),alt.Y(x_y[1]),alt.Color("Name"))
)
st.altair_chart(chartInt)
col1,col2,col3=st.columns(3)
chart2=(
    alt.Chart(data)
    .mark_point()
    .encode(alt.X("Wins").scale(domain=[0,lim]),alt.Y("Cooperation_rating"),alt.Color("Name",legend=None)).properties(title="cooperation rate per wins")
)
with col1:
    st.altair_chart(chart2,use_container_width=True)

chart2_1=(
    alt.Chart(data)
    .mark_point()
    .encode(alt.X("Rank").scale(domain=[0,lim]),alt.Y("Cooperation_rating"),alt.Color("Name",legend=None)).properties(title="cooperation rate per rank"))
with col2:
    st.altair_chart(chart2_1,use_container_width=True)

container=st.container(border=True)
container.write("from the graphs above what can we conclude about winning the single match and cooperating rarely? does it payoff? does winning the single battle win u the war?or doesn't it? does being a jerk and not cooperating work ?") 
chart3=(
    alt.Chart(data)
    .mark_point()
    .encode(alt.X("Rank").scale(domain=[0,lim]),alt.Y("Wins").scale(domain=[0,lim]),alt.Color("Name")).properties(title="rank of player per wins")
)
with col3:
    st.altair_chart(chart3)

st.write("bozza perchè non ho la variabile di intresse score totale al posto di wins")
chart4=(
    alt.Chart(data)
    .mark_bar()
    .encode(alt.X("Wins"),alt.Y("Name"),alt.Color("Name"))
)
st.altair_chart(chart4)


#https://axelrod.readthedocs.io/en/stable/how-to/access_tournament_results.html#tournament-results
st.subheader("scores")
st.write(results.scores)#lungo n-1 ma sempre con 9 elementi dentro che non riesco a interpreatre
st.subheader("payoff_matrix")
st.write(results.payoff_matrix)#utilizzabile
st.subheader("wins")
st.write(results.wins)#lungo n-1 ma sempre con 9 elementi dentro che non riesco a interpreatre
st.subheader("normalised scores")    
st.write(results.normalised_scores)  #lungo n-1 ma sempre con 9 elementi dentro che non riesco a interpreatre                     
st.subheader("match length")    
st.write(results.match_lengths) #lungo n-1 e n-1 elementi per elemento




# domanda  come gestire grafici, implemeto wiki come? con tanti if?, aggiungere colonne oe scores al dataframe?con polars?,creare nuoa colonna rankings che parto da 1 e non da 0?, fare più grafici non interattivi?o solo uno ma interattivo on possibiliotà di cambiare asse x e y ?tengo grafici di axl?, come far funzionare Image?, for in match no funzionante,scores è sempre lungo 9 prchè?

#noin funziona radiobutton, aggiungere colonne (scores ) e capire cosa significano, faccio wiki a tendina con tutti o interattiva con tanti iof macchuinosi?
                          

