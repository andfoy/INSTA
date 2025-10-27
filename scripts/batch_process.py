import os
import os.path as osp
import argparse
import subprocess

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-dir', type=str, help='Input dir', required=True)
    args = parser.parse_args()

    for root, dirs, _ in os.walk(args.input_dir):
        for dir in dirs:
            if dir[0] == '.':
                continue
            subprocess.run(["bash", "generate.sh", osp.join(root, dir),
                            osp.join(root, dir, "INSTA"), "10"])
