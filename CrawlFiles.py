import os
import csv

with open('test.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Select location of files
    for root, dirs, files in os.walk('C:/'):
        for file in files:
            # choose file extension
            if file.endswith('.exe'):
                # Write the path to a csv file
                csvwriter.writerow([os.path.join(root, file)])
