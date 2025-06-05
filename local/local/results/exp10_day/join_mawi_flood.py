# File paths
file1 = "day_20240619_2.txt"
file2 = "flood.txt"
output_file = "day_flood_20240619_2.txt"

# Read the lines from both files
with open(file1, 'r') as f1, open(file2, 'r') as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

# Determine the maximum number of lines
max_len = max(len(lines1), len(lines2))

# Open the output file for writing
with open(output_file, 'w') as out:
    for i in range(max_len):
        # Get the value from each file, or 0 if the line doesn't exist
        val1 = int(float(lines1[i].strip())) if i < len(lines1) else 0
        val2 = int(float(lines2[i].strip())) if i < len(lines2) else 0
        # Write the integer sum to the output file
        out.write(f"{val1 + val2}\n")

print(f"Combined integer file written to {output_file}")
