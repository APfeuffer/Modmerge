import os, sys
from pathlib import Path

def merge(dst, *src, verbose=True):
    if all([os.path.isfile(s) for s in src]):
        if verbose: print(f"{dst} is a file, using first source: {src[0]}")
        os.makedirs(Path(dst).parent,exist_ok=True)
        os.symlink(os.path.abspath(src[0]),dst)
    elif all([os.path.isdir(s) for s in src]):
        if len(src)==1 and dst!='.' and dst!='..':
            if verbose: print(f"{dst} is a directory with only one source: {src[0]}")
            os.makedirs(Path(dst).parent,exist_ok=True)
            os.symlink(os.path.abspath(src[0]),dst)
        else:
            if verbose: print(f"{dst} is a directory with multiple sources, merging recursively...")
            contents = {}
            for s in src:
                cnt = list(os.listdir(s))
                for c in cnt:
                    if c in contents: contents[c]+=[s+'/'+c]
                    else: contents[c]=[s+'/'+c]
            for entry, sources in contents.items():
                if len(dst): merge(dst+'/'+entry,*sources)
                else: merge(entry,*sources)
    else:
        print(f"Merge failed. Sources must be either all files or all directories:\n{'\n'.join(src)}")

if __name__=="__main__":
    merge(*sys.argv[1:])
