# 🐍 Python

Kumpulan proyek dan eksperimen Python milik saya. Repo ini dipakai untuk belajar dan mencoba banyak hal, mulai dari mengolah file sampai computer vision.

## 📁 Daftar Proyek

| Proyek | Deskripsi | Status |
|--------|-----------|--------|
| [`pdf-jpg-converter`](./pdf-jpg-converter) | Konversi PDF ke JPG dan JPG ke PDF | 🚧 Direncanakan |
| [`hand-detection`](./hand-detection) | Deteksi tangan secara real-time lewat kamera | 🚧 Direncanakan |

> Daftar ini akan bertambah seiring proyek baru dibuat.

## 🗂️ Struktur Repo

```
python/
├── README.md
├── .gitignore
├── pdf-jpg-converter/
│   ├── pdf_to_jpg.py
│   ├── jpg_to_pdf.py
│   └── requirements.txt
└── hand-detection/
    ├── hand_detect.py
    └── requirements.txt
```

## ⚙️ Persiapan

1. Pastikan Python 3.9 atau lebih baru sudah terpasang:

   ```bash
   python --version
   ```

2. Clone repo ini:

   ```bash
   git clone https://github.com/mahatsafa/python.git
   cd python
   ```

3. Buat virtual environment (disarankan satu per proyek):

   ```bash
   python -m venv venv
   ```

   Aktifkan:

   - Windows: `venv\Scripts\activate`
   - macOS / Linux: `source venv/bin/activate`

4. Install dependensi proyek yang ingin dijalankan:

   ```bash
   pip install -r nama-proyek/requirements.txt
   ```

## 🛠️ Library yang Direncanakan

- **PyMuPDF**: membaca PDF dan mengubah halamannya menjadi gambar
- **Pillow**: mengolah gambar dan menyusunnya menjadi PDF
- **OpenCV**: akses kamera dan pemrosesan video
- **MediaPipe**: deteksi dan pelacakan tangan (21 titik landmark)

## 🎯 Rencana ke Depan

- [ ] Konversi PDF ke JPG
- [ ] Konversi JPG ke PDF
- [ ] Tampilkan feed kamera dengan OpenCV
- [ ] Deteksi tangan dan gambar landmark di layar
- [ ] Hitung jumlah jari yang terangkat
- [ ] Kenali gestur sederhana

## 📝 Catatan

Repo ini masih dalam tahap awal dan terus berkembang. Setiap proyek nanti punya `requirements.txt` sendiri supaya dependensinya tidak bercampur.

## 👤 Author

[@mahatsafa](https://github.com/mahatsafa)