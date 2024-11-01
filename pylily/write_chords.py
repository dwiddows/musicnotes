import subprocess
import os

def generate_lilypond_thumbnail(clef, chord_name):
    # Create the output directory if it doesn't exist
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Set the absolute pitch for treble or bass clef
    if clef == "treble":
        fixed_pitch = "c"
    elif clef == "bass":
        fixed_pitch = "c,"
    else:
        raise ValueError("Invalid clef! Please use 'treble' or 'bass'.")

    # Create an output filename based on the clef and chord name
    base_filename = f"{chord_name.replace('1', '').replace(':', '_')}_{clef}"
    ly_file = os.path.join(output_dir, f"{base_filename}.ly")
    pdf_file = os.path.join(output_dir, f"{base_filename}.pdf")
    jpg_file = os.path.join(output_dir, f"{base_filename}.jpg")

    # Corrected LilyPond content with backslashes for mm units
    lilypond_content = fr"""
\version "2.24.0"

\paper {{
  #(set-paper-size "custom")
  paper-width = 30\mm
  paper-height = 20\mm
  indent = 0\mm
  top-margin = 0\mm
  bottom-margin = 0\mm
  left-margin = 2\mm
  right-margin = 2\mm
}}

\layout {{
  \context {{
    \Score
    \omit BarNumber
  }}
}}

\header {{
  tagline = ##f
}}

\fixed {fixed_pitch} {{
  \omit Staff.TimeSignature
  \clef {clef}
  \chordmode {{
    {chord_name}
  }}
}}
"""

    # Write the LilyPond content to the .ly file
    with open(ly_file, "w") as file:
        file.write(lilypond_content)

    print(f"LilyPond file generated: {ly_file}")

    # Compile the .ly file into a PDF using LilyPond
    subprocess.run(["lilypond", "-o", output_dir, ly_file], check=True)
    print(f"PDF generated: {pdf_file}")

    # Convert the PDF to a JPG using ImageMagick's convert command
    convert_command = ["magick", "-density", "300", pdf_file, "-quality", "90", jpg_file]
    subprocess.run(convert_command, check=True)
    print(f"JPG generated: {jpg_file}")

    # Keep the .ly file for debugging purposes
    print(f"Keeping .ly file: {ly_file}")

    # Optionally, remove the PDF but keep the .ly file for debugging
    os.remove(pdf_file)

    return jpg_file

# List of chord types
chord_types = ["c1", "c1:m", "c1:dim", "c1:aug", "c1:7", "c1:m7", "c1:maj7", "c1:dim7"]
clefs = ["treble", "bass"]

# Loop over each chord type and clef
for chord in chord_types:
    for clef in clefs:
        generate_lilypond_thumbnail(clef, chord)
