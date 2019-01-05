class Movement:
    def __init__(self, old_setup, new_setup):
        """
        Movement
        :param old_setup: Old setup to move from
        :type old_setup: list[Table]
        :param new_setup: New setup to move to
        :type new_setup: list[Table]
        """
        self.old_setup = old_setup
        self.new_setup = new_setup

    