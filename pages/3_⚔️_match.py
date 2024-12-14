import polars as pl
import streamlit as st
import axelrod as axl
from icecream import ic
import csv
import pygame
from io import BytesIO
from PIL import Image


st.set_page_config(page_title="Match",page_icon="⚔️")
st.sidebar.success("select a page above")

st.title("⚔️MATCH⚔️ ")
with st.popover("Open popover"):
    name = st.text_input("How would u like to be called?")

st.write("Ready to create a head to head match ", name,"?")

#inizializzazione parametri
st.sidebar.header("Please filter here: ")


players2=st.sidebar.multiselect("choose what strategies will prisoner number 1 and priusoner number 2 will respectively perform",axl.axelrod_first_strategies,placeholder="choose 2 : ",max_selections=2,format_func=lambda x: str(x).strip("<'>").split('.')[-1])#trovare lista di strategie che mi interessa
players2=[d()for d in players2]
noise=st.sidebar.slider("choose the noise of the environment(likelihood of every choice to be changed by randomness) : ", min_value=0.0,max_value=1.0)
#prob_end=st.sidebar.slider("choose the likelihood of the match ending every turn : ", min_value=0.0,max_value=1.0)
turns=st.sidebar.slider("choose how many crimes did they commit(number of turns): ", min_value=0,max_value=1000)



#---------------Match--------------------
#https://github.com/Axelrod-Python/Axelrod/blob/dev/axelrod/strategies/axelrod_first.py

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


#match

st.title("PRISONERS CLASH")
container = st.container(border=True)


container.write("I am presenting u here 2 prisoners Dwight and Nikita, who committed many crimes togheter in their career, but now that they got busted it's prisoner-1(Dwight) word against prisoner-2(Nikita)'s. They have 2 choices to snitch or to admit, if they both admit they both get 1 year of judgment, if they both snitch they get 3 year of judgment each, if one snithes and the other doesn't the one who snitched gets 0 years and the other gets 5.    ")

col11,col22=st.columns(2)
#img=Image.open(r"C:\Users\Luca Biasetto\OneDrive\Desktop\3zo anno\Sistemi 2\progetto\pygame_graphics\dwight.png")#pathlib.Path()
with col11 :
    st.image(r"C:\\Users\\Luca Biasetto\\OneDrive\Desktop\3zo anno\Sistemi 2\\progetto\\pygame_graphics\\americano.png",caption="Dwight, Prisoner 1",use_container_width=True)

with col22 :
    st.image(r"C:\\Users\\Luca Biasetto\\OneDrive\Desktop\3zo anno\Sistemi 2\\progetto\\pygame_graphics\\russovero.png",caption="NIkita, prisoner 2",use_container_width=True)

match=axl.Match(players=players2,turns=turns,noise=noise)

results2=match.play()


st.subheader("results")
st.write(results2)
#st.write(type(results2))

anniD=0
anniN=0
for el in results2:
    if repr(el[0])=="C" and repr(el[1])=="C":
        anniD=anniD+1
        anniN=anniN+1
    elif(repr(el[0])=="D" and repr(el[1])=="D"):
        anniD+=3
        anniN+=3
    elif(repr(el[0])=="C" and repr(el[1])=="D"):
        anniD+=5
        anniN+=0
    elif(repr(el[0])=="D" and repr(el[1])=="C"):
        anniD+=0
        anniN+=5
st.write("gli anni di galera sono:",anniD,anniN)


st.title("Controllo Pygame con Streamlit")
st.write("Premi il pulsante per avanzare di un turno")

# Inizializza Pygame
pygame.init()

# Dimensioni dello schermo

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Prisoners Clash")

p1= pygame.image.load('pygame_graphics\\dwight1.png').convert_alpha() 
p1=pygame.transform.smoothscale(p1,(370,420))
p2= pygame.image.load('pygame_graphics\\nikita1.png').convert_alpha() 
p2=pygame.transform.smoothscale(p2,(370,420))#ridimensiono immagine
game_bg = pygame.image.load('pygame_graphics\\tribunale.png').convert_alpha()  # Immagine per il gioco
game_over_bg = pygame.image.load("pygame_graphics\\game_end.png").convert_alpha()  # Immagine per il Game Over

