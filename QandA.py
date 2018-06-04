import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import*
from random import*
import csv

question = "Questions will appear here, press Next Q to get the first question \nor Random Q for a random question from the list"
answer = "Answers will appear here, press Answer to get the answer"
question_number = 0


app = QApplication(sys.argv)
win = QWidget()

l1 = 	QLabel()
l2 = QLabel()
l3 = QLabel()
l4 = QLabel()
b1 = QPushButton(win)			#answer button
b2 = QPushButton(win)			#next Q button
b3 = QPushButton(win)			#random Q button
b4 = QPushButton(win)			#about the program
	
l2.setUpdatesEnabled(True)
l4.setUpdatesEnabled(True)


def b1_clicked(self):
		with open("QandA.csv") as Qfile:
			readcsv = csv.reader(Qfile, delimiter=',')
			
			answers = []

			for row in readcsv:
				question = row[1]
				answer = row[2]

				answers.append(answer)	
		
				global question_number
								
			print("Answer", question_number)
			answer = answers[question_number]
			print(answer)
			l4.setText(answer)
	

def b2_clicked(self):
		with open("QandA.csv") as Qfile:
			readcsv = csv.reader(Qfile, delimiter=',')
			
			questions = []

			for row in readcsv:
				question = row[1]
				answer = row[2]

				questions.append(question)	
		
				global question_number
			
			Length = int(len(questions))
			Length -= 1

			if question_number == Length:
				question_number = 1
			else:
				question_number += 1

			print("Question", question_number)
			question = questions[question_number]
			print(question)
			l2.setText(question)
		

def b3_clicked(self):
		with open("QandA.csv") as Qfile:
			readcsv = csv.reader(Qfile, delimiter=',')
			
			questions = []

			for row in readcsv:
				question = row[1]
				answer = row[2]

				questions.append(question)	
		
				global question_number
			
			Length = int(len(questions))
			Length -= 1

			if question_number == Length:
				question_number = 1
			else:
				question_number = randint (1,Length)

			print("Question", question_number)
			question = questions[question_number]
			print(question)
			l2.setText(question)


def b4_clicked(self):
		msg=QMessageBox()
		msg.setIcon(QMessageBox.Information)
		msg.setText("A simple Quesion and Answer Quiz aimed at revision")
		msg.setInformativeText("This acts a que cards for revision purposes where you can test yourself on questions from a list of questions you have written show details for more information.")
		msg.setWindowTitle("About QandA")
		
		msg.setDetailedText("""Details on how to use this application: 

To select the next question use the next Q button, this will display the next question.

To select a random question use the Random Q button, this will display a random question.

To find the answer press the Answer button, this will display the answer to the current question.

To create a list of questions you need to use .csv file called QandA.csv in the same folder as the program.

The .csv file should have the follwing format:
ID,Question,Answer
1,What is Phtosynthesis?,Photosynthesis is the change of water and CO2 into Glucose and O2 in plants
2,What does Amylase break down?,Starch

QandA, a simple revision quiz application. Version 0.1.0.
Copyright (C) 2018  Somewun somewuns@hotmail.com
For full source code see www.github.com/........
 
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
 
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
 
You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>.""")
		
		msg.setStandardButtons(QMessageBox.Ok)
		retval=msg.exec_()


l1.setText("Question")
l1.setAlignment(Qt.AlignLeft)
l2.setText(question)
l2.setAlignment(Qt.AlignLeft)
l3.setText("Answer")
l3.setAlignment(Qt.AlignLeft)
l4.setText(answer)
l4.setAlignment(Qt.AlignLeft)
b1.setText("View Answer")
b1.move(50,20)
b1.clicked.connect(b1_clicked)
b2.setText("Next Q")
b2.move(50,20)
b2.clicked.connect(b2_clicked)
b3.setText("Random Q")
b3.move(50,20)
b3.clicked.connect(b3_clicked)								
b4.setText("About")
b4.move(50,20)
b4.clicked.connect(b4_clicked)

vbox=QVBoxLayout()
vbox.addWidget(l1)
vbox.addStretch()
vbox.addWidget(l2)
vbox.addStretch()
vbox.addWidget(l3)
vbox.addStretch()
vbox.addWidget(l4)
vbox.addStretch()
vbox.addWidget(b2)
vbox.addWidget(b3)												
vbox.addWidget(b1)
vbox.addWidget(b4)

win.setLayout(vbox)
win.resize(500, 300)
win.move(300, 300)
win.setWindowTitle("QandA Revision Questions")
win.show()
sys.exit(app.exec_())

