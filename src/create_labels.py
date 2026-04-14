import os

train_img_dir = "data/images/train"
train_label_dir = "data/labels/train"

val_img_dir = "data/images/val"
val_label_dir = "data/labels/val"

os.makedirs(train_label_dir, exist_ok=True)
os.makedirs(val_label_dir, exist_ok=True)

print("🚀 SCRIPT STARTED")

def create_labels(image_dir, label_dir):
    print(f"\n🔍 Checking: {image_dir}")

    if not os.path.exists(image_dir):
        print("❌ PATH DOES NOT EXIST")
        return

    files = os.listdir(image_dir)
    print(f"📂 Files found: {len(files)}")

    if len(files) == 0:
        print("❌ EMPTY FOLDER")
        return

    count = 0

    for img_name in files:
        print("👉 Processing:", img_name)

        if not img_name.lower().endswith((".jpeg", ".jpg", ".png")):
            continue

        label_name = os.path.splitext(img_name)[0] + ".txt"
        label_path = os.path.join(label_dir, label_name)

        if "bacteria" in img_name.lower() or "virus" in img_name.lower():
            with open(label_path, "w") as f:
                f.write("0 0.5 0.5 1 1")
        else:
            open(label_path, "w").close()

        count += 1

    print(f"✅ Labels created: {count}")

create_labels(train_img_dir, train_label_dir)
create_labels(val_img_dir, val_label_dir)

print("\n🎯 DONE")