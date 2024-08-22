kok = 0
kok_current_round_score = 0
sam = 0
sam_current_round_score = 0
brian = 0
brian_current_round_score = 0
ang = 0
ang_current_round_score = 0

response ='y'

while response == "y" or response == 'Y':
    kok_current_round_score = int(input("\nEnter Kok's score: "))
    sam_current_round_score = int(input("Enter Sam's score: "))
    brian_current_round_score = int(input("Enter Brian's score: "))
    ang_current_round_score = int(input("Enter Ang's score: "))

    kok += kok_current_round_score
    sam += sam_current_round_score
    brian += brian_current_round_score
    ang += ang_current_round_score

    response = input("Do you want to continue? (y/n): ")

print("""
       FINAL SCORE:
       Kok's total score: {}
       Sam's total score: {}
       Brian's total score: {}
       Ang's total score: {}""".format(kok,sam,brian,ang))
