import os

folder = r"C:\Users\😴\OneDrive\Desktop\Photos"
image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"}

files = sorted(
    f for f in os.listdir(folder)
    if os.path.splitext(f)[1].lower() in image_extensions
)

# Pass 1: Rename to temporary names
temp_files = []
for i, file in enumerate(files):
    ext = os.path.splitext(file)[1]
    temp_name = f"__temp__{i}{ext}"

    os.rename(
        os.path.join(folder, file),
        os.path.join(folder, temp_name)
    )

    temp_files.append(temp_name)

# Pass 2: Rename to final names
start = 7

for i, temp_name in enumerate(temp_files, start=start):
    ext = os.path.splitext(temp_name)[1]
    final_name = f"Dev{i}{ext}"

    os.rename(
        os.path.join(folder, temp_name),
        os.path.join(folder, final_name)
    )

    print(f"{temp_name} -> {final_name}")

print("✅ Done!")