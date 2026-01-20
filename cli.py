from datetime import datetime

from models import Cardio, Nutrition, Bodyweight
from tracker import FitnessTracker


def today_str() -> str:
    return datetime.now().strftime("%Y-%m-%d")


class TrackerCLI:
    """
    Represents the Command Line Interface the user will see.

    This class will manage the menu, handle user input/output in the terminal, validate user data, and coordinate with tracker.py or the FitnessTracker Class for data persistence.
    
    Attributes:
        tracker (FitnessTracker): The FitnessTracker class used for backend tracker logic.
    """
    def __init__(self, tracker: FitnessTracker):
        """
        Initializes the CLI with a specific backend tracker.

        Args:
            tracker (FitnessTracker): The logic engine used to save and retrieve data.
        """
        self.tracker = tracker

    def run(self) -> None:
        """
        Starts the main infinite loop of the CLI.

        Displays the menu and dispatches user choices to the appropiate logging method.
        """
        while True:
            print("\nFitness Tracker")
            print("1. Log workout (one exercise, multiple sets)")
            print("2. Log cardio")
            print("3. Log nutrition")
            print("4. Log bodyweight")
            print("5. Exit")

            choice = input("Choose: ").strip()

            if choice == "1" or choice == "Log workout":
                self._log_workout()
            elif choice == "2" or choice == "Log cardio":
                self._log_cardio()
            elif choice == "3" or choice == "Log nutrition":
                self._log_nutrition()
            elif choice == "4" or choice == "Log bodyweight":
                self._log_bodyweight()
            elif choice == "5" or choice == "Exit":
                break
            else:
                print("❌ Invalid choice")

    # -------- Loggers --------
    def _log_workout(self) -> None:
        """
        Interface for logging workouts.

        Handles a multi-step input process:
            1. Prompts for date and exercise name
            2. Loops to collect sets, reps, and weights.
            3. Passes the data to the tracker.
        """
        self.tracker.show_last_workouts()

        date = input(f"Date (YYYY-MM-DD) [default {today_str()}]: ").strip() or today_str()
        
        print("\n--- Logging Workout ---")

        while True:
            exercise = input("Exercise: ").strip()
            if not exercise:
                print("✅ Workout complete.")
                break

            try:
                num_sets = int(input("How many sets? ").strip())
                if num_sets <= 0:
                    print("❌ Sets must be > 0")
                    continue
            except ValueError:
                print("❌ Enter a valid integer for sets.")
                continue

            sets = []
            for i in range(1, num_sets + 1):
                try:
                    reps = int(input(f"Set {i} reps: ").strip())
                    weight = float(input(f"Set {i} weight: ").strip())
                    sets.append((reps, weight))
                except ValueError:
                    print("❌ Invalid reps/weight. Aborting entry.")
                    return
            
            if not sets:
                continue

            notes = input("Notes (optional): ").strip()
            self.tracker.log_workout(
                date=date, 
                exercise=exercise, 
                sets=sets, 
                notes=notes
            )
            
            print(f"✅ Saved {exercise} for {date}")
        

            again = input("Add another exercise? (y/n): ").strip().lower()
            if again != "y":
                print("✅ Workout saved.")
                break

    def _log_cardio(self) -> None:
        """
        Interface for logging cardio sessions.

        Handles a multi-step input process:
            1. Prompts for date, cardio type, and duration.
            2. Passes the data to the tracker.
        """
        self.tracker.show_last_cardio()

        date = input(f"Date (YYYY-MM-DD) [default {today_str()}]: ").strip() or today_str()
        cardio_type = input("Cardio type (walk, run, bike, etc.): ").strip()

        try:
            duration = float(input("Duration (min): ").strip())
        except ValueError:
            print("❌ Enter a valid number for duration.")
            return

        notes = input("Notes (optional): ").strip()

        entry = Cardio(
            date=date, 
            cardio_type=cardio_type, 
            duration=duration, 
            notes=notes
        )
        
        self.tracker.log_cardio(entry)

        print("✅ Saved cardio!")

    def _log_nutrition(self) -> None:
        """
        Interface for logging nutrition entries.

        Handles a multi-step input process:
            1. Prompts for calories, protein, carbs, fats, and tracked
            2. Passes the data to the tracker.
        """
        self.tracker.show_last_nutrition()

        date = input(f"Date (YYYY-MM-DD) [default {today_str()}]: ").strip() or today_str()

        try:
            calories = int(input("Calories: ").strip())
            protein = int(input("Protein (g): ").strip())
            carbs = int(input("Carbs (g): ").strip())
            fats = int(input("Fats (g): ").strip())
            tracked = bool(input("Track everything? (TRUE/FALSE) "))
        except ValueError:
            print("❌ Enter valid integers for calories/protein.")
            return

        notes = input("Notes (optional): ").strip()

        entry = Nutrition(
            date=date, 
            calories=calories,
            protein=protein, 
            carbs=carbs, 
            fats=fats, 
            tracked=tracked, 
            notes=notes
        )

        self.tracker.log_nutrition(entry)

        print("✅ Saved nutrition!")

    def _log_bodyweight(self) -> None:  
        """
        Interface for logging bodyweight.

        Handles a multi-step input process:
            1. Prompts for date and bodyweight.
            2. Passes the data to the tracker.
        """
        self.tracker.show_last_bodyweights()

        date = input(f"Date (YYYY-MM-DD) [default {today_str()}]: ").strip() or today_str()

        try:
            weight = float(input("Bodyweight: ").strip())
        except ValueError:
            print("❌ Enter a valid number for bodyweight.")
            return

        notes = input("Notes (optional): ")
        entry = Bodyweight(
            date=date, 
            weight=weight, 
            notes=notes
        )
        self.tracker.add_bodyweight(entry)
        print("✅ Saved bodyweight!")

