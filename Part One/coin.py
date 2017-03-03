moves = 5 #Records the moves
counter = 0 #Records the counter
coins_string = ('H H H H H T T T T T')
coin_array = coins_string.split(" ")
while (moves > 0 and moves <=5): #Amount of the moves the player can do 
  print('moves = ', moves) #Shows the amount of moves the player has
  print('counter = ', counter) #Shows the counter for the player
  print(''.join(coin_array))
  coin_input = int (input("Enter coin number 1-10")) #User inputs which of the two coins they want
  val_Input = False #Validates if the players chooses the coins within the range, not out of bounds
  while val_Input == False:
      if coin_input < 1 or coin_input > 9:
       print("Out of bounds, Enter coin number 1-10.")
       coin_input = int(input())
      else:
        val_Input = True #Lets the user continue
  print("You entered: ", coin_input, coin_array[coin_input-1],coin_array[coin_input])
  print("") #Displays what the player chose
  print(''.join(coin_array))
  coin_position = int (input("Where would like to place these coins? Enter position 1-10"))
  val_Position = False #Validates the user position to be in range
  while val_Position == False:
      if coin_position < 1 or coin_position > 10:
       print("Out of bounds, Enter position 1-10")
       coin_position = int(input())
      else:
        val_Position = True #Lets the user continue
  if ('-') not in coin_array: #If the ('-') is not in the array
    if coin_position == 1:
      if coin_input == 1:
         moves = moves - 1
         counter = counter + 1
         print(''.join(coin_array))
      elif coin_input!=1:
        temp1 = coin_array[coin_input-1] #Temporary storage for first coin
        temp2 = coin_array[coin_input] #Temporary storage for second coin
        coin_array[coin_input-1] = ('-')
        coin_array[coin_input] = ('-')
        coin_array.append(temp1) 
        coin_array.append(temp2)
        moves = moves - 1 #Decrements player moves
        counter = counter + 1 #Increments counter
  else:
    if coin_array[coin_position -1] and coin_array[coin_position] == ('-'):
      swap1 = coin_array[coin_position]
      swap2 = coin_array[coin_position -1]
      coin_array[coin_position-1] = swap1
      coin_array[coin_position] = swap2
      coin_array[coin_input - 1] = ('-')
      coin_array[coin_input] = ('-')
      if coin_input == 1:
        coin_array.remove('-')
        coin_array.remove('-')
      if coin_input == 9:
        coin_array.remove('-')
        coin_array.remove('-')
      moves = moves - 1 #Decrements player moves
      counter = counter + 1  #Increments counter
      print(''.join(coin_array))
print("Game over")
