import polars as pl
import streamlit as st
import axelrod as axl
from icecream import ic
import csv
import pandas as pd
from PIL import Image

st.set_page_config(page_title="Match",page_icon="⚔️")
st.sidebar.success("select a page above")

st.title("⚔️MATCH⚔️ ")
with st.popover("Open popover"):
    name = st.text_input("How would u like to be called?")

st.write("Ready to create a head to head match ", name,"?")

#inizializzazione parametri
st.sidebar.header("Please filter here: ")

st.write("i am presenting u here 2 prisoners Dwight and Nikita, who committed many crimes togheter in their career, but now that they got busted it's prisoner-1(Dwight) word against prisoner-2(Nikita)'s. They have 2 choices to snitch or to admit, if they both admit they both get 1 year of judgment, if they both snitch they get 3 year of judgment each, if one snithes and the other doesn't the one who snitched gets 0 years and the other gets 5.    ")
#img=Image.open("C:\Users\Luca Biasetto\OneDrive\Desktop\3zo anno\Sistemi 2\progetto\pygame_graphics\dwight.png")
#st.image("img")
#st.image("img1")



players2=st.sidebar.multiselect("choose what strategies will prisoner number 1 and priusoner number 2 will respectively perform",axl.axelrod_first_strategies,placeholder="choose 2 : ",max_selections=2,format_func=lambda x: str(x).strip("<'>").split('.')[-1])#trovare lista di strategie che mi interessa
players2=[d()for d in players2]
noise=st.sidebar.slider("choose the noise of the environment(likelihood of every choice to be changed by randomness) : ", min_value=0.0,max_value=1.0)
prob_end=st.sidebar.slider("choose the likelihood of the math ending every turn : ", min_value=0.0,max_value=1.0)
turns=st.sidebar.slider("choose how many crimes did they commit(number of turns): ", min_value=0,max_value=1000)



#---------------Match--------------------
#https://github.com/Axelrod-Python/Axelrod/blob/dev/axelrod/strategies/axelrod_first.py

match=axl.Match(players=players2,turns=turns,noise=noise)

results2=match.play()

st.subheader("results")
st.write(results2)
st.write(type(results2))
anniD=0
anniN=0
for el in results2:
    if (el[0]=="C" and el[1]=="C"):
        anniD+=1
        anniN+=1
    elif(el[0]=="D" and el[1]=="D"):
         anniD+=3
         anniN+=3
    elif(el[0]=="C" and el[1]=="D"):
        anniD+=5
        anniN+=0
    elif(el[0]=="D" and el[1]=="C"):
        anniD+=0
        anniN+=5
st.write("gli anni di galera sono :",anniD,anniN)
    





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

'''
import pygame
import numpy as np
from PIL import Image
import streamlit as st

# Inizializza Pygame
pygame.init()
screen_width, screen_height = 400, 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame in Streamlit")

# Colori e clock
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
clock = pygame.time.Clock()

# Disegna sullo schermo di Pygame
def draw_pygame_frame():
    screen.fill(black)
    pygame.draw.circle(screen, red, (200, 150), 50)  # Disegna un cerchio
    pygame.display.update()

# Cattura lo schermo come immagine
def capture_frame():
    frame = pygame.surfarray.array3d(screen)  # Ottieni i dati RGB dallo schermo
    frame = np.rot90(frame, 3)  # Ruota per adattare l'orientamento
    frame = np.flip(frame, axis=1)  # Capovolgi orizzontalmente
    return Image.fromarray(frame)  # Converte in immagine PIL
2. Integra Pygame in Streamlit
Mostra i frame catturati in tempo reale all'interno dell'applicazione Streamlit.

python
Copia codice
st.title("Esecuzione di Pygame in Streamlit")

# Placeholder per lo schermo
placeholder = st.empty()

# Loop principale per l'aggiornamento
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Disegna il frame di Pygame
    draw_pygame_frame()
    
    # Cattura il frame e mostralo su Streamlit
    frame_image = capture_frame()
    placeholder.image(frame_image, caption="Pygame Screen", use_column_width=True)
    
    clock.tick(30)  # Limita a 30 FPS

# Chiudi Pygame
pygame.quit()
Come funziona?
Pygame genera il contenuto grafico sul proprio schermo.
Ogni frame viene catturato usando pygame.surfarray.array3d.
Il frame viene convertito in un'immagine usando Pillow (Image.fromarray).
Streamlit aggiorna il contenuto nel browser con st.image.
Limitazioni
Prestazioni: Pygame è progettato per applicazioni desktop, quindi il rendering continuo potrebbe rallentare se non ottimizzato.
Schermo interattivo: Streamlit non supporta l'interattività completa di Pygame (come eventi di mouse o tastiera). Tuttavia, puoi utilizzare Streamlit per inviare eventi personalizzati a Pygame.
Estensione: Aggiungi interazione
Puoi integrare controlli Streamlit (come pulsanti) per simulare input utente in Pygame.

python
Copia codice
if st.button("Muovi il cerchio"):
    # Simula un'interazione (esempio: cambia posizione del cerchio)
    pygame.draw.circle(screen, red, (250, 150), 50)
Con questa configurazione, puoi mostrare schermate generate da Pygame direttamente su Streamlit in tempo reale!
'''
#altra alternativa Manim community