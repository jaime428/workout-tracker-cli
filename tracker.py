import pandas as pd
from typing import List, Tuple

from models import Workout, Cardio, Nutrition, Bodyweight
from storage import ExcelStore


class FitnessTracker:
    """
    Prepares the data to be stored into the excel file.

    Attributes: 
        store (class): The ExcelStore class that operates the excel file including creating, reading, and appending.
    """
    def __init__(self, store: ExcelStore):
        """
        Initializes the storage.

        Arguments:
            store (str): Uses the ExcelStore class to store the user's data into the excel sheets.
        """
        self.store = store

    # --------------------
    # Workouts
    # --------------------
    def log_workout(self, date: str, exercise: str, sets: List[Tuple[int, float]], notes: str = "") -> None:
        """
        Logs a multi-set exercise entry to the data store.

        This method converts a list of sets into individual row dictionaries and appends them to the workout sheet.

        Arguments:
            date (str): The date of the session (YYYY-MM-DD).
            exercise (str): The name of the exercise performed.
            sets (List[Tuple[int, float]]): A list where each tuple represents 
                (reps, weight) for a single set.
            notes (str, optional): Additional comments for the entire exercise. 
                Defaults to an empty string.
        """
        rows = []
        for i, (reps, weight) in enumerate(sets, start=1):
            rows.append(
                Workout(
                    date=date,
                    exercise=exercise,
                    set_number=i,
                    reps=reps,
                    weight=weight,
                    notes=notes
                ).to_row()
            )

        self.store.append_rows(
            Workout.sheet_name(),
            Workout.columns(),
            rows
        )

    def get_workouts(self) -> pd.DataFrame:
        """
        Retrieves all logged workouts as a cleaned DataFrame.

        Reads the workout sheet and ensures that numeric columns are  properly typed for analysis (handles conversion of SetNumber, Reps, and Weight).

        Returns:
            pd.DataFrame: A DataFrame containing all workout history. 
                Returns an empty DataFrame if no data exists.
        """
        df = self.store.read_sheet(Workout.sheet_name())
        if df.empty:
            return df

        for col in ["SetNumber", "Reps", "Weight"]:
            df[col] = pd.to_numeric(df[col], errors="coerce")

        return df
    
    def show_last_workouts(self):
        """
        Prints the 5 most recent workout entries to the console.

        Useful for providing context to the user before they log a new 
        session in the CLI.
        """
        self.store.get_last_entries("Workouts", 5)

    # --------------------
    # Cardio
    # --------------------
    def log_cardio(self, entry: Cardio) -> None:
        """
        Logs a cardio entry to the data store.

        This method appends the cardio entry to the cardio sheet.

        Arguments:
            date (str): The date of the session (YYYY-MM-DD).
            entry (Cardio): The attributes of the Cardio Class including
                date (str): The date of the working in the "YYYY-MM-DD" Format.
                cardio_type (str): The name of the cardio the user is doing.
                duration (float): The duration of the cardio session.
                notes (str, optional): Optional notes about the session.
        """
        self.store.append_rows(
            Cardio.sheet_name(),
            Cardio.columns(),
            [entry.to_row()]
        )

    def get_cardio(self) -> pd.DataFrame:
        """
        Retrieves all logged cardio entries as a cleaned DataFrame.

        Reads the workout sheet and ensures that numeric columns are properly typed for analysis (handles conversion of Duration).

        Returns:
            pd.DataFrame: A DataFrame containing all cardio history. 
                Returns an empty DataFrame if no data exists.
        """
        df = self.store.read_sheet(Cardio.sheet_name())
        if df.empty:
            return df

        df["Duration"] = pd.to_numeric(df["Duration"], errors="coerce")
        return df
    
    def show_last_cardio(self):
        """
        Prints the 5 most recent cardio entries to the console.

        Useful for providing context to the user before they log a new 
        session in the CLI.
        """
        self.store.get_last_entries("Cardio", 5)

    # --------------------
    # Nutrition
    # --------------------
    def log_nutrition(self, entry: Nutrition) -> None:
        """
        Logs a nutrition entry to the data store.

        This method appends the nutrition entry to the nutrition sheet.

        Arguments:
            date (str): The date of the session (YYYY-MM-DD).
            entry (Nutrition): The attributes of the Nutrition Class including
                calories (int): The total amount of calories the user ate.
                protein (int): The total number of protein (g) the user ate.
                carbs (int): The total number of carbs (g) the user ate.
                fats (int): The total number of fats (g) the user ate.
                tracked (bool): Whether or not the user tracked all of their foods.
                notes (str, optional): Optional notes about the full day of eating.
        """
        self.store.append_rows(
            Nutrition.sheet_name(),
            Nutrition.columns(),
            [entry.to_row()]
        )

    def get_nutrition(self) -> pd.DataFrame:
        """
        Retrieves all logged nutrition entries as a cleaned DataFrame.

        Reads the workout sheet and ensures that numeric columns are properly typed for analysis (handles conversion of Calories, Protein, Carbs, Fats).

        Returns:
            pd.DataFrame: A DataFrame containing all nutrition history. 
                Returns an empty DataFrame if no data exists.
        """
        df = self.store.read_sheet(Nutrition.sheet_name())
        if df.empty:
            return df

        for col in ["Calories", "Protein", "Carbs", "Fats"]:
            df[col] = pd.to_numeric(df[col], errors="coerce")

        return df
    
    def show_last_nutrition(self):
        """
        Prints the 5 most recent nutrition entries to the console.

        Useful for providing context to the user before they log a new 
        session in the CLI.
        """
        self.store.get_last_entries("Nutrition", 5)

    # --------------------
    # Bodyweight
    # --------------------
    def add_bodyweight(self, entry: Bodyweight) -> None:
        """
        Logs a bodyweight entry to the data store.

        This method appends the bodyweight entry to the bodyweight sheet.

        Arguments:
            date (str): The date of the session (YYYY-MM-DD).
            entry (Bodyweight): The attributes of the Bodyweight Class including
                date (str): The date of the working in the "YYYY-MM-DD" Format.
                weight (float): The amount the user weighed in at.
                notes (str, optional): Optional notes about the session.
        """
        self.store.append_rows(
                Bodyweight.sheet_name(),
                Bodyweight.columns(),
                [entry.to_row()]
        )

    def get_bodyweight(self) -> pd.DataFrame:
        """
        Retrieves all logged bodyweights as a cleaned DataFrame.

        Reads the workout sheet and ensures that numeric columns are properly typed for analysis (handles conversion of Weight).

        Returns:
            pd.DataFrame: A DataFrame containing all bodyweight history. 
                Returns an empty DataFrame if no data exists.
        """
        df = self.store.read_sheet(Bodyweight.sheet_name())
        if df.empty:
            return df

        df["Weight"] = pd.to_numeric(df["Weight"], errors="coerce")
        return df.sort_values("Date")


    def show_last_bodyweights(self):
        """
        Prints the 5 most recent bodyweight entries to the console.

        Useful for providing context to the user before they log a new 
        session in the CLI.
        """
        self.store.get_last_entries("Bodyweight", 5)

    