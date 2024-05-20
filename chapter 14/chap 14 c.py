def copy_and_number_lines(input_filename, output_filename):
 
  with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
    line_number = 1
    for line in input_file:
      # Extract content after the first five columns (assuming space delimiter)
      content = line.split(maxsplit=5)[5:]
      # Join the content back into a line with a space separator
      formatted_line = ' '.join(content)
      # Create the line with five-digit numbering and add a space
      output_line = f"{line_number:05d} {formatted_line}"
      output_file.write(output_line)
      line_number += 1

# Example usage
input_filename = "qc.txt"
output_filename = "qc2.txt"
copy_and_number_lines(input_filename, output_filename)
print(f"Lines copied and numbered to {output_filename}")
