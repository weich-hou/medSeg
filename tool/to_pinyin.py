import os
import shutil

import argparse
from tqdm import tqdm

import util


parser = argparse.ArgumentParser("zip_dataset")
parser.add_argument("--in_dir", type=str)
parser.add_argument("--out_dir", type=str)
args = parser.parse_args()


def main():
    files = os.listdir(args.in_dir)
    for f in tqdm(files):
        shutil.copy(
            os.path.join(args.in_dir, f),
            os.path.join(args.out_dir, util.to_pinyin(f)),
        )
        # input("here")


if __name__ == "__main__":
    main()
