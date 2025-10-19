import os
import ra2mix

# Define paths
red_alert_folder = r"D:\Games\Red Alert 2\Game"
output_folder = r"R:\output"

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

def extract(folder):
    # Iterate over all .mix files in the Red Alert folder
    for file in os.listdir(folder):
        if file.lower().endswith(".mix"):
            mix_path = os.path.join(folder, file)
            print(f"Processing: {mix_path}")

            try:
                filemap = ra2mix.read(mix_path)
            except Exception as e:
                print(f"Failed to read {mix_path}: {e}")
                continue

            # Iterate over files inside the .mix archive
            for filename, file_data in filemap.items():
                if filename.lower().endswith((".wav", ".mp3", ".mix")):
                    output_path = os.path.join(output_folder, filename)
                    try:
                        with open(output_path, "wb") as f:
                            f.write(file_data)
                        print(f"Extracted: {filename}")
                    except Exception as e:
                        print(f"Failed to write {filename}: {e}")

extract(red_alert_folder)
extract(output_folder)

for file in os.listdir(output_folder):
    if file.endswith(".mix"):
        os.remove(os.path.join(output_folder, file))
        print(f"Deleted: {file}")