from pathlib import Path
from git import Repo

PATH_OF_GIT_REPO = r'./.git'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'proofread hfml updated'

def git_pull():
    repo = Repo(PATH_OF_GIT_REPO)
    origin = repo.remote(name='origin')
    origin.pull()

def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')

def get_vol_text(vol_path):
    vol_text = ''
    page_paths = list(vol_path.iterdir())
    page_paths.sort()
    for page_path in page_paths:
        if page_path.suffix == ".txt":
            page_num = int(page_path.stem)
            page_content = page_path.read_text(encoding='utf-8')
            vol_text += f'〔{page_num}〕\n{page_content}\n'
    return vol_text

if __name__ == "__main__":
    git_pull()
    # vol_paths = list(Path('./esukhia_tengyur/').iterdir())
    # vol_paths.sort()
    # for vol_path in vol_paths:
    #     vol_text = get_vol_text(vol_path)
    #     Path(f'./proofread_tengyur_hfml/{vol_path.stem}.txt').write_text(vol_text, encoding='utf-8')
    git_push()