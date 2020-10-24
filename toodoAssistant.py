import sys
import function
from PyQt5 import QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = function.fun_main()
    ui.show()
    sys.exit(app.exec_())
