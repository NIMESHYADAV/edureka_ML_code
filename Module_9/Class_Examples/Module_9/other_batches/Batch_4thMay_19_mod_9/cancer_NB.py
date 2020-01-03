"""
Bayes Theorem

P(A|B) = P(B|A).P(A)
        ------------
            P(B)

Problem:
Approx 1% of women aged 40-50 have breast cancer.
A women with cancer has a 90% chance of a +ve test from a mammogram,
while a women without cancer has 10% chance of a false positive result,
What is the probability a women has breast cancer given that she just had
a positive test from mammogram?


Solution:

events:
    A: Cancer is there
    B: +ve mammogram test
P(Cancer) = 0.01
P(+ve|Cancer) = 0.90

P(Cancer | +ve) ????
use bayes theorem
P(Cancer | +ve) = P(+ve|cancer).P(Cancer)
                    ------------------
                        P(+ve)
                =  0.90 * 0.01
                -------------------
                 0.01*0.90 + 0.99*0.10
                 = 0.083 = > 8.3 %



"""