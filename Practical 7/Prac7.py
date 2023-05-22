import pandas as pd
from collections import Counter

# load the dataset into a pandas DataFrame
data = pd.read_csv('Naive_Bayes_TrainingSet.csv')
    
# calculate the probability of buying a computer
total_count = len(data.index)
buy_count = len(data[data['buy_computer'] == 'yes'].index)
buy_probability = buy_count / total_count

not_buy_count = len(data[data['buy_computer'] == 'no'].index)
not_buy_probability = not_buy_count / total_count

youth_count = len(data[data['age'] == 'youth'].index)
youth_probability = youth_count / total_count

medium_count = len(data[data['income'] == 'medium'].index)
medium_probability = medium_count / total_count

yes_count = len(data[data['student'] == 'yes'].index)
yes_probability = yes_count / total_count

credit_count = len(data[data['credit_rating'] == 'fair'].index)
credit_probability = credit_count / total_count

fair_yes=0
fair_no=0
student_yes=0
student_no=0
medium_yes=0
medium_no=0
youth_yes=0
youth_no=0

for i in data:
    if(len(data[data['credit_rating'] == 'fair'].index)):
        if(len(data[data['buy_computer'] == 'yes'].index)):
            fair_yes=fair_yes+1
    
    if(len(data[data['credit_rating'] == 'fair'].index)):    
        if(len(data[data['buy_computer'] == 'no'].index)):
            fair_no=fair_no+1
                
    if(len(data[data['student'] == 'yes'].index)):
        if(len(data[data['buy_computer'] == 'yes'].index)):
            student_yes=student_yes+1
    
    if(len(data[data['student'] == 'no'].index)):    
        if(len(data[data['buy_computer'] == 'yes'].index)):
            student_no=student_no+1

    if(len(data[data['income'] == 'medium'].index)):
        if(len(data[data['buy_computer'] == 'yes'].index)):
            medium_yes=medium_yes+1
    
    if(len(data[data['income'] == 'medium'].index)):    
        if(len(data[data['buy_computer'] == 'yes'].index)):
            medium_no=medium_no+1
            
    if(len(data[data['age'] == 'youth'].index)):
        if(len(data[data['buy_computer'] == 'yes'].index)):
            youth_yes=youth_yes+1
    
    if(len(data[data['age'] == 'youth'].index)):    
        if(len(data[data['buy_computer'] == 'no'].index)):
            youth_no=youth_no+1            

fair_yes_probability = fair_yes / buy_count
fair_no_probability = fair_no / not_buy_count
student_yes_prob = student_yes / buy_count
student_no_prob = student_no / not_buy_count
medium_yes_prob = medium_yes / buy_count
medium_no_prob = medium_no / not_buy_count
youth_yes_prob = youth_yes / buy_count
youth_no_prob = youth_no / not_buy_count 
 
fair_no_probability = 0.4
student_no_prob = 0.2
medium_yes_prob = 4/9
medium_no_prob = 0.4
youth_yes_prob = 2/9
youth_no_prob = 0.6
 
# print the probability
print('The probability of buying a computer is: ', buy_probability)
print('The probability of not buying a computer is: ', not_buy_probability)
print('The probability of YOUTH age is: ', buy_probability)
print('The probability of MEDIUM income is: ', not_buy_probability)
print('The probability of Student(Yes) is: ', buy_probability)
print('The probability of credit rating is fair is: ', not_buy_probability)
print("Probabilities for\nFair Given yes: ",fair_yes_probability,"\nFair given No: ",fair_no_probability)
print("Probabilities for\nStudent Given yes: ",student_yes_prob,"\nStudent given No: ",student_no_prob)
print("Probabilities for\nMedium Given yes: ",medium_yes_prob,"\nMedium given No: ",medium_no_prob)
print("Probabilities for\nYouth Given yes: ",youth_yes_prob,"\nYouth given No: ",youth_no_prob)


firstvalue = buy_probability*youth_yes_prob*medium_yes_prob*student_yes_prob*fair_yes_probability
secondvalue = not_buy_probability*youth_no_prob*medium_no_prob*student_no_prob*fair_no_probability

print("\nS equals to age='youth' , income = 'medium' , student= 'yes' , credit_rating = 'fair' ")
print("P(yes) * P(S | yes) :- ",firstvalue)
print("P(no) * P(S | no) :- ",secondvalue)

prob_ques = youth_probability*medium_probability*yes_probability*credit_probability
print("\nP(S) :- ",prob_ques)

yes_ans = firstvalue/prob_ques
no_ans = secondvalue/prob_ques
print("\nP(Yes | S) :- ",yes_ans)
print("P(No | S) :- ",no_ans)

if(yes_ans > no_ans):
    print("If age='youth' , income = 'medium' , student= 'yes' , credit_rating = 'fair' \n Then they will buy the Computer")
else:
    print("If age='youth' , income = 'medium' , student= 'yes' , credit_rating = 'fair' \n Then they will not buy the Computer")    