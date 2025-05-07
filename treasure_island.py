print('''                  _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-''')
print("welcome to treasure Island")
print("Your mission is to find the treasure")
choice1=input('you\'re at a crossroad, where do you want to go?Type"left"or"right".').lower()
if choice1=="right":
    print("you fell into the hole game over")
if choice1=="left":
    choice2=input('you\'ve come to a lake, there is island in the middle of the lake. type "wait "to wait for the boat. type "swim "to swim across ')
    if choice2=="wait":
      choice3=  input("you arrive at the island unharmed. there are three color of door.which color you want to choose? red yellow blue ").lower()
      if choice3=="red":
          print("game over")
      elif choice3=="yellow":
          print("you got the treasure")
      else:
          print("game over")

    else:
        print("game over ")