# Ridimensiona gli sfondi per adattarli allo schermo
game_bg = pygame.transform.scale(game_bg, (screen_width, screen_height))
game_over_bg = pygame.transform.scale(game_over_bg, (screen_width, screen_height))#al momento inutili 

# Colori
white = (255, 255, 255)
black = (0, 0, 0)

# Font
font = pygame.font.Font(None, 50)
font1 = pygame.font.Font(None, 40)
font2 = pygame.font.Font(None, 40)#inutili

# Stato del gioco
tick_count = st.session_state.get("tick_count", 0)  # Mantieni il conteggio dei tick tra i reloads
game_state = "running"  # Possibili stati: "running", "game_over"



# Controllo del tick
a,b,c=st.columns(3)
with a:
    if st.button("Go to the recap"):
        screen.blit(game_over_bg, (0, 0))
        #capisco come fare in modo che se esegue questo salta la parte sotto di game, ma questo appare anche alla fine dei turni
    
with b:
    if st.button("Go to next turn"):
        tick_count += 1
        st.session_state["tick_count"] = tick_count  # Salva lo stato del tick
    st.write(tick_count)
with c:
    if st.button("Go to previous turn"):
        ba#non so se lo implementerò

# Disegna il frame di Pygame


screen.blit(game_bg, (0, 0))

annid=0
annin=0
annitot1=0
annitot2=0
#non entra nell'if
#if tick_count==0:
    #annitot1=0
   #annitot2=0


if repr(results2[tick_count][0])=="C" and repr(results2[tick_count][1])=="C":
    annid=annid+1
    annin=annin+1
elif repr(results2[tick_count][0])=="D" and repr(results2[tick_count][1])=="D":
    annid+=3
    annin+=3
elif repr(results2[tick_count][0])=="C" and repr(results2[tick_count][1])=="D":
    annid+=5
    annin+=0
elif repr(results2[tick_count][0])=="D" and repr(results2[tick_count][1])=="C":
    annid+=0
    annin+=5

annitot1+=annid
annitot2+=annin


text = font.render(f"Turn {tick_count}", True, black)
text_rect = text.get_rect(center=(70,50))
screen.blit(text, text_rect)

text0 = font.render(f"Judgment {annitot1,annitot2}", True, black)
text0_rect = text.get_rect(center=(340,30))
screen.blit(text0, text0_rect)

text1 = font1.render(f"+ {annid}", True, black)
text_rect1 = text1.get_rect(center=(180,220))
screen.blit(text1, text_rect1)

text2 = font2.render(f"+ {annin}", True, black)
text_rect2 = text2.get_rect(center=(600,220))
screen.blit(text2, text_rect2)

#p1 e p2
p1_rect=p1.get_rect(center=(180,430))
screen.blit(p1,p1_rect)

p2_rect=p2.get_rect(center=(600,420))
screen.blit(p2,p2_rect)


# Converti la superficie Pygame in un'immagine visualizzabile in Streamlit
buffer = BytesIO()
pygame_image = pygame.image.tostring(screen, "RGBA")
image = Image.frombytes("RGBA", (screen_width, screen_height), pygame_image)
image.save(buffer, format="PNG")
st.image(buffer.getvalue(), caption="Schermata Pygame")

# Esci da Pygame (opzionale, non necessario durante l'esecuzione continua)
pygame.quit()


#sincronizzo i tick e il ciclo for, trovo modo per non eseguire sempre match perchè ogno volta che clicco button mi cambiano i risultati se c'è rumore, non so come usare tick_count e quindi non posso creare variabile anni parziali del turno e devo creare 2 variabiuli diverse annin e annid anniN e anniD e nemmeno usare la condizione if tick_count == turns+1 o turns per decretare la fine del match,capisco come fare in modo che se esegue st button salta la parte sotto di game, ma questo appare anche alla fine dei turni, e aggiungo go to previus turn?

        




l,m,m,m,r= st.columns(5)
with r:
    st.write("𝓑𝓲𝓪𝓼𝓮𝓽𝓽𝓸 𝓛𝓾𝓬𝓪 ,  𝓪.𝓪.𝟐𝟎𝟐𝟒/𝟐𝟓, 𝟐𝟎𝟔𝟕𝟏𝟖𝟔")