import random
word_list = ["manzana", "celular", "colchon",
             "control", "piano", "plato",
             "platano", "pera", "television",
             "mesa", "silla", "camiseta",
             "libro", "cuchara", "zapato"
             ]

selected_word = random.choice(word_list)

def ahorcado():
  palabra = ["_"] * len(selected_word)
  i = 0
  for i in range(6) and "_" in palabra:
    user_letter = str(input(f"Ingresa una letra: {" ".join(palabra)} (Presiona 1 para usar un comodín de letra): "))
    for o in range(int(len(selected_word))):
      if selected_word[o] == user_letter:
        palabra[o] = user_letter
      else:
        i += 1
  else:
    if len(palabra) == selected_word:
      return "¡¡Felicidades. Has completado la palabra!!"
    else:
      return "Haz agotado el numero de intentos. Intenta de nuevo."
        
print("""Bienvenido al juego del ahorcado. 
      Intenta adivinar la palabra secreta, tienes 5 oportunidades...
      
        ||==============|
        ||              |
        ||              |
        ||            __|__
        ||           ( o o ) 
        ||            ( - )
        ||              |
        ||            / | \\
        ||           /  |  \\
        ||             / \\  
       /||\\           /   \\
           """)

print(ahorcado())