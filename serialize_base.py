from pathlib import Path

def get_vol_text(vol_path):
    vol_text = ''
    page_paths = list(vol_path.iterdir())
    page_paths.sort()
    for page_path in page_paths:
        if page_path.suffix == ".txt":
            page_num = int(page_path.stem)
            page_content = page_path.read_text(encoding='utf-8')
            vol_text += f'{page_content}\n\n'
    return vol_text

if __name__ == "__main__":
    vol_paths = list(Path('./esukhia_tengyur/').iterdir())
    vol_paths.sort()
    for vol_path in vol_paths:
        vol_text = get_vol_text(vol_path)
        Path(f'./proofread_tengyur_base/{vol_path.stem}.txt').write_text(vol_text, encoding='utf-8')