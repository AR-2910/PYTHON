# Import the datetime module to work with date and time.
import datetime

# Prompt the user for input in the format "goal:dd.mm.yyyy".
user_input=input("enter your goal with a deadline separeated by a colon\n=>")
input_list=user_input.split(":")

# Extract the goal and deadline from user input.
goal=input_list[0]
deadline=input_list[1]

# Convert the deadline string to a datetime object.
deadline_date=datetime.datetime.strptime(deadline, "%d.%m.%Y")

# Get the current date and time.
today_date=datetime.datetime.today()

# Calculate the number of days from now until the deadline.
time_left=deadline_date-today_date

# Display the message with the calculated time left.
print(f"dear user, you have about {time_left.days} days left to accomplish {goal}")
