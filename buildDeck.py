# Author: DATADISCRETE LLC
# DATE: 27 JUNE 2021

import os

bg_arr = [i for i in os.listdir("./backgrounds") if not i.startswith("._") if not i.startswith(".")]
playerDeck_arr = [i for i in os.listdir("./playerdeck") if not i.startswith("._") if not i.startswith(".")]
branded_arr = [i for i in os.listdir("./branded_playerdeck") if not i.startswith("._") if not i.startswith(".")]

print(bg_arr)
print(playerDeck_arr)
print(branded_arr)




