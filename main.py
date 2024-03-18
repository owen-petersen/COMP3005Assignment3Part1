import psycopg


class DatabaseInterface:
    def __init__(self):
        """
        Creates and interface for the database. Database is currently hardcoded but can be changed.
        """
        try:
            self.conn = psycopg.connect(
                "dbname=assignment3 user=postgres password=10/11/2003 host=localhost port=5432"
            )
        except psycopg.OperationalError as e:
            print(f"Error: {e}")
            exit(1)
        self.conn.autocommit = True #automatically commit any changes to the database
        self.cursor = self.conn.cursor()

    def close(self) -> None:
        """
        closes the connection to the database once finished.
        """
        self.cursor.close()
        self.conn.close()

    def getAllStudents(self) -> None:
        """
        Gets all students in the table
        """
        self.cursor.execute("SELECT * FROM students")
        rows = self.cursor.fetchall()
        print("student_it, first_name, last_name, email, enrollment_date") #prints the header
        for row in rows:
            print(row) #Prints each row of the database

    def addStudent(self, first_name: str, last_name: str, email: str, enrollment_date: str) -> None:
        """
        Inserts a new student into the table with the specified values
        """
        self.cursor.execute(f"INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES ('{first_name}', '{last_name}', '{email}', '{enrollment_date}')")

    def updateStudentEmail(self, student_id: int, new_email: str) -> None:
        """
        Updates an existing student's email with the new specified email.
        """
        self.cursor.execute(f"UPDATE students SET email = '{new_email}' WHERE student_id={student_id}")

    def deleteStudent(self, student_id: int) -> None:
        """
        Removes the specified student from the database.
        """
        self.cursor.execute(f"DELETE FROM students WHERE student_id={student_id}")


if __name__ == "__main__":
    database = DatabaseInterface()
    while True:
        #Displays the available commands
        print("------------------------------")
        print("[1] getAllStudents")
        print("[2] addStudent")
        print("[3] updateStudentEmail")
        print("[4] deleteStudent")
        userInput = input("Enter number to select function or type 'quit' to close application: ")
        match userInput:
            case "1":
                database.getAllStudents()
            case "2":
                first_name = input("Provide a first name for the new student: ")
                last_name = input("Provide a last name for the new student: ")
                new_email = input("Provide an email for the new student: ")
                enrollment_date = input("Provide the enrollment date for the new student (YYYY-MM-DD): ")
                database.addStudent(first_name, last_name, new_email, enrollment_date)
            case "3":
                student_id = int(input("Select a student id to update: "))
                new_email = input("Provide a new email for the selected student: ")
                database.updateStudentEmail(student_id, new_email)
            case "4":
                student_id = int(input("Provide the student id of the student you wish to remove: "))
                database.deleteStudent(student_id)
            case "quit": #ends the loop, exits the application
                print("Exiting program.")
                break
            case _: #default case for match, never used
                print()

    database.close() #close the connection when finished