import time
import threading
import random
import csv
from chatbot import Chatbot

class TestQuestions:
    def __init__(self, csv_file, num_users=100, num_questions=50):
        self.num_users = num_users
        self.num_questions = num_questions
        self.questions = self.load_questions_from_csv(csv_file)
        self.num_questions = min(len(self.questions), 50)

    def load_questions_from_csv(self, csv_file):
        questions = []
        try:
            with open(csv_file, 'r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    questions.append(row[0]) 
        except FileNotFoundError:
            print(f"Error: CSV file '{csv_file}' not found.")
        except csv.Error as e:
            print(f"Error reading CSV file: {e}")
        return questions

    def send_question(self, question, user_id):
        start_time = time.time()
        response = chatbot_api.send_message(question) 
        end_time = time.time()

        response_time = end_time - start_time
        print(f"User {user_id}: Question: {question}, Response time: {response_time:.2f} seconds")

        if not response:
            print(f"User {user_id}: Error sending question: {question}")

    def simulate_user(self, user_id, questions):
        for question in questions:
            self.send_question(question, user_id)

    def run(self):
        threads = []
        for i in range(self.num_users):
            user_questions = random.sample(self.questions, self.num_questions)
            thread = threading.Thread(target=self.simulate_user, args=(i+1, user_questions))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

if __name__ == "__main__":
    csv_file = './questions.csv'
    tester = TestQuestions(csv_file)
    tester.run()

