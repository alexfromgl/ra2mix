import os
import ra2mix
import tempfile

# Define paths
red_alert_folder = r"D:\Games\Red Alert 2\Game"
output_folder = r"R:\output"

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

def extractfile(filePath):
    filemap = ra2mix.read(filePath)
    mixfilename = os.path.splitext(os.path.basename(filePath))[0]
    mix_extractedpath = os.path.join(output_folder, mixfilename)
    for filename, file_data in filemap.items():
        if filename.lower().endswith(".wav"):
            os.makedirs(mix_extractedpath, exist_ok=True)
            output_path = os.path.join(mix_extractedpath, filename)
            try:
                with open(output_path, "wb") as f:
                    f.write(file_data)
                print(f"Extracted: '{output_path}'")
            except Exception as e:
                print(f"Failed to write {filename}: {e}")
        elif filename.lower().endswith(".mix"):
            output_path = os.path.join(tempfile.gettempdir(), f"{mixfilename}-{filename}")
            try:
                with open(output_path, "wb") as f:
                    f.write(file_data)
                extractfile(output_path)
                print(f"Extracted: {filename}")
            except Exception as e:
                print(f"Failed to write {filename}: {e}")
        elif filename.lower().endswith((".bag", ".idx")):
            os.makedirs(mix_extractedpath, exist_ok=True)
            output_path = os.path.join(mix_extractedpath, filename)
            try:
                with open(output_path, "wb") as f:
                    f.write(file_data)
                print(f"Extracted: '{output_path}'")
            except Exception as e:
                print(f"Failed to write {filename}: {e}")


for file in os.listdir(red_alert_folder):
    if file.lower().endswith(".mix"):
        try:
            extractfile(os.path.join(red_alert_folder, file))
        except:
            print("Skip " + file)