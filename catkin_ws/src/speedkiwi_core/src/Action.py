class Action(object):
    """
    The Action class is used to define an action for a Robot to perform.
    It is intended to be extended to define different actions that robots can perform.
    """
    def __init__(self):
        pass

    def start(self, robot):
        """
        robot: The robot that is performing the action.

        Called when the action starts executing.
        This should be overridden if you want behaviour at the start of the action.
        """
        pass

    def during(self, robot):
        """
        robot: The robot that is performing the action.

        Called during the robot's execute loop.
        This should be overridden to define the Action's behaviour.
        """
        pass

    def is_finished(self, robot):
        """
        robot: The robot that is performing the action.

        Must return true when the action is complete.
        This MUST be overridden or the Action will NEVER finish executing.
        """
        pass

    def finish(self, robot):
        """
        robot: The robot that is performing the action.

        Called when the command finishes executing.
        This should be overridden if you want behaviour at the end of the action.
        """
        pass
