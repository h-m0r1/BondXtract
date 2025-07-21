import os
import json

base_dir = "symmetry_operations/json"
all_data = {}

for fname in sorted(os.listdir(base_dir)):
    if fname.startswith("sg_") and fname.endswith(".json"):
        num = fname[3:6]
        with open(os.path.join(base_dir, fname), encoding="utf-8") as f:
            all_data[str(int(num))] = json.load(f)

with open("embedded_spacegroups.js", "w", encoding="utf-8") as f:
    f.write("const embeddedSpaceGroupData = ")
    json.dump(all_data, f, ensure_ascii=False, indent=2)
    f.write(";")