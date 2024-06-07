import csv

# Read the CSV file and store the data in a list
input_file = 'security_incidents.csv'
output_file = 'security_incidents_modified.csv'

data = []

with open(input_file, 'r', newline='') as file:
    reader = csv.reader(file)
    header = next(reader)
    data = [row for row in reader]

# Add the new column 'Status' with the default value 'Pending'
header.append('Status')
for row in data:
    row.append('Pending')

# Save the modified data to a new CSV file
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)

print(f"Data has been written to {output_file}")
