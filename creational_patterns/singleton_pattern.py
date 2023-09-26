"""

Category: Creational pattern

Intent: This design pattern ensures that a class only has one instance,
while providing a global access point to this instance.

Usage:
    - Managing access to share resources, e.g. databases, files, etc.
    If we already created a database connection, later on decide to create a
    new one, we instead get the created one,

    - Singleton pattern lets us access some object from anywhere in the program,
    while protecting that instance from being overridden.


Real-world analogy: 
    Maintaining a single copy of the application state


Implementation:
    - Hide the constructor,
    - implement a static creation method.

"""


class ApplicationState:
    instance = None

    def __init__(self):
        self.is_logged_in = False

    @staticmethod
    def getAppState():
        if not ApplicationState.instance:
            ApplicationState.instance = ApplicationState()
        return ApplicationState.instance


if __name__ == '__main__':
    app_state1 = ApplicationState.getAppState()
    print(f"[INFO] {app_state1.is_logged_in}")

    app_state2 = ApplicationState.getAppState()
    app_state2.is_logged_in = True

    print(f"[INFO] {app_state1.is_logged_in}")
    print(f"[INFO] {app_state2.is_logged_in}")
