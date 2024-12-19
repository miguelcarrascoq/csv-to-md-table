import csv
import os
import sys

def csv_to_markdown(csv_content):
    # Split csv content into lines
    lines = csv_content.strip().split('\n')
    
    # Parse CSV lines
    csv_reader = csv.reader(lines, delimiter=';')
    rows = list(csv_reader)
    
    if not rows:
        return ""
        
    # Get headers
    headers = rows[0]
    
    # Calculate column widths
    widths = [max(len(str(row[i])) for row in rows) for i in range(len(headers))]
    
    # Generate header row
    markdown = '| ' + ' | '.join(str(headers[i]).ljust(widths[i]) for i in range(len(headers))) + ' |\n'
    
    # Generate separator row
    markdown += '|' + '|'.join('-' * (width + 2) for width in widths) + '|\n'
    
    # Generate data rows
    for row in rows[1:]:
        markdown += '| ' + ' | '.join(str(row[i]).ljust(widths[i]) for i in range(len(row))) + ' |\n'
        
    return markdown

if len(sys.argv) != 2:
    print("Usage: python3 csv_to_markdown.py <path_to_csv_file>")
    sys.exit(1)

csv_path = sys.argv[1]

if not os.path.exists(csv_path):
    raise FileNotFoundError(f"No such file or directory: '{csv_path}'")

with open(csv_path, 'r', encoding='utf-8') as f:
    csv_content = f.read()

# Write markdown output
output_path = os.path.splitext(csv_path)[0] + '.md'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(csv_to_markdown(csv_content))

print(f"Markdown file created at: {output_path}")