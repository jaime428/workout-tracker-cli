from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass
class Workout:
    """
    Represents a single set within a workout session. This class serves as a data model for indiviudal exercise entries.

    Attributes:
        date (str): The date of the working in the "YYYY-MM-DD" Format
        exercise (str): The name of the exercise
        set_number (int): The set number for this exercise
        reps (int): The number of reps completed.
        weight (float): The amount of weight lifted.
        notes (str, optional): Optional notes about the set.
    """
    date: str
    exercise: str
    set_number: int
    reps: int
    weight: float
    notes: str = ""

    @staticmethod
    def sheet_name() -> str:
        """
        Provides the sheet name for Workout Class, used for the spreadsheet.
        
        Returns:
            str: The name of the workout sheet where workout data is stored.
        """
        return "Workouts"

    @staticmethod
    def columns() -> List[str]:
        """
        Defines the header names for the storage medium.

        Returns:
            List[str]: A list of strings represent the header names
        """
        return ["Date", "Exercise", "SetNumber", "Reps", "Weight", "Notes"]

    def to_row(self) -> Dict[str, Any]:
        """
        Used for inserting data into the spreadsheet or dataframes.

        Returns:
            Dict[str, Any]: A mapping of column names to workout attributions.
        """
        return {
            "Date": self.date,
            "Exercise": self.exercise,
            "SetNumber": self.set_number,
            "Reps": self.reps,
            "Weight": self.weight,
            "Notes": self.notes,
        }

@dataclass
class Cardio:
    """
    Represents a single cardio session. This class serves as a data model for indiviudal cardio entries.

    Attributes:
        date (str): The date of the working in the "YYYY-MM-DD" Format.
        cardio_type (str): The name of the cardio the user is doing.
        duration (float): The duration of the cardio session.
        notes (str, optional): Optional notes about the session.
    """
    date: str
    cardio_type: str
    duration: float
    notes: str = ""

    @staticmethod
    def sheet_name() -> str:
        """
        Provides the sheet name for Cardio Class, used for the spreadsheet.
        
        Returns:
            str: The name of the cardio sheet where cardio data is stored.
        """
        return "Cardio"
    
    @staticmethod
    def columns() -> List[str]:
        """
        Defines the header names for the storage medium.

        Returns:
            List[str]: A list of strings represent the header names
        """
        return ["Date", "Cardio Type", "Duration", "Notes"]
    
    def to_row(self) -> Dict[str, Any]:
        """
        Used for inserting data into the spreadsheet or dataframes.

        Returns:
            Dict[str, Any]: A mapping of column names to workout attributions.
        """
        return{
            "Date": self.date,
            "Cardio Type": self.cardio_type,
            "Duration": self.duration,
            "Notes": self.notes
        }

@dataclass   
class Nutrition:
    """
    Represents a full day of eating. This class serves as a data model for indiviudal nutrition entries.

    Attributes:
        date (str): The date of the working in the "YYYY-MM-DD" Format.
        calories (int): The total amount of calories the user ate.
        protein (int): The total number of protein (g) the user ate.
        carbs (int): The total number of carbs (g) the user ate.
        fats (int): The total number of fats (g) the user ate.
        tracked (bool): Whether or not the user tracked all of their foods.
        notes (str, optional): Optional notes about the full day of eating.
    """
    date: str
    calories: int
    protein: int
    carbs: int
    fats: int
    tracked: bool
    notes: str = ""

    @staticmethod
    def sheet_name() -> str:
        """
        Provides the sheet name for Nutrition Class, used for the spreadsheet.
        
        Returns:
            str: The name of the nutrition sheet where nutrition data is stored.
        """
        return "Nutrition"
    
    @staticmethod
    def columns() -> List[str]:
        """
        Defines the header names for the storage medium.

        Returns:
            List[str]: A list of strings represent the header names
        """
        return ["Date", "Calories", "Protein", "Carbs", "Fats", "Tracked?", "Notes"]
    
    def to_row(self) -> Dict[str, Any]:
        """
        Used for inserting data into the spreadsheet or dataframes.

        Returns:
            Dict[str, Any]: A mapping of column names to workout attributions.
        """
        return{
            "Date": self.date,
            "Calories": self.calories,
            "Protein": self.protein,
            "Carbs": self.carbs,
            "Fats": self.fats,
            "Tracked?": self.tracked,
            "Notes": self.notes
        }
    
@dataclass
class Bodyweight:
    """
    Represents a single bodyweight entry. This class serves as a data model for indiviudal bodyweight entries.

    Attributes:
        date (str): The date of the working in the "YYYY-MM-DD" Format.
        weight (float): The amount the user weighed in at.
        notes (str, optional): Optional notes about the session.
    """
    date: str
    weight: float
    notes: str = ""

    @staticmethod
    def sheet_name() -> str:
        """
        Provides the sheet name for Bodyweight Class, used for the spreadsheet.
        
        Returns:
            str: The name of the bodyweight sheet where bodyweight data is stored.
        """
        return "Bodyweight"
    
    @staticmethod
    def columns() -> List[str]:
        """
        Defines the header names for the storage medium.

        Returns:
            List[str]: A list of strings represent the header names
        """
        return ["Date", "Weight", "Notes"]
    
    def to_row(self) -> Dict[str, Any]:
        """
        Used for inserting data into the spreadsheet or dataframes.

        Returns:
            Dict[str, Any]: A mapping of column names to workout attributions.
        """
        return{
            "Date": self.date,
            "Weight": self.weight,
            "Notes": self.notes
        }


