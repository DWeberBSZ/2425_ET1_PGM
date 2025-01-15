# Pfade der Eingabe- und Ausgabedateien
input_file = "namen_input.txt"
output_file = "namen_output.txt"

# Einlesen
with open(input_file, 'r') as infile:
    lines = infile.readlines()

# Schreiben
with open(output_file, 'w') as outfile:
    for i in range(0, len(lines), 2):
        first_name = lines[i].strip()
        last_name = lines[i + 1].strip()
        outfile.write(f"{first_name} {last_name}\n")
