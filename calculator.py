def days_in_week (amount_daily_cours_study, max):
    ''''
    this function calculate if the amount of daily study is exceed the max heur indicated by the user
     then it will ask for more time.
    ''''
    if amount_daily_cours_study > max and amount_daily_cours_study < 12:
        pritn ("You need to study harder for that goal!")
    elif amount_daily_cours_study > 12:
        print ("This is a mission imposibele")

        
def calculator(period, weekend_n, pages, hardship_ratio):
    '''
    this function calculate each days study for each course
    period= the period of the total semester in weeks or any period 
        that student wants to study.
    weekend_n= number of off days in each weeks
    pages = number of each pages for each courses
    hardship_ratio = how many pages in one heur.
    '''
    total_days = period * (7 - weekend_n)
    total_hours= total_days * 2
    amount_daily_cours_study = (pages/total_days)/ hardship_ratio
    return daily_cours_study
a = calculator(5, 2, 100, 3)
print (a)