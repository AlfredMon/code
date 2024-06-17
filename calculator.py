def calculator(period, weekend_n, pages, hardship_ratio):
    '''
    this function calculate each days study for each course
    period= the period of the total semester in weeks or any period 
        that student wants to study.
    weekend_n= number of off days in each weeks
    pages = number of each pages for each courses
    hardship_ratio = how many pages in one heur.
    '''
    total_days = period * (7 -weeken_n)
    daily_cours_study = total_days/pages * hardship_ratio
    return daily_cours_study
    