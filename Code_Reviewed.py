from datetime import datetime , timedelta
# import random
class CodeReviewSystem:
    def __init__(self):
        self.code_submissions = []
        self.review_assignments = []

    def check_code_id_exists(self, code_id):
        return any(submission['code_id'] == code_id for submission in self.code_submissions)

    def create_code_submission(self, project, code_id, code_content):
        if self.check_code_id_exists(code_id):
            print(f"Code ID {code_id} already exists. Please choose a different Code ID.")
            return

        submission = {
            'project': project,
            'code_id': code_id,
            'code_content': code_content,
            'developer_id': None,
            'developer_name': None,
            'review_status': "Not Assigned",
            'review_id': None,
            'assignment_timestamp': None,
            'open_timestamp': None,
            'close_timestamp': None,
        }
        self.code_submissions.append(submission)
        print(f"Code submission created successfully.")

    def read_code_submissions(self):
        if not self.code_submissions:
            print("No Code Submissions")
            return

        print("Code Submissions:")
        for submission in self.code_submissions:
            print("---------------------------------------")
            print(f"Project              : {submission['project']}")
            print(f"Code_ID              : {submission['code_id']}")
            print(f"Developer ID         : {submission['developer_id']}")
            print(f"Developer Name       : {submission['developer_name']}")
            print(f"Code Content         : {submission['code_content']}")
            print(f"Review ID            : {submission['review_id']}")
            print(f"Review Status        : {submission['review_status']}")
            print(f"Review Assign Time   : {submission['assignment_timestamp']}")
            print(f"Review Open Time     : {submission['open_timestamp']}")
            print(f"Review Close Time    : {submission['close_timestamp']}")
            print("\n")

    def assign_review(self, code_id, developer_name, review_id):
        if not self.check_code_id_exists(code_id):
            print(f"Code submission {code_id} not found.")
            return

        assignment_timestamp = datetime.now()
        for submission in self.code_submissions:
            if submission['code_id'] == code_id:
                submission['review_id'] = review_id
                submission['review_status'] = "Assigned"
                submission['developer_id'] = code_id
                submission['developer_name'] = developer_name
                submission['assignment_timestamp'] = assignment_timestamp
                print(f"Review assigned successfully.")
                return

    def update_code(self, code_id, review_id, code_content, review_status):
        
        if not self.check_code_id_exists(code_id):
            print(f"Code submission {code_id} not found.")
            return

        found_submission = False
        for submission in self.code_submissions:
            if submission['code_id'] == code_id:
                found_submission = True
                if submission['review_status'] != "Assigned":
                    print(f"Code ID {code_id} is not assigned for review. Cannot update.")
                    return
                elif submission['open_timestamp'] is None:
                    print(f"Code ID {code_id} is not yet opened for review. Cannot update.")
                    return

                submission['review_status'] = review_status
                submission['code_content'] = code_content
                submission['close_timestamp'] = (datetime.now() + timedelta(days=10))
                print(f"Review for code ID {code_id} by Review ID {review_id} marked as {review_status}.")
                return

        if not found_submission:
             print(f"Code submission {code_id} not found.") 

    def delete_code_submission(self, code_id):
        if not self.check_code_id_exists(code_id):
            print(f"Code submission {code_id} not found.")
            return

        self.code_submissions = [submission for submission in self.code_submissions if submission['code_id'] != code_id]
        print(f"Code submission {code_id} deleted successfully.")

    def generate_review_stats(self, developer_id):
        found_submission = False
        for submission in self.code_submissions: 
            if submission['developer_id'] == developer_id: 
                found_submission = True 
                print(f"Developer Name       : {submission['developer_name']}")
                print(f"Code ID              : {submission['code_id']}")
                print(f"Review ID            : {submission['review_id']}")
                print(f"Review Status        : {submission['review_status']}") 
                print(f"Review Assign Time   : {submission['assignment_timestamp']}")
                print(f"Review Open Time     : {submission['open_timestamp']}")
                print(f"Review Close Time    : {submission['close_timestamp']}")
                break

        if not found_submission:
            print(f"No submissions found for Developer ID: {developer_id}")

    def review_code(self, code_id):
        if not self.check_code_id_exists(code_id):
            print("Code ID is incorrect!")
            return

        open_timestamp = ( datetime.now() + timedelta(days=2))
        for submission in self.code_submissions:
            if submission['code_id'] == code_id:
                submission['open_timestamp'] = open_timestamp
                submission['Review Status'] = 'In Progress'
                print("Review ID:", submission['review_id'])
                print("Code content:", submission['code_content'])
                break


code_review_system = CodeReviewSystem()

while True:
    print("\nCode Review System Menu:")
    print("1. Create Code Submission")
    print("2. Read Code Submissions")
    print("3. Update Code")
    print("4. Delete Code")
    print("5. Assign Review")
    print("6. Open Review")
    print("7. Generate Review Stats")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        project = input("Enter Project: ")
        #code_id = random.randint(1000,9999)
        code_id = input("Enter Code ID: ")
        code_content = input("Enter Code Content: ")
        code_review_system.create_code_submission(project, code_id, code_content)

    elif choice == '2':
        code_review_system.read_code_submissions()

    elif choice == '3':
        code_id = input("Enter Code ID to review: ")
        review_id = input("Enter Review ID: ")
        code_content = input("Update the Code: ")
        review_status = input("Enter Review Status (Passed/Failed): ")
        code_review_system.update_code(code_id, review_id, code_content, review_status)

    elif choice == '4':
        code_id = input("Enter Code ID to delete: ")
        code_review_system.delete_code_submission(code_id)

    elif choice == '5':
        code_id = input("Enter Code ID to assign review: ")
        developer_name = input("Enter Developer Name: ")
        review_id = input("Enter Review ID: ")
        code_review_system.assign_review(code_id, developer_name, review_id)

    elif choice == '6':
        code_id = input("Enter Code ID to Review the Code: ")
        code_review_system.review_code(code_id)

    elif choice == '7':
        developer_id = input("Enter Developer ID to check review status: ")
        code_review_system.generate_review_stats(developer_id)

    elif choice == '8':
        print("Exiting Code Review System. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 8.")
