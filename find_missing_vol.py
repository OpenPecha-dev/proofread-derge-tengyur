from pathlib import Path

def get_text_list(list_path):
    text_list = list_path.read_text(encoding='utf-8').splitlines()
    text_list = list(set(text_list))
    text_list.sort()
    return text_list

def find_missing_vols():
    missing_vols = []
    nalanda_vols = get_text_list(Path('./nalanda_text_vol.txt'))
    vol_paths = list(Path(f'./versions/acip_tengyur').iterdir())
    vol_paths.sort()
    acip_vols = []
    for vol_path in vol_paths:
        vol_id = vol_path.stem
        acip_vols.append(vol_id)
    for nalanda_vol in nalanda_vols:
        if nalanda_vol in acip_vols:
            continue
        else:
            missing_vols.append(nalanda_vol)
    missing_vols = list(set(missing_vols))
    missing_vols.sort()
    Path('./missing_vol.txt').write_text("\n".join(missing_vols), encoding='utf-8')



if __name__ == "__main__":
    find_missing_vols()
