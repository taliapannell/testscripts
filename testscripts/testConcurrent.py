import concurrent.futures
import time
import random

# Simulate a chatbot function
def ask_chatbot(question):
    # Simulate processing time
    time.sleep(random.uniform(0.1, 1.0))
    response = f"Response to: {question}"
    return response

# Function to simulate one user asking a question
def simulate_user_question(user_id):
    question = f"User {user_id} question"
    response = ask_chatbot(question)
    print(f"User {user_id} received: {response}")
    return response

# Simulate 100 users concurrently asking questions
def simulate_concurrent_users(num_users=100):
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_users) as executor:
        futures = [executor.submit(simulate_user_question, user_id) for user_id in range(1, num_users + 1)]
        results = [future.result() for future in concurrent.futures.as_completed(futures)]
    return results

if __name__ == "__main__":
    simulate_concurrent_users()
