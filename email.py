### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

    # Declare the class variable, with default value, for emails. 
 
    # Initialise the instance variables for emails.

    # Create the method to change 'has_been_read' emails from False to True.

class Email:

    has_been_read = False

    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    def mark_as_read(self):
        """An instance method that sets the has_been_read instance
        variable to 'True'."""
        self.has_been_read = True


# --- Lists --- #
# Initialise an empty list to store the email objects.

inbox = []

# Create 3 sample emails and add it to the Inbox list.
email1 = Email("bob@gmail.com", "Welcome to HyperionDev!", "Onboarding")
email2 = Email("joe@gmail.com", "Great work on the bootcamp!", "Support")
email3 = Email("alan@gmail.com", "Your excellent marks!", "Grading")

# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox():
    """A function that creates an email object with the email address,
    subject line, and contents, and stores it in the inbox list."""
    inbox.append(email1)
    inbox.append(email2)
    inbox.append(email3)


def list_emails():
    """A function which prints the email's subject line along with a
    corresponding number."""
    print("Inbox:")
    for i, email in enumerate(inbox):
        print(i, email.subject_line)


def read_email():
    """A function that displays a selected email, together with the
    email_address, subject_line, and email_content, and then sets
    its has_been_read instance variable to True."""
    while True:
        try:
            choose_email = int(input(
                "\nWhich email do you want to see? Enter 0, 1, or 2. "))
            selected_email = inbox[choose_email]
            print("\nEmail Details:")
            print(f"From: {selected_email.email_address}")
            print(f"Subject: {selected_email.subject_line}")
            print(f"Content: {selected_email.email_content}\n")
            # Call the class method to set 'has_been_read' to True.
            selected_email.mark_as_read()
            print(f"Email from {selected_email.email_address} marked as read.")
            break
        except (IndexError, ValueError):
            """If the user inputs a different number or a non-integer
            value, we show them an error message and ask them to try
            again."""
            print("\nInvalid input. Please enter 0, 1, or 2.\n")


populate_inbox()

list_emails()

read_email()

# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.

# Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        """Call the read_email function to prompt the user to select
        an email."""
        print()  # Line break
        list_emails()  # Show the user their inbox
        read_email()
        
    elif user_choice == 2:
        """If there are any unread emails, list them. Otherwise, inform
        the user that all emails have been read."""
        any_emails_unread = False  # Track if any unread emails remain
        print("\nUnread emails:")
        for i, email in enumerate(inbox):
            if not email.has_been_read:
                """Checks for emails whose has_been_read status was not
                overriden by mark_as_read"""
                print(i, email.subject_line)
                any_emails_unread = True  # Update the unread email tracker
        if not any_emails_unread:
            """When there are no more unread emails left, print an
            informative statement"""
            print("All emails have been read.")
            
    elif user_choice == 3:
        """Logic to quit the application"""
        print("\nEnjoy the rest of your day!")
        break

    else:
        print("\nOops - incorrect input.")

