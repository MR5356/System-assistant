import sys
import update_function
from PyQt5 import QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = update_function.fun_main(sys.argv)
    ui.show()
    sys.exit(app.exec_())
