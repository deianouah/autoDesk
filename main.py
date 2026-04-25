import os
import shutil

# 1. تحديد المسارات (تأكد من تغيير 'user' لاسم المستخدم الخاص بك)
downloads_path = "/Users\Deia\Downloads"

# 2. تعريف المجلدات المستهدفة وامتداداتها
folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Zipped": [".zip", ".rar"]
}

# 3. التأكد من وجود المجلدات، وإن لم توجد يتم إنشاؤها
for folder in folders.keys():
    folder_path = os.path.join(downloads_path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# 4. فحص الملفات ونقلها
for filename in os.listdir(downloads_path):
    file_path = os.path.join(downloads_path, filename)
    
    # نتأكد أنه ملف وليس مجلد
    if os.path.isfile(file_path):
        extension = os.path.splitext(filename)[1].lower()
        
        # البحث عن المجلد المناسب للملف
        for folder, extensions in folders.items():
            if extension in extensions:
                destination = os.path.join(downloads_path, folder, filename)
                shutil.move(file_path, destination)
                print(f"تم نقل: {filename} إلى {folder}")