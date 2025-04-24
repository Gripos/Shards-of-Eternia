import os

# Путь к директории, содержащей .md файлы
root_dir = "D:\Github\Shards-of-Eternia\content"
output_file = "собранный_сеттинг.md"

def read_file_with_fallback(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except UnicodeDecodeError:
        try:
            with open(path, "r", encoding="windows-1251") as f:
                return f.read()
        except Exception as e:
            print(f"Не удалось прочитать файл: {path} — {e}")
            return None

with open(output_file, "w", encoding="utf-8") as outfile:
    for foldername, subfolders, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.lower().endswith(".md"):
                file_path = os.path.join(foldername, filename)
                relative_path = os.path.relpath(file_path, root_dir)
                content = read_file_with_fallback(file_path)
                if content is not None:
                    outfile.write(f"# {relative_path}\n\n")
                    outfile.write(content + "\n\n")
print('готово')
