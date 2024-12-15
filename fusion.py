from turtle import Turtle, Screen
import time
from random import randint # *NOTICE*
import variable

t = Turtle()

r = 250
pen_size = 130
padding_du_la_rache = 10

COLOR = ("red", "blue", "yellow", "green")
SYMBOLS = ("R", "B", "J", "V")
COORDONNEE = ([5, 5], [5, -5], [-5, -5], [-5, 5])

turtles = [Turtle() for i in range(4)]
text_nouvelle_couleur = Turtle()
try_again_text = Turtle()
text_score = Turtle()

text_nouvelle_couleur.goto(0, -250)
text_nouvelle_couleur.color("white")

screen = Screen()
screen.bgcolor("black")
screen.tracer(0)

def define_new_color():
    return ["rouge", "bleu", "jaune", "vert"][randint(0, 3)]


def read_score():
    return open("score.txt", "r").read()


def save_score(score):

    if int(read_score()) < score:
        with open("score.txt", "w") as fichier:
            fichier.write(str(score))
        fichier.close()
        return True
    
    return False

def init_txt():

    fichier = open("score.txt", "a")
    fichier.write("")

    if read_score() == "":
        fichier.write("0")

    fichier.close()

def drawSquares():
    for i in range(4):
        turtles[i].speed(10)
        turtles[i].penup()
        turtles[i].goto(COORDONNEE[i][0] * 20, COORDONNEE[i][1] * 20)
        turtles[i].fillcolor(COLOR[i])
        turtles[i].shapesize(10, 10, 1)
        turtles[i].shape("square")
        turtles[i].stamp()  # Dessine le carré

    screen.update()

def draw_cercle():
    t.speed(0)
    t.color("black")
    t.pendown()
    t.pensize(40)
    t.circle(1)
    t.penup()
    t.sety(-r/2 - pen_size + padding_du_la_rache)
    t.pendown()
    t.pensize(pen_size)

    for i in range(6):
        t.circle(r)

    


def highlight(e, ms):
    """
    La fonction va changer la couleur d'une touche pour signaler que la touche est jouée
    PARAMETRES :
        e -> est la touche à signaler
        ms -> le temps que doit durer la signalisation
    """

    turtles[e].fillcolor("grey")
    screen.update()
    time.sleep(ms / 1000)
    turtles[e].fillcolor(COLOR[e])

    screen.update()
    draw_cercle()
    draw_text_color()

def draw_text_color():

    for i in range(4):
        
        symbol_turtle = Turtle()
        symbol_turtle.hideturtle()
        symbol_turtle.penup()
        symbol_turtle.goto(COORDONNEE[i][0] * 20, COORDONNEE[i][1] * 20 - 10)
        symbol_turtle.color("white")
        symbol_turtle.write(SYMBOLS[i], align="center", font=("Arial", 18, "bold"))


def get_key(x, y):
    """
    La fonction retourne la touche qui correspond aux coordonnées en paramètre
    Retourne -1 si les coordonnées sont en dehors du jeu
    """
    if x > 200 or y > 200 or y < -200 or x < -200:
        return -1
    else:
        if x > 0 and y > 0:
            return 0
        elif x > 0 and y < 0:
            return 1
        elif x < 0 and y < 0:
            return 2
        else:
            return 3
def show_new_color(difficulty):

    text_nouvelle_couleur.showturtle()
    print(f"difficulter {variable.difficulty}")
    if not difficulty:
        text_nouvelle_couleur.write(
            "la nouvelle couleur est : " + str(variable.color_sequence[len(variable.color_sequence) - 1]),
            align="center",
            font=("Arial", 12, "normal")
        )
    else: 
        text_nouvelle_couleur.write(
            "la nouvelle couleur est : " + 
            str(variable.color_sequence[len(variable.color_sequence) - 2]) + 
            "\net puis : " + 
            str(variable.color_sequence[len(variable.color_sequence) - 1]),
            align="center",
            font=("Arial", 12, "normal")
        )
    

