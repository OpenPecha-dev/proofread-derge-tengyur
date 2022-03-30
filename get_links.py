import csv

from pathlib import Path

base_link = "https://openpecha.bdrc.io/proofread/proofread-derge-tengyur/"

def get_number_of_page(nalanda_vol):
    number_of_pages = len(list(Path(f'./versions/esukhia_tengyur/{nalanda_vol}/').iterdir()))
    return number_of_pages/2


def make_report(nalanda_vols):
    output_path =f"./nalanda_base_proofread.xlsx"
    header = [" Vol Id", "Link", "Status", "Number of Page"]
    with open(output_path, "w", encoding="UTF8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for nalanda_vol in nalanda_vols:
            nalanda_vol_id = f"v{int(nalanda_vol):03}"
            number_of_pages = get_number_of_page(nalanda_vol_id)
            vol_link = f"{base_link}{nalanda_vol_id}"
            writer.writerow([nalanda_vol_id, vol_link, '', number_of_pages])

if __name__ == "__main__":
    nalanda_vol_list = Path('./nalanda_text_vol.txt').read_text(encoding='utf-8')
    nalanda_vol_list = nalanda_vol_list.splitlines()
    make_report(nalanda_vol_list)
