import os
import csv

# Directory containing the input CSV files
input_directory = '/home/martin/Desktop/RIWR_Russian_Inner_water_routes/GateHouse/WOU_hourly-WOU_hourly-frv_demo7-job2702298684769811'

# Output CSV file
output_file = '/home/martin/Desktop/RIWR_Russian_Inner_water_routes/GateHouse/WOU_hourly-WOU_hourly-frv_demo7-job2702298684769811/0000_total.xtx'

# Initialize a flag to track if we need to write the header to the output file
write_header = True

# Open the output CSV file in write mode
with open(output_file, 'w', newline='') as out_csvfile:
    csv_writer = csv.writer(out_csvfile)

    # Iterate through each file in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith('.csv'):
            input_file = os.path.join(input_directory, filename)

            # Open the current input CSV file in read mode
            print(f" .. processing: {input_file}")
            with open(input_file, 'r', newline='') as in_csvfile:
                csv_reader = csv.reader(in_csvfile)

                # Read and write the header if it's the first file
                if write_header:
                    header = next(csv_reader)
                    csv_writer.writerow(header)
                    write_header = False

                # Write the remaining rows from the input file to the output file
                for row in csv_reader:
                    csv_writer.writerow(row)

print(f'All CSV files in "{input_directory}" have been merged into "{output_file}"')
