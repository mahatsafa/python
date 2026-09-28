import subprocess
import sys
from datetime import datetime


def jalankan(perintah):
    hasil = subprocess.run(perintah, capture_output=True, text=True)
    if hasil.stdout.strip():
        print(hasil.stdout.strip())
    if hasil.stderr.strip():
        print(hasil.stderr.strip())
    return hasil


def main():
    # Pesan commit: dari argumen, kalau kosong pakai tanggal & jam otomatis
    if len(sys.argv) > 1:
        pesan = " ".join(sys.argv[1:])
    else:
        pesan = f"update {datetime.now():%Y-%m-%d %H:%M}"

    # Cek apakah ada perubahan
    status = jalankan(["git", "status", "--porcelain"])
    if not status.stdout.strip():
        print("Tidak ada perubahan, tidak ada yang di-push.")
        return

    print("Perubahan yang akan di-commit:")
    jalankan(["git", "status", "--short"])

    jalankan(["git", "add", "."])

    commit = jalankan(["git", "commit", "-m", pesan])
    if commit.returncode != 0:
        print("Commit gagal.")
        return

    push = jalankan(["git", "push"])
    if push.returncode == 0:
        print(f"Selesai: '{pesan}' berhasil di-push.")
    else:
        print("Push gagal, cek pesan error di atas.")


if __name__ == "__main__":
    main()