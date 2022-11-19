def coding_problem_24():

    class LockingBinaryTreeNode(object):

        def __init__(self, parent = None, left_c = None, right_c = None):

            self.parent, self.left, self.right = parent, left_c, right_c
            self.locked, self.descendants_locked = False, False

            for child_node in (left_c, right_c):
                if child_node:
                    child_node.parent = self

        def is_locked(self):
            return self.locked

        def set_lock(self, lock_state):

            if self.descendants_locked:
                return False

            parent = self.parent

            while parent:

                if parent.locked:
                    return False
                parent = parent.parent

            self.locked = lock_state
            parent = self.parent

            while parent:
                parent.descendants_locked = any(False if node is None else (node.locked or node.descendants_locked)
                for node in (parent.left, parent.right))
                parent = parent.parent

            return True

        def lock(self):
            return self.set_lock(True)

        def unlock(self):
            return self.set_lock(False)

    return LockingBinaryTreeNode