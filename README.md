# Free Time Finder and Comparison

This Python script calculates the free times for two individuals based on their schedules and bounded working hours. It then determines the common available time slots for potential meetings.

## Features

- **Free Time Finder**: Identifies gaps between scheduled activities for each person.
- **Bounded Time Adjustment**: Considers overall working hours and adjusts the free times accordingly.
- **Time Comparison**: Finds overlapping free time slots between two individuals.

## How It Works

1. **Input Schedule**: The schedules for Person 1 (`p1_time`) and Person 2 (`p2_time`) are predefined in the code.
2. **Working Hours**: Bounded working hours (`Bounded1` and `Bounded2`) are also defined.
3. **Free Time Calculation**: The `free_time_finder` function determines the free time slots between scheduled activities.
4. **Bounded Time Handling**: The `add_bound` function ensures the free time slots are adjusted to respect the bounded working hours.
5. **Comparison**: The `compare` function identifies overlapping free time slots between the two individuals.

## Functions

### `free_time_finder(time_list)`

- **Input**: A list of scheduled time intervals.
- **Output**: A list of free time intervals between the scheduled activities.

### `time_to_integer(time)`

- **Input**: A time string in `HH:MM` format.
- **Output**: Total minutes from midnight.

### `add_bound(free_time, bounded, p_time)`

- **Input**: Free time list, bounded working hours, and original schedule.
- **Output**: Adjusts free time to include the bounded working hours.

### `compare(time_1, time_2)`

- **Input**: Two lists of free time intervals.
- **Output**: Overlapping free time intervals.

## Example

```python
p1_time = [['09:00','10:30'],['10:30','12:00'],['14:00','15:00'],['16:00','17:30']]
Bounded1 = ['08:00','20:00']

p2_time = [['10:00','11:30'],['12:00','13:00'],['14:00','15:30'],['16:30','18:00']]
Bounded2 = ['08:00','19:00']

free_time_1 = free_time_finder(p1_time)
free_time_2 = free_time_finder(p2_time)
add_bound(free_time_1, Bounded1, p1_time)
add_bound(free_time_2, Bounded2, p2_time)

common_times = compare(free_time_1, free_time_2)
print(common_times)
```

**Output**: A list of overlapping time intervals available for both individuals.

## Usage

1. Modify the `p1_time`, `p2_time`, `Bounded1`, and `Bounded2` variables to match your schedules.
2. Run the script to see the common available meeting times.

