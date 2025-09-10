import re
import csv
import os
import argparse

def extract_issue_data(file_path):
    """Extract all issue name, cycle, and last duration minutes entries from a markdown file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Extract all Issue Names
    issue_names = re.findall(r'Issue Name:\s*(.+)', content)
    
    # Extract all Cycles
    cycles = re.findall(r'Cycle:\s*(\d+)', content)
    
    # Extract all Last Duration Minutes
    durations = re.findall(r'Last Duration Minutes:\s*([\d.]+)', content)
    
    # Create list of tuples for all entries
    entries = []
    max_entries = max(len(issue_names), len(cycles), len(durations))
    
    for i in range(max_entries):
        issue_name = issue_names[i].strip().replace('\\', '/') if i < len(issue_names) else ""
        cycle = cycles[i] if i < len(cycles) else ""
        duration = durations[i] if i < len(durations) else ""
        entries.append((issue_name, cycle, duration))
    
    return entries

def generate_csv_output(input_folder, output_file):
    """Generate CSV output from issue files."""
    # Prepare output data
    output_data = []
    
    # Process each issue file in the input folder
    for filename in os.listdir(input_folder):
        if filename.startswith('issue-') and filename.endswith('.md'):
            file_path = os.path.join(input_folder, filename)
            if os.path.exists(file_path):
                entries = extract_issue_data(file_path)
                # Add all entries from this file
                for issue_name, cycle, duration in entries:
                    output_data.append([issue_name, cycle, duration])
                print(f"Processed: {file_path} ({len(entries)} entries)")
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