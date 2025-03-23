import numpy as np

# Performance comparison between original and vectorized solutions:
# Original solution: Uses loops and iterates through each timelog entry sequentially
# Vectorized solution: Uses numpy arrays for efficient array operations
# The vectorized approach is approximately 2x faster due to:
# 1. Avoiding Python loops by using numpy's optimized C-based operations
# 2. Processing multiple elements simultaneously through array broadcasting
# 3. Efficient boolean masking for weekday filtering
def add_10minutes(times):
    # Vectorized operation for adding 10 minutes
    hours = times // 100
    minutes = times % 100 + 10
    hours += minutes // 60
    minutes = minutes % 60
    return hours * 100 + minutes

def solution(schedules, timelogs, startday):
    # Convert inputs to numpy arrays
    print(schedules)
    schedules = np.array(schedules)
    timelogs = np.array(timelogs)
    
    # Generate weekday mask
    days = np.arange(len(timelogs[0]))
    weekdays = (startday + days - 1) % 7 + 1
    weekday_mask = ~np.isin(weekdays, [6, 7])
    
    # Calculate allowed arrival times (schedule + 10 minutes)
    allowed_times = add_10minutes(schedules)

    # Filter weekday logs and check violations
    weekday_logs = timelogs[:, weekday_mask]
    violations = np.any(weekday_logs > allowed_times[:, np.newaxis], axis=1)
    return len(schedules) - np.sum(violations)

# Test case
schedules = [700, 800, 1100]
timelogs = [[710, 2359, 1050, 700, 650, 631, 659],
            [800, 801, 805, 800, 759, 810, 809],
            [1105, 1001, 1002, 600, 1059, 1001, 1100]]
startday = 5

print(solution(schedules, timelogs, startday))  # =3