Fitness Tracker CLI
A lightweight, object-oriented Command Line Interface for tracking workouts, cardio, nutrition, and bodyweight. This tool saves data to a structured format for easy analysis later.

🚀 Getting Started
Prerequisites
Python 3.8+

Pandas (for data processing)

Installation
Clone the repository:

Bash
git clone https://github.com/yourusername/fitness-tracker-cli.git
cd fitness-tracker-cli
Install dependencies:

Bash
pip install -r requirements.txt
Running the Program
To start the tracker, open your terminal in the project folder and run:

Bash
python main.py
🛠 Features
Resistance Training: Log exercises, multiple sets, reps, and weight.

Cardio Tracking: Record activity types and duration.

Nutrition: Track calories, macronutrients, and consistency.

Bodyweight: Monitor weight changes over time with notes.

History: View recent entries before logging new ones to stay on track.

📂 Project Structure
main.py: The entry point that initializes the CLI.

cli.py: The CLI that the user will see.

models.py: Contains the @dataclass definitions for Workout, Cardio, etc.

tracker.py: The logic layer that handles data processing and cleaning.

store.py: Manages reading and writing to the data storage (CSV/Excel).

📝 Usage Example
When you run main.py, follow the on-screen prompts:

Select 1 to log a workout.

Enter the exercise name (e.g., "Squats").

Enter the number of sets.

For each set, provide the reps and weight.

Hit Enter to finish and save!

Check the created excel file!