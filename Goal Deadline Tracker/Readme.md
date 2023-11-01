# **Project Name: Goal Deadline Calculator**

**Project Description:**

The Goal Deadline Calculator is a Python program that allows users to set and calculate the time left to achieve a specific goal with a given deadline. It provides a user-friendly and interactive way to track progress and stay motivated.

**Key Features:**

**Goal and Deadline Input:** Users can input their goals and deadlines in the format "goal:dd.mm.yyyy".

**Time Left Calculation:** The program calculates the number of days remaining until the specified deadline.

**User-Friendly Interface:** Users are guided through the input process and receive a clear message about their goal and the time left.

**How It Works:**

1. Users are prompted to enter their goal and deadline in the format "goal:dd.mm.yyyy" when the program starts.

2. The program extracts the goal and deadline from the user input.

3. It converts the deadline into a `datetime` object using the specified date format.

4. The program obtains the current date and time.

5. It calculates the time remaining by subtracting the current date from the deadline date, resulting in a `timedelta` object.

6. The user receives a friendly message that includes the number of days left to accomplish their goal.

**Usage:**

- Run the program.
- Enter your goal and its deadline in the format "goal:dd.mm.yyyy".
- The program will calculate and display the number of days left to achieve your goal.

**Project Benefits:**

- **Goal Tracking:** Helps users set, track, and manage their goals effectively.
- **Date Calculations:** Demonstrates practical use of date and time calculations in Python.
- **User Engagement:** Provides a user-friendly interface for setting and tracking goals with deadlines.