def append_du_ghetto(liste):


    def add(liste, multiplicateur):
        liste += [None] * multiplicateur
        for i in range(multiplicateur):
            liste[len(liste) - multiplicateur] = define_new_color()
    
    
    if variable.difficulty:
        print(f"difficulter le if est bon {variable.difficulty}")
        for i in range(2): add(liste, 1)
    else:
        add(liste, 1)
    return liste

def recommencer_le_train_train():
    """
    Réinitialise tout
    """
    variable.can_click = False

    screen.bgcolor("white")
    

    try_again_text.st()
    try_again_text.write(
        "Tu t'es vautré lamentablement comme une loutre bourrée \n"
        "à la bière tombant sur une épluchure de concombre.\n"
        "On dit qu'on oublie tout ?",
        align="center",
        font=("Arial", 12, "normal")
    )

    def cacher_texte_et_activer_clic():
        try_again_text.clear()
        try_again_text.ht()

    def affichier_le_nouveau_score():
        text_score.showturtle()

        variable.score = len(variable.color_sequence) * 12
        if variable.difficulty: variable.score *= 2
        
        text_score.clear()
        text_nouvelle_couleur.clear()

        if save_score(variable.score):
            text_nouvelle_couleur.write(
                "Tu as battu ton score !!!" + 
                "\n et ton nouveau score est : " + str(variable.score),
                align="center",
                font=("Arial", 12, "normal")
            )
        else:
            text_nouvelle_couleur.write(
                "Ton précédent score était : " + read_score() +
                "\n et ton nouveau score est : " + str(variable.score),
                align="center",
                font=("Arial", 12, "normal")
            )

        variable.can_click = True
        variable.color_sequence = [define_new_color()]
        variable.current_step = 0

    def reinitialiser_apres_score():
        
        text_score.clear()
        text_nouvelle_couleur.clear()

        show_new_color(False)
        screen.bgcolor("black")
        t.color("black")

    def supprimer_nouvelle_couleur():
        text_nouvelle_couleur.hideturtle()

    screen.ontimer(cacher_texte_et_activer_clic, 1000)
    screen.ontimer(affichier_le_nouveau_score, 2000)
    screen.ontimer(reinitialiser_apres_score, 4000)
    screen.ontimer(supprimer_nouvelle_couleur, 5000)



def action_on_click(x, y):
    """
    Fonction appelée à chaque clic de l'utilisateur.
    :param x: Position x du clic.
    :param y: Position y du clic.
    """
    
    if not variable.can_click:
        return

    key = get_key(x, y)
    if key == -1:
        print("M'en fous de ton clic")
        return

    highlight(key, 110)
    couleurs = ["rouge", "bleu", "jaune", "vert"]
    selected_color = couleurs[key]
    print("t'as choisi ça", selected_color, "bon choix !")

    expected_color = variable.color_sequence[variable.current_step]
    if selected_color == expected_color:
        print("YOUPI !!!")
        variable.current_step += 1

        if variable.current_step == len(variable.color_sequence):
            
            variable.color_sequence = append_du_ghetto(variable.color_sequence)
            variable.current_step = 0
            show_new_color(variable.difficulty)
            text_nouvelle_couleur.hideturtle()
    else:

        print("Le jeu est fini, tu t'es trompé... dommage...")
        recommencer_le_train_train()

    print("Étape actuelle :", variable.current_step, "/ Séquence :", variable.color_sequence)

def game():
    print(f"difficulter {variable.difficulty}")
    
    variable.color_sequence = [define_new_color()]

    
    print("Couleur initiale :", variable.color_sequence)
    text_nouvelle_couleur.showturtle()
    
    init_txt()

    drawSquares()
    draw_cercle()

    show_new_color(False)
    draw_text_color()
    screen.onclick(action_on_click)

    screen.mainloop()