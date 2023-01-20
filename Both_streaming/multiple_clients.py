"""
Run Multiple clients in one go.

"""

import os

number_of_clients = int(input("Please, enter how many client you want to run: "))
for client in range(0, number_of_clients):
    os.system("start py client.py")  # this will pop up python cmd and client will run.
    # os.system("start pythonw.exe client.py") # we can run python scripts in backgound.
