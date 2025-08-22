import re
import csv
import os
import argparse

def extract_issue_data(file_path):
    """Extract issue name, cycle, and last duration minutes from a markdown file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Extract Issue Name
    issue_name_match = re.search(r'Issue Name:\s*(.+)', content)
    issue_name = issue_name_match.group(1).strip() if issue_name_match else ""
    
    # Extract Cycle
    cycle_match = re.search(r'Cycle:\s*(\d+)', content)
    cycle = cycle_match.group(1) if cycle_match else ""
    
    # Extract Last Duration Minutes
    duration_match = re.search(r'Last Duration Minutes:\s*([\d.]+)', content)
    duration = duration_match.group(1) if duration_match else ""
    
    # Replace backslashes with forward slashes in issue name
    issue_name = issue_name.replace('\\', '/')
    
    return issue_name, cycle, duration

def generate_csv_output(input_folder, output_file):
    """Generate CSV output from issue files."""
    # Prepare output data
    output_data = []
    
    # Process each issue file in the input folder
    for filename in os.listdir(input_folder):
        if filename.startswith('issue-') and filename.endswith('.md'):
            file_path = os.path.join(input_folder, filename)
            if os.path.exists(file_path):
                issue_name, cycle, duration = extract_issue_data(file_path)
                output_data.append([issue_name, cycle, duration])
                print(f"Processed: {file_path}")
            else:
                print(f"File not found: {file_path}")
    
    # Write to CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Write header
        writer.writerow(['Issue Name', 'Cycle', 'Last Duration (minutes)'])
        # Write data rows
        writer.writerows(output_data)
    
    print(f"\nCSV file generated: {output_file}")
    print("Content:")
    with open(output_file, 'r', encoding='utf-8') as f:
        print(f.read())

def main():
    """Main function to parse arguments and generate CSV output."""
    parser = argparse.ArgumentParser(description='Generate CSV report from issue markdown files.')
    parser.add_argument('input_folder', help='Input folder containing markdown issue files')
    parser.add_argument('output_file', help='Output CSV file path')
    
    args = parser.parse_args()
    
    # Validate input folder exists
    if not os.path.exists(args.input_folder):
        print(f"Error: Input folder '{args.input_folder}' does not exist.")
        return
    
    generate_csv_output(args.input_folder, args.output_file)

if __name__ == "__main__":
    main()