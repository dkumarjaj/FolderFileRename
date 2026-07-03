import os

folder = input("Enter the folder path: ")
image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"}
Name=input("Enter the new name prefix (e.g., 'Dev'): ")
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
start = int(input("Enter the starting number for the new names: "))

for i, temp_name in enumerate(temp_files, start=start):
    ext = os.path.splitext(temp_name)[1]
    final_name = f"{Name}{i}{ext}"

    os.rename(
        os.path.join(folder, temp_name),
        os.path.join(folder, final_name)
    )

    print(f"{temp_name} -> {final_name}")

print("✅ Done!")