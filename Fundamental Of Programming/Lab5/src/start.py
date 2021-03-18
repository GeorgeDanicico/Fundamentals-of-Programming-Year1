from src.ui.console import ui
from src.tests import tests

test = tests()
test.test_add()
test.test_filter()
test.test_undo()



complex_ui = ui()
complex_ui.start()
