import os
import tkinter as tk
from tkinter import filedialog, messagebox

import pymupdf  # PyMuPDF
from PIL import Image


def pilih_file():
    return filedialog.askopenfilename(
        title="Pilih file (PDF atau gambar)",
        filetypes=[
            ("PDF atau gambar", "*.pdf *.png *.jpg *.jpeg"),
            ("PDF", "*.pdf"),
            ("Gambar", "*.png *.jpg *.jpeg"),
        ],
    )


def gambar_ke_pdf(sumber):
    nama = os.path.splitext(os.path.basename(sumber))[0]
    tujuan = filedialog.asksaveasfilename(
        title="Simpan hasil PDF di mana?",
        defaultextension=".pdf",
        initialfile=f"{nama}.pdf",
        filetypes=[("PDF", "*.pdf")],
    )
    if not tujuan:
        return None
    Image.open(sumber).convert("RGB").save(tujuan)
    return tujuan


def pdf_ke_jpg(sumber):
    folder = filedialog.askdirectory(title="Pilih folder untuk menyimpan hasil JPG")
    if not folder:
        return None
    nama = os.path.splitext(os.path.basename(sumber))[0]
    doc = pymupdf.open(sumber)
    for i, halaman in enumerate(doc, start=1):
        pix = halaman.get_pixmap(dpi=150)
        pix.save(os.path.join(folder, f"{nama}_halaman_{i}.jpg"))
    doc.close()
    return folder


def main():
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    sumber = pilih_file()
    if not sumber:
        print("Dibatalkan: tidak ada file dipilih.")
        return

    ext = os.path.splitext(sumber)[1].lower()
    if ext == ".pdf":
        hasil = pdf_ke_jpg(sumber)
    else:
        hasil = gambar_ke_pdf(sumber)

    if hasil:
        print(f"Selesai: {hasil}")
        messagebox.showinfo("Selesai", f"Berhasil disimpan di:\n{hasil}")
    else:
        print("Dibatalkan: lokasi simpan tidak dipilih.")


if __name__ == "__main__":
    main()