import re

# Add the location to the Log File you wish to Parse
def extract_unique_ips_from_log(log_file_path):
    # Initialize a set to store unique IP addresses
    unique_ips = set()
    
    # Open the log file and read each line
    with open(log_file_path, 'r') as file:
        for line in file:
            # Use regex to find IP addresses in the current line
            ips = re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', line)
            # Add found IP addresses to the set of unique IPs
            unique_ips.update(ips)
    
    # Return the list of unique IP addresses
    return list(unique_ips)

# Call the function and print the extracted IP addresses
ips = extract_unique_ips_from_log('sample_log.txt')
print("Unique Extracted IP Addresses:")
for ip in ips:
    print(ip)
