import os
import csv
from datetime import datetime
from .models import File

def import_new_csv_files(directory_path):
    # Get list of existing filenames from the database
    existing_filenames = set(File.objects.values_list('name', flat=True))

    # Iterate through files in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith('.csv') and filename not in existing_filenames:
            # File doesn't exist in the database, import it
            file_path = os.path.join(directory_path, filename)
            import_csv_file(file_path)

def import_csv_file(file_path):
    # Read data from CSV file and import it into the database
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # Assuming the CSV file has columns: Name, Date, Etat, Taille
            name = row[0]
            date_import = datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S')  # Adjust date format as needed
            etat = row[2]
            taille = int(row[3])

            # Create new File object and save it to the database
            file_obj = File(name=name, date_import=date_import, etat=etat, taille=taille)
            file_obj.save()

# Example usage
if __name__ == "__main__":
    # Specify the directory path where new CSV files are expected
    directory_path =r'\static\file'

    # Call the function to import new CSV files
    import_new_csv_files(directory_path)
