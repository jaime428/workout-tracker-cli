from storage import ExcelStore
from tracker import FitnessTracker
from cli import TrackerCLI


def main():
    store = ExcelStore("fitness_tracker.xlsx")
    tracker = FitnessTracker(store)
    app = TrackerCLI(tracker)
    app.run()


if __name__ == "__main__":
    main()
