def get_demerit_points(driving_speed, speed_limit, holiday_period=False):
    '''Calculates demerit point information, returns tuple of (<True/False> penalty_points)
    where True/False is wether or not the penalty is mandatory.'''

    penalty_points = False

    if driving_speed>speed_limit:
        if 0<(driving_speed-speed_limit)<= 10:
            penalty_points = 10
        elif 20>=(driving_speed-speed_limit)>10:
            penalty_points = 20
        elif 30>=(driving_speed-speed_limit)>20:
            penalty_points = 30
        elif driving_speed-speed_limit > 30:
            penalty_points = 50

        if penalty_points:
            return (True, penalty_points) if (holiday_period and driving_speed-speed_limit>4) or (not(holiday_period) and (driving_speed-speed_limit>5)) else (False, penalty_points)   
    return (False, 0)


def validation(x, y):
    '''validates user input from home.html, returns message to flash to user for invalid case, 
    returns None if inputs are good'''

    try:
        float(x)
        validity=True
    except ValueError:    #Block of code determines wether driving speed entered is able to convert to type float
        validity=False

    try:
        int(y)
        if validity:
            return None                                         #Checks if speed limit entered is able to convert to type int
        return 'Driving speed must be type int or float.'
    
    except ValueError:
        if validity:
            return 'Speed limit must be type int.'
        return 'Driving speed must be type int or float. Speed limit must be type int.'

def message(x, driving_speed, speed_limit):
    '''Returns string pertaining to the type of penalty a user is liable for IF liable.'''

    if x[1]:
        if x[0]:
            option = 'madatory'
        else:
            option = 'discretional'
        return f'The {option} penalty for driving at {driving_speed}km/h in a {speed_limit}km/h zone is {x[1]} points'
    return f'{driving_speed}km/h in a {speed_limit}km/h zone is not speeding.'
    
