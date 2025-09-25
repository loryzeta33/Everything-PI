import shutil
import urllib.request
import zipfile
import os


URL = "https://archive.org/download/Math_Constants/Pi.zip"
ZIP_FILE = "pi.zip"
PI_FILE = "pi_dec_1b.txt"
TEMP_FOLDER = ".temp"
PI_VALUES_FOLDER = "pi_values"


def download_billion_pi():
    os.makedirs(TEMP_FOLDER, exist_ok=True)

    # Verify download
    try:
        # Download ZIP file
        print(f"Downloading file from {URL} ...")
        urllib.request.urlretrieve(URL, os.path.join(TEMP_FOLDER, ZIP_FILE))
        print(f"Download complete.")
    except Exception as e:
        print(f"Error downloading the file: {e}")
        shutil.rmtree(TEMP_FOLDER)
        return

    # Extracting content of ZIP file
    try:
        print(f"Extracting files...")
        with zipfile.ZipFile(os.path.join(TEMP_FOLDER, ZIP_FILE), "r") as zip_ref:
            zip_ref.extractall(TEMP_FOLDER)
        print(f"Extraction complete.")
    except zipfile.BadZipFile:
        print("Error: Bad ZIP file.")
        shutil.rmtree(TEMP_FOLDER)
        return
    except Exception as e:
        print(f"Error extracting the ZIP file: {e}")
        shutil.rmtree(TEMP_FOLDER)
        return

    os.makedirs(PI_VALUES_FOLDER, exist_ok=True)

    # Verify "PI - Dec.txt" file exists
    source_path = os.path.join(TEMP_FOLDER, "PI - Dec.txt")
    if not os.path.isfile(source_path):
        print(f"Error: Source file '{source_path}' does not exist.")
        shutil.rmtree(TEMP_FOLDER)
        return

    # Copy file in the pi_values folder
    destination_path = os.path.join(PI_VALUES_FOLDER, PI_FILE)
    try:
        shutil.copy(source_path, destination_path)
        print(f"File copied to: {destination_path}")
    except Exception as e:
        print(f"Error copying file: {e}")
        shutil.rmtree(TEMP_FOLDER)
        return

    # Removing temporary folder and ZIP file
    try:
        shutil.rmtree(TEMP_FOLDER)
    except Exception as e:
        print(f"Error while cleaning: {e}")
        return


def main():
    one_b_file_path = os.path.join(PI_VALUES_FOLDER, PI_FILE)

    #Check if file already exists
    if os.path.isfile(one_b_file_path):
        print(f"File '{PI_FILE}' already downloaded and present in {PI_VALUES_FOLDER}.")
        return

    # Download file
    download_billion_pi()


if __name__ == "__main__":
    main()