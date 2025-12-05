from pathlib import Path
from uuid import uuid4

from pydicom import dcmread


def create_manifest(input_pth: Path, output_pth: Path):
    # Initialize the accession map
    accession_map = {}

    # Iterate through all subfolders in the source path
    i = 0
    for subfolder_path in [f for f in input_pth.iterdir() if f.is_dir()]:
        print(f"Processing subfolder: {subfolder_path.name}")
        for dcm_path in subfolder_path.glob("*.dcm"):
            try:
                ds = dcmread(str(dcm_path))
                accession_number = ds.AccessionNumber
                if accession_number not in accession_map:
                    accession_map[accession_number] = uuid4().hex
            except Exception as e:
                print(f"Error reading {dcm_path}: {e}")
            
            i += 1
            if i % 100 == 0:
                print(f"Processed {i} total files", flush=True)

    # Write the accession map to a CSV file
    with open(output_pth, "w") as f:
        f.write("accession_num, subject_id\n")
        for accession_number, uuid in accession_map.items():
            f.write(f"{accession_number},{uuid}\n")
