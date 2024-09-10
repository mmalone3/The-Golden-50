from abc import ABC, abstractmethod

class ActivityInterface(ABC):
    @abstractmethod
    def display_activity(self):
        pass

    @abstractmethod
    def congratulate(self):
        pass

    @abstractmethod
    def printProperties(self):
        pass

class Activity(ActivityInterface):
    def __init__(self, name, duration_minutes, activity_type):
        """
        Initialize an Activity object.

        Args:
            name (str): Name of the person performing the activity.
            duration_minutes (int): Duration of the activity in minutes.
            activity_type (str): Type of activity being performed.
        """
        self.name = name
        self.duration_minutes = duration_minutes
        self.activity_type = activity_type

    def display_activity(self):
        """
        Display the activity information.
        """
        print(f"Activity Type: {self.activity_type}")
        print(f"Duration: {self.duration_minutes} minutes")
        print(f"Name: {self.name}")

    def congratulate(self):
        """
        Print a congratulatory message for completing the activity.
        """
        print(f"Good job {self.name} for spending {self.duration_minutes} minutes on {self.activity_type}!")

    def printProperties(self):
        """
        Print all properties of the class using reflection.
        """
        print("Properties of the Activity class:")
        for key, value in vars(self).items():
            print(f"{key}: {value}")

# Inherited class
class AdvancedActivity(Activity):
    def __init__(self, name, duration_minutes, activity_type, intensity):
        """
        Initialize an AdvancedActivity object.

        Args:
            name (str): Name of the person performing the activity.
            duration_minutes (int): Duration of the activity in minutes.
            activity_type (str): Type of activity being performed.
            intensity (str): Intensity level of the activity.
        """
        super().__init__(name, duration_minutes, activity_type)
        self.intensity = intensity

    def display_activity(self):
        """
        Display the advanced activity information.
        """
        super().display_activity()
        print(f"Intensity: {self.intensity}")

    def printProperties(self):
        """
        Print all properties of the class using reflection.
        """
        print("Properties of the AdvancedActivity class:")
        for key, value in vars(self).items():
            print(f"{key}: {value}")

# Example usage:
if __name__ == "__main__":
    # Static creation of AdvancedActivity
    advanced_activity = AdvancedActivity("Alice", 60, "Running", "High")
    advanced_activity.display_activity()
    advanced_activity.congratulate()
    advanced_activity.printProperties()

    # Dynamic creation of AdvancedActivity
    name = input("Enter your name: ")
    duration = int(input("Enter activity duration in minutes: "))
    activity_type = input("Enter activity type: ")
    intensity = input("Enter activity intensity (Low, Medium, High): ")

    dynamic_advanced_activity = AdvancedActivity(name, duration, activity_type, intensity)
    dynamic_advanced_activity.display_activity()
    dynamic_advanced_activity.congratulate()
    dynamic_advanced_activity.printProperties()