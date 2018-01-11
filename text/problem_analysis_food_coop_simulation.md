# food_coop_simulation.py - A Food Co-op's Worker Scheduling Simulation

<h1>PROBLEM ANALYSIS</h1>
<h3>Computational issue</h3> 
<p>model and simulate the behaviour of individuals 
for assumed probabilities of certain actions</p>
<dl>
    <dt>Scheduled Scenario</dt>
        <dd>Workers sign up in advance to work certain time slots.</dd>
    <dt>Unscheduled Scenario</dt>
        <dd>workers show up to work whenever they feel like it</dd>
</dl>
<h4>Assuptions &amp; Probabilities</h4>
<dl>
    <dt>Time keeping - workers showing up late or leaving early</dt>
        <dd>
            Use a random number generator to calculate these probabilities. 
            For example, if there is an assumed 10% chance that any given 
            person may show up late, a random number between 1 and 10 is 
            generated. 
            If the generated value is 1, the action is assumed to occur; 
            otherwise, the action is assumed not to occur.
        </dd>
    <dt>Working hours - schedule of hours that the co-op is open </dt>
        <ul>
            <li>Sunday  12:00 pm–6:00 pm</li>
            <li>Monday–Thursday 8:00 am–6:00 pm</li>
            <li>Friday, Saturday    8:00 am–8:00 pm</li>
        </ul>
    <dt>Time slots - every time slot is two hours long</dt>
        <dd>
            For example, there would be three time slots on Sundays, 
            12:00–2:00 pm, 2:00–4:00 pm, and 4:00–6:00 pm. 
        </dd>
        <dd>Based on this, there are 35 time slots in a week.</dd>
    <dt>Membership -the co-op has 75 members.</dt>
    <dt>
        Because of the different natures of the two scheduling approaches, 
        we assume different probabilities for the behaviors of members.
    </dt>
        <dd>
            For the scheduled approach, we assume a probability of 15% that a 
            given member will not show up for their time slot.
        </dd>
        <dd>
            For the unscheduled approach, we assume a probability that any 
            given worker will decide to show up for a given time slot to be 5%. 
        </dd>
        <dd>A scheduled worker will show up late for the start of the time 
            slot is greater than in the unscheduled approach, 
            since in the unscheduled approach workers show up for the time 
            slot that is convenient for them. 
        </dd>
        <dd>
            Assume a greater chance that unscheduled workers will leave 
            fifteen minutes earlier than scheduled workers, since they may 
            feel less committed to working the complete time slot
        </dd>
</dl>

<img src='static/assumed_probabilities_food_coop_simulation.png' 
    alt='Assumed Probabilities for the Food Co-op Simulation Program'>

<h3>Program Design</h3>
<h6>Meeting the Program Requirements<h6>
<p>
    The program must simulate the number of workers that show up for each of 
    the time slots that the co-op is open by utilizing assumed probabilities. 
    
    The co-op requires two workers in the store at all times that it is open. 
    The program must also utilize the probabilities that workers will show up 
    15, 30, or 45 minutes late for work, or leave 15 or 30 minutes early.
</p>

<h6>Data Description</h6>
<dl>
    <dt>The data that needs to be represented in this program includes;</dt>
    <dd>number of co-op members - integer,</dd>
    <dd>two-hour time slots that a worker may work -  tuple,</dd>
    <dd>Probabilities of each of the actions that may occur - dictionary</dd>
    <dd>names of the days of the week - tuple </dd>
</dl>

<pre>
    <code>
        num_members = 75
        time_slots = ('8:00am', '10:00am', '12:00pm', '4:00pm', '6:00pm')
        days = ( 
            'Sunday','Monday','Tuesday','Wednesday',
            'Thursday','Friday', 'Saturday')
        sched_probabilities = { 
            'come_late_15_min': 15, 
            'come_late_30_min': 5, 
            'come_late_45_min': 2,
            'close_early_15_min': 5, 
            'close_early_30_min': 3,
            'no_show_sched':15}
        unsched_probabilities = { 
            'come_late_15_min': 5, 
            'come_late_30_min': 2, 
            'come_late_45_min': 1,
            'close_early_15_min': 10, 
            'close_early_30_min': 3,
            'no_show_unsched': 5}
    </code>
</pre>
<p>
    In dictionary probabilities;
    <code>come_late_15_min</code>, <code>come_late_30_min</code>, <code>come_late_45_min</code>
    contain the chances that a worker will arrive 15, 30, or 45 minutes late, respectively; 
    <code>close_early_15_min</code>, <code>close_early_30_min</code> contain 
    the chances that a worker will leave 15 or 30 minutes early, respectively; 
    <code>no_show_sched</code> contains the chance that a scheduled worker will 
    not show up for their time slot; <code>no_show_unsched</code> is the chance 
    that an unscheduled worker will decide to show up to work.
</p>

<h6>Algorithmic Approach</h6>
<p>
    Use of <mark>randomization</mark> to run the simulation. 
    One complete week of co-op staffing is simulated, 
    including the number of workers showing up for each of the 35 time slots in a week, 
    how many show up a given number of minutes late, 
    and how many leave a given number of minutes early. 
    For the assumed probability of each of these actions, a random number 
    will be generated for simulating whether each event has occurred or not.
</p>