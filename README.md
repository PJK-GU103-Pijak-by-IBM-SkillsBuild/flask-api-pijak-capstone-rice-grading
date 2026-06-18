# RICE QUALITY PREDICTION
**ID TIM: PJK-GU103**

**Cek kualitas beras anda dengan mudah dengan landasan SNI.**  
Hanya dengan menginputkan gambar beras anda untuk mengetahui kualitas beras anda.

---

## Tentang RICE QUALITY PREDICTION

Proyek Rice Quality Prediction adalah pengembangan sistem kecerdasan buatan (deep learning berbasis computer vision) untuk mengotomatisasi klasifikasi kualitas fisik beras.
- **Cara Kerja**: Sistem akan menganalisis gambar beras berdasarkan parameter fisik seperti persentase butir patah, warna atau derajat sosoh, dan keberadaan benda asing. Analisis ini sepenuhnya mengacu pada standar nasional SNI 6128:2020.
- **Tujuan**: Menggantikan proses inspeksi manual yang lambat dan subjektif menjadi sistem penilaian yang lebih cepat, objektif, dan efisien.
- **Hasil Akhir**: Model klasifikasi ini akan diintegrasikan ke dalam sebuah web UI sederhana yang memungkinkan pengguna untuk mengunggah gambar beras dan langsung melihat hasil prediksi kualitasnya.


## Setup Environment and Run
Environment:
```
cp .env.example .env
```
silahkan sesuaikan environment dan menggunakan model berikut ([tautan model](https://huggingface.co/arykurnia/pijak-capstone-rice-grading)):
```
REPO_ID=arykurnia/pijak-capstone-rice-grading
MODEL_FILENAME=mobilenetv2_rice_quality.tflite
```
Run Code:
```bash
pip install -r requirements.txt
python run.py
```
or Docker:
```
docker pull arykurnia/api-rice-grading-flask:latest
docker run -p 5000:5000 arykurnia/api-rice-grading-flask:latest
```

## Endpoint API
[Documentation](https://pijak.arykurnia.my.id/docs/)
---



