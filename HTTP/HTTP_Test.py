import sys
from PyQt5.QtWidgets import QLabel, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QScrollArea

from dist import HTTP_Client


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # 전체 레이아웃 설정
        hbox = QHBoxLayout()
        
        # Left Layout
        vbox_buttons = QVBoxLayout()
        
        buttons = [
            ('CASE1', 1),
            ('CASE2', 2),
            ('CASE3_4', 'CASE3_4'),
            ('CASE5', 5),
            ('CASE6', 6),
            ('CASE7', 7),
            ('CASE8', 8),
            ('CASE9', 9),
            ('CASE10', 10)
        ]
        
        for text, case in buttons:
            button = QPushButton(text, self)
            button.clicked.connect(lambda _, x=case: self.call_case(x))
            vbox_buttons.addWidget(button)
        
        # Right Layout
        vbox_texts = QVBoxLayout()
        
        # Request Box
        request_label = QLabel("Request", self)
        vbox_texts.addWidget(request_label)
        self.request_edit = QTextEdit(self)
        self.request_edit.setPlaceholderText("Request Message")
        scroll_request = QScrollArea()
        scroll_request.setWidget(self.request_edit)
        self.request_edit.setReadOnly(True)
        scroll_request.setWidgetResizable(True)
        scroll_request.setFixedHeight(150)
        vbox_texts.addWidget(scroll_request)
        
        # Response Box
        request_label = QLabel("Response", self)
        vbox_texts.addWidget(request_label)
        self.response_edit = QTextEdit(self)
        self.response_edit.setPlaceholderText("Response Message")
        scroll_response = QScrollArea()
        scroll_response.setWidget(self.response_edit)
        self.request_edit.setReadOnly(True)  # 읽기 전용 설정
        scroll_response.setWidgetResizable(True)
        scroll_response.setFixedHeight(150)
        vbox_texts.addWidget(scroll_response)
        
        # Set Layout
        hbox.addLayout(vbox_buttons)
        hbox.addLayout(vbox_texts)
        self.setLayout(hbox)
        
        # Set Window
        self.setWindowTitle('PyQt HTTP Messages Example')
        self.setGeometry(300, 300, 600, 400)
        self.setFixedSize(600, 400)
        self.show()
    
    def call_case(self, case_number):
        try:
            # Call HTTP_Client.py Func
            if isinstance(case_number, str):
                case_func = getattr(HTTP_Client, case_number)
            else:
                case_func = getattr(HTTP_Client, f'CASE{case_number}')
            
            request, response = case_func()
            
            # Set Request, Response message
            self.request_edit.setPlainText(request)
            self.response_edit.setPlainText(response)
        except Exception as e:
            self.request_edit.setPlainText(f"Error: {e}")
            self.response_edit.setPlainText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())