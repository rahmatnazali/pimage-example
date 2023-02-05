from pimage import copy_move
import glob

file_list = sorted(glob.glob("input/small/*_copy_rb5.png"))

for i, filename in enumerate(file_list):
    print(f"{i}/{len(file_list)} {filename}")
    copy_move.detect_and_export(filename, "output", verbose=True)
    print()
