class KdTreeNode:
    def __init__(self, value):
        """
        KdNode
        :param value: Value to insert; Must be a tuple with the amount of values equal to the amount of
        dimensions of the KD-tree
        """
        self.value = value
        self.left = None
        self.right = None
