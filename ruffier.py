''' Module for calculating the results of Ruffier tests.


The sum of the three tries at pulse readings (before strain, right after strain, and after a short break)
ideally, there should be no more than 200 beats per minute.
We propose that the children measure their pulse for 15 seconds,
and find the result of beats per minute by multiplying by 4:
   S = 4 * (P1 + P2 + P3)
The further the result is from the ideal 200 beats, the worse it is.
Traditionally, tables are given by values divided by 10.


Ruffier index  
   IR = (S - 200) / 10
is evaluated corresponding to age according to the table:
       7–8             9–10                11–12               13–14               15+ (only for adolescents!)
perfect    6.4 and below   4.9 and below       3.4 and below         1.9 and below               0.4 and below
good    6.5–11.9     5–10.4          3.5–8.9           2–7.4                   0.5–5.9
satisfactory  12–16.9      10.5–15.4       9–13.9            7.5–12.4                6–10.9
weak  17–20.9      15.5–19.4       14–17.9           12.5–16.4               11–14.9
unsatisfactory   21 and above     19.5 and above      18 and above          16.5 and above             15 and above


the result “unsatisfactory” is 4 from the result “weak” for all ages,
“weak” is separated from “satisfactory” by 5, and “good” from “satisfactory” by 5.5


so we will write a function ruffier_result(r_index, level) which will produce
the calculated Ruffier index and level “unsatisfactory” for the tested age, and produce a result


'''
# here the lines which produce the result are given
txt_index = "Your Ruffier index: "
txt_workheart = "Heart efficiency: "
txt_nodata = '''
there is no data for that age'''
txt_res = []
txt_res.append('''low.
Go see your doctor ASAP!''')
txt_res.append('''satisfactory.
Go see your doctor!''')
txt_res.append('''average.
It might be worth additional tests at the doctor.''')
txt_res.append('''
higher than average''')
txt_res.append('''
high''')


def ruffier_index(P1, P2, P3):
    ''' it returns the index value according to the three pulse calculations for comparison with the table'''
    return (4 * (P1+P2+P3) - 200) / 10


def neud_level(age):
    ''' the options with an age of less than 7 and with adults have to be processed separately,
    here we select the level “unsatisfactory” only within the table:
    for the age of 7, “unsatisfactory” is an index of 21, then onwards every 2 years it decreases by 1.5 until the level of 15 at age 15–16 '''
    norm_age = (min(age, 15) - 7) // 2  # every two years the from age seven turns into one unit, all the way to age 15
    result = 21 - norm_age * 1.5 # every two years multiply the difference by 1.5, that's how the levels are arranged in the table
    return result
  
def ruffier_result(r_index, level):
    ''' the function obtains a Ruffier index and interprets it,
    we return the readiness level: a number from 0 to 4
    (the higher the readiness level, the better).  '''
    if r_index >= level:
        return 0
    level = level - 4 # this will not run if we already returned the answer “unsatisfactory”
    if r_index >= level:
        return 1
    level = level - 5 # analogously, we end up here if the level is, at minimum, “satisfactory”
    if r_index >= level:
        return 2
    level = level - 5.5 # next level
    if r_index >= level:
        return 3
    return 4 # we end up here if the index is less than all the intermediate levels, that is, the tested circle.


def test(P1, P2, P3, age):
    ''' this function can be used from outside the module for calculating the Ruffier index.
    We return the ready texts that just need to be written in the necessary place
    We use the constants used at the beginning of this module for texts. '''
    if age < 7:
        return (txt_index + "0", txt_nodata) # this is a mystery beyond this test
    else:
        ruff_index = ruffier_index(P1, P2, P3) # calculation
        result = txt_res[ruffier_result(ruff_index, neud_level(age))] # the interpretation and conversion of the numeric preparation level into text data
        res = txt_index + str(ruff_index) + '\n' + txt_workheart + result
        return res