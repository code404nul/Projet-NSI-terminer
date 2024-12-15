
from turtle import textinput, Screen
from fusion import game
import variable

def main():

    screen = Screen()
    screen.title("Demande d'Entrée")
    screen.bgcolor("black")

    nom = textinput("Entrée de l'utilisateur", "Niveau de difficulter 0 facile / 1 mort qui tue")

    variable.difficulty = bool(int(nom))
    print(variable.difficulty)

    game()
    
    screen.mainloop()

if __name__ == "__main__":
    main()
