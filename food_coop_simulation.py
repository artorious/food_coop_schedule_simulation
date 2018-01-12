#!/usr/bin/env python3
""" A Food Co-op's Worker Scheduling Simulation

Schedule requires two members working (on-the-clock) at all times.
Program  simulates the number of people that show up for work using two 
different worker scheduling methods in which;
    - Workers sign up for certain time slots
    - Workers show up whenever they want.

The program  performs simulation for both scheduled and unscheduled approaches
based on assumed probabilities of typical human behaviour.

Compares the effectivenes of the scheduled vs. the unscheduled approach both 
from the co-op's and the members' point of view.
"""

import random 

# NOTE:
# Probabilities for simulation (for values between 1 - 100)
# come_late_**_min = chance of being late for work
# come_early_**_min = chance of leaving early from work
# no_show_sched = Chance that a scheduled worker WILL NOT show up for work
# showup_unsched = Chance that an unscheduled worker WILL  show up to work

def event_occurred(chances):
    """ (int) -> bool 
    For given value <chances> as a percentage value (1-100), 
    returns True if randomly generated number in range(1, 100) is
    less than or equal to <chances>, otherwise returns False
    """
    return 

def num_workers_showed_up(indiv_chance, num_individuals):
    """ (int, int) -> int
    
    For given intger values <indiv_chance> and <num_individuals>,
    returns how many times  that  <num_individuals> calls to 
    event_occurred(<indiv_chance>) returns True
    """
    return 

def display_scheduled_worker_hrs(worker_num, probabilities):
    """ (int, dict) -> stdout
    
    For <worker_num> equal to 1 or 2, and the <probalities> values given in a
    ditionary in the form
        { 
            'come_late_15_min': <num>, 'come_late_30_min': <num>, 
            'come_late_45_min': <num>, 'close_early_15_min': <num>, 
            'close_early_30_min': <num>, 'no_show_sched': <num>
        }
    where each <num> is a value between 1-100, dispalys one of 

        worker <worker_num> -- no show --   or
        worker <worker_num> -- <mins_late> mins late and/or
        worker <worker_num> -- left <mins_early> imins easrly
    
    where <mins_late> is 15, 30, or 45, <mins_early> is 15 or 30
    """
    pass

def display_unscheduled_worker_hrs(worker_num, probabilities):
    """ (int, dict) -> stdout
    
    For <worker_num> equal to 1 or 2, and the <probalities> values given in a
    ditionary in the form
        { 
            'come_late_15_min': <num>, 'come_late_30_min': <num>, 
            'come_late_45_min': <num>, 'close_early_15_min': <num>, 
            'close_early_30_min': <num>, showup_unsched': <num>
        }
    where each <num> is a value between 1-100, dispalys one of 

        worker <worker_num> -- no show --   or
        worker <worker_num> -- <mins_late> mins late and/or
        worker <worker_num> -- left <mins_early> imins easrly
    
    where <mins_late> is 15, 30, or 45, <mins_early> is 15 or 30
    """
    pass

def execute_scheduled_simulation(probabilities, days, time_slots):
    """ (dict, tuple, tuple) -> stdout

    Displays a simulated week of workers in attendance for all time slots,
    based on a scheduled worker schedule. 
    """
    pass

def execute_unscheduled_simulation(probabilities, days, time_slots):
    """ (dict, tuple, tuple) -> stdout

    Displays a simulated week of workers in attendance for all time slots,
    based on an  unscheduled worker schedule. 
    """
    pass



def main():
    """ Overall Steps of the program"""
    #  Init: assumed number of co-op members for simulation
    num_members = 75 
    # Init: start time of all the two-hour time slots that workers may work
    time_slots = ('8:00am', '10:00am', '12:00pm', '4:00pm', '6:00pm')
    # Init: days of the week that the co-op is open (every day of the week)
    days = ( 
        'Sunday','Monday','Tuesday','Wednesday',
        'Thursday','Friday', 'Saturday')
    # Init: (for values between 1-100 )
    # assumed probabilities for when scheduled workers show up late, leave early, or don’t show up at all        
    sched_probabilities = { 
        'come_late_15_min': 15, 
        'come_late_30_min': 5, 
        'come_late_45_min': 2,
        'close_early_15_min': 5, 
        'close_early_30_min': 3,
        'no_show_sched':15}
    # Init: (for values between 1-100 )
    # assumed probabilities for when unscheduled workers show up late, leave early, and decide to show up to work for a given time slot
    unsched_probabilities = { 
        'come_late_15_min': 5, 
        'come_late_30_min': 2, 
        'come_late_45_min': 1,
        'close_early_15_min': 10, 
        'close_early_30_min': 3,
        'showup_unsched': 5}

    # seed random number generator with system clock
    # This ensures that each time the program is run, a different sequence of random numbers most likely will be generated.
    random.seed()

    # Get scheduled or unscheduled scheduling selection from user
    print('Welcome to the Food Co-op Schedule Simulation Program')

    valid_input = False # Control for simulation selection loop 
    # Start simulation
    while not valid_input:
        try:
            response = int(input(
                '(1) - scheduled, (2) - Unscheduled Simulation?\n>>> '))

            while (response != 1) and (response != 2):
                print('Invalid Selection\n')
                response = int(input(
                    '(1) - scheduled, (2) - Unscheduled Simulation?\n>>> '))
                
            if response == 1:
                print('<< SCHEDULED WORKER SIMULATION\n')
                execute_scheduled_simulation(
                    sched_probabilities, days, time_slots)
            else:
                print('<< UNSCHEDULED WORKER SIMULATION >>\n')
                execute_unscheduled_simulation(
                    unsched_probabilities, days, time_slots)
            
            valid_input = True

        except ValueError as verr:
            print('Please enter numerical value 1 or 2\n')
    

if __name__ == '__main__':
    main()


 