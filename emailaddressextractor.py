import re
# # Add the location to the Log File you wish to Parse
def extract_unique_emails_from_log(log_file_path):
    # Initialize a set to store unique email addresses
    unique_emails = set()
    
    # Open the log file and read each line
    with open(log_file_path, 'r') as file:
        for line in file:
            # Use regex to find email addresses in the current line
            emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', line)
            # Add found email addresses to the set of unique emails
            unique_emails.update(emails)
    
    # Return the list of unique email addresses
    return list(unique_emails)

# Call the function and print the extracted email addresses
emails = extract_unique_emails_from_log('sample_email_log.txt')
print("Unique Extracted Email Addresses:")
for email in emails:
    print(email)
