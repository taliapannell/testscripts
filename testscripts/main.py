import csv
from testquestions import TestQuestions
from chatbot import Chatbot



with open('./questions.csv', 'r') as file:
    reader = csv.reader(file, quoting=csv.QUOTE_ALL, skipinitialspace=True)
    for row in reader:
        source = row[0]
        question = row[1]
        source_answer = row[2]
        answer_location = row[3]
        answer = row[4]
        
       #print(f"Source: {source}, Question: {question}, Answer Location: {answer_location}, Answer: {answer}")

if __name__ == "__main__":
    csv_file = './questions.csv'
    tester = TestQuestions(csv_file)
    tester.run()

