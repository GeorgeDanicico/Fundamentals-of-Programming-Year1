class UndoServiceError(Exception):
    def __init__(self, msg):
        self._msg = msg


class UndoService:
    def __init__(self):
        self._history = []
        self._index = -1

    def record(self, operation):
        # we need to make that the redo function can be called only when we have did an undo before, not when we add other operation
        # so in order to do that, we copy all the operations before the index to avoid doing a redo without a previus undo
        self._history = self._history[0:self._index+1]

        # we append the operation
        self._history.append(operation)
        self._index += 1

    def undo(self):

        if self._index == -1:
            raise UndoServiceError("No more undo's to do!...\n")
        self._history[self._index].undo()
        self._index -= 1

    def redo(self):
        if self._index == len(self._history) - 1:
            raise UndoServiceError("No more redo's to do!...\n")

        self._index += 1
        self._history[self._index].redo()

class CascadedOperation:
    def __init__(self, *operations):
        self._operations = operations

    def undo(self):
        for op in self._operations:
            op.undo()

    def redo(self):
        for op in self._operations:
            op.redo()



class OperationCall:
    def __init__(self,undo_operation, redo_operation):
        self._undo_operation = undo_operation
        self._redo_operation = redo_operation

    def undo(self):
        self._undo_operation()

    def redo(self):
        self._redo_operation()

class FunctionCall:
    def __init__(self, function_name, *function_params):
        self._function_name = function_name
        self._function_params = function_params

    def call(self):
        return self._function_name(*self._function_params)

    def __call__(self):
        self.call()