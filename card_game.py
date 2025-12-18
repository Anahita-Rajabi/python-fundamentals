print("Enter cards as <rank><suit> (e.g., AH or 10S).")
card1=input("Card 1:")


rank1 = card1[:-1]
suit1 = card1[-1]

rank=False
suit=False
if rank1=="A" or rank1=="K" or rank1=="Q" or rank1=="J" or rank1=="10" or rank1=="9" or rank1=="8" or rank1=="7" or rank1=="6" or rank1=="5" or rank1=="4" or rank1=="3" or rank1=="2":
    rank=True
else:
    print("Invalid rank " + rank1 + ". Must be 2-10, J, Q, K, or A.")

if suit1 == "H" or suit1=="D" or suit1 =="S" or suit1 =="C":
    suit=True
else:
 print("Invalid suit " + suit1+ ".Must be H,D,C,or S.")
 exit()

if rank1 == "A":
    value1 = 11
elif rank1 == "K" or rank1 == "Q" or rank1 == "J":
    value1 = 0
elif rank1 == "10":
    value1 = 10
elif rank1 == "9":
    value1 = 9
elif rank1 == "8":
    value1 = 8
elif rank1 == "7":
    value1 = 7
elif rank1 == "6":
    value1 = 6
elif rank1 == "5":
    value1 = 5
elif rank1 == "4":
    value1 = 4
elif rank1 == "3":
    value1 = 3
else:
    value1 = 2




card2 =input("Card 2:")


rank2 = card2[:-1]
suit2 = card2[-1]

rank=False
suit=False
if rank2=="A" or rank2=="K" or rank2=="Q" or rank2=="J" or rank2=="10" or rank2=="9" or rank2=="8" or rank2=="7" or rank2=="6" or rank2=="5" or rank2=="4" or rank2=="3" or rank2=="2":
    rank=True
else:
    print("Invalid rank " + rank2 + ". Must be 2-10, J, Q, K, or A.")

if suit2== "H" or suit2=="D" or suit2 =="S" or suit2 =="C":
    suit=True
else:
 print("Invalid suit " + suit2 + ".Must be H,D,C,or S.")
 exit()

if rank2== "A":
    value2 = 11
elif rank2== "K" or rank2 == "Q" or rank2 == "J":
    value2 = 0
elif rank2== "10":
    value2 = 10
elif rank2== "9":
    value2 = 9
elif rank2== "8":
    value2 = 8
elif rank2== "7":
    value2= 7
elif rank2== "6":
    value2 = 6
elif rank2== "5":
    value2= 5
elif rank2== "4":
    value2 = 4
elif rank2== "3":
    value2= 3
else:
    value2= 2

Error=False
if card1== card2:
    Error=False
    print("There can't be two",card1,"in the same hand.You're playing with a fake deck!")
    exit()







card3=input("Card 3:")


rank3 = card3[:-1]
suit3 = card3[-1]

rank=False
suit=False
if rank3=="A" or rank3=="K" or rank3=="Q" or rank3=="J" or rank3=="10" or rank3=="9" or rank3=="8" or rank3=="7" or rank3=="6" or rank3=="5" or rank3=="4" or rank3=="3" or rank3=="2":
    rank=True
else:
    print("Invalid rank " + rank3 + ". Must be 2-10, J, Q, K, or A.")

if suit3 == "H" or suit3=="D" or suit3 =="S" or suit3 =="C":
    suit=True
else:
 print("Invalid suit " + suit3 + ".Must be H,D,C,or S.")
 exit()

if rank3== "A":
    value3 = 11
elif rank3== "K" or rank3 == "Q" or rank3 == "J":
    value3 = 0
elif rank3== "10":
    value3 = 10
elif rank3== "9":
    value3 = 9
elif rank3== "8":
    value3 = 8
elif rank3== "7":
    value3 = 7
elif rank3== "6":
    value3 = 6
elif rank3== "5":
    value3 = 5
elif rank3== "4":
    value3 = 4
elif rank3== "3":
    value3= 3
else:
    value3= 2
Error=False
if card1==card3:
    Error=False
    print("There can't be two",card1,"in the same hand. You're playing with a fake deck!")
    exit()
elif card2==card3:
    Error=False
    print("There can't be two", card2, "in the same hand. You're playing with a fake deck!")
    exit()



TOTAL_VALUE=value1+value2+value3
face=False
if rank1=="J" or rank1=="Q" or rank1=="K":
    face=True
elif rank2=="J" or rank2=="Q" or rank2=="K":
    face=True
elif rank3=="J" or rank3=="Q" or rank3=="K":
    face=True

if face == True:
    TOTAL=TOTAL_VALUE+10
    print("Point value of hand:",TOTAL,)



elif value1>value2 and value1>value3:
    largest=value1

elif value2>value3 and value2>value1:
    largest=value2
else:
    largest=value3
    print("Point value of hand:", largest)



