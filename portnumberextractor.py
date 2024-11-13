import re
# Add the location to the Log File you wish to Parse
def extract_unique_ports_from_log(log_file_path):
    # Initialize a set to store unique port numbers
    unique_ports = set()
    
    # Open the log file and read each line
    with open(log_file_path, 'r') as file:
        for line in file:
            # Use regex to find potential port numbers in the current line
            ports = re.findall(r'\b\d{1,5}\b', line)
            # Filter and add valid port numbers (0-65535) to the set
            unique_ports.update([port for port in ports if 0 <= int(port) <= 65535])
    
    # Return the list of unique port numbers
    return list(unique_ports)

# Call the function and print the extracted port numbers
ports = extract_unique_ports_from_log('sample_ports_log.txt')
print("Unique Extracted Port Numbers:")
for port in ports:
    print(port)
