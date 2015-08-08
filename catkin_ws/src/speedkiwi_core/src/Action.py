class Action(object):
    """Action for a robot to perform"""
    def __init__(self):
        pass

    def start(self, robot):
        pass

    def during(self, robot):
        pass

    def is_finished(self):
        """returns true when this action has been completed"""
    pass

    def finish(self, robot):
        pass
