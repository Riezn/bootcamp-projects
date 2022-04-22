[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=7442091&assignment_repo_type=AssignmentRepo)
# Live Code 2

## Instruction

Live Code ini dikerjakan dalam format ***notebook*** isi *notebook* harus mengikuti *outline* di bawah ini:
1. Perkenalan
   > Bab pengenalan harus diisi dengan identitas.
   
2. Judul/Penanda Soal
   > Sediakan cell markdown sebelum cell import pustaka yang berisi nomor soal dan judul problem yang dikerjakan disetiap soalnya. Setiap soal mengikuti format nomor 3-11.
   
3. Import Pustaka
   > Cell pertama pada *notebook* **harus berisi dan hanya berisi** semua *library* yang digunakan dalam *project*.

4. Data Loading
   > Bagian ini berisi proses penyiapan data sebelum dilakukan eksplorasi data lebih lanjut. Proses Data Loading dapat berupa memberi nama baru untuk setiap kolom, mengecek ukuran dataset, dll.
   
5. Exploratory Data Analysis (EDA)
   > Bagian ini berisi eksplorasi data pada dataset diatas dengan menggunakan query, grouping, visualisasi sederhana, dan lain sebagainya.

6. Data Preprocessing
   > Bagian ini berisi proses penyiapan data untuk proses pelatihan model, seperti pembagian data menjadi train-test-inference, transformasi data (normalisasi, encoding, dll.), dan proses-proses lain yang dibutuhkan.

7. Model Definition
   > Bagian ini berisi cell untuk mendefinisikan model. Jelaskan alasan menggunakan suatu algoritma/model, hyperparameter yang dipakai, jenis penggunaan metrics yang dipakai, dan hal lain yang terkait dengan model.

8. Model Training
   > Cell pada bagian ini hanya berisi code untuk melatih model dan output yang dihasilkan. Lakukan beberapa kali proses training dengan hyperparameter yang berbeda untuk melihat hasil yang didapatkan. Analisis dan narasikan hasil ini pada bagian Model Evaluation.

9. Model Evaluation
   > Pada bagian ini, dilakukan evaluasi model yang harus menunjukkan bagaimana performa model berdasarkan metrics yang dipilih. Hal ini harus dibuktikan dengan visualisasi tren performa dan/atau tingkat kesalahan model. **Lakukan analisis terkait dengan hasil pada model dan tuliskan hasil analisisnya**.

10. Model Inference
    > Model yang sudah dilatih akan dicoba pada data yang bukan termasuk ke dalam train-set ataupun test-set. Data ini harus dalam format yang asli, bukan data yang sudah di-scaled.
   
11. Pengambilan Kesimpulan
    > Pada bagian terakhir ini, **harus berisi** kesimpulan yang mencerminkan hasil yang didapat dengan *objective* yang sudah ditulis di bagian pengenalan.

12. Notebook harus diupload dalam akun GitHub masing-masing siswa untuk selanjutnya dinilai. Jika dalam sebuah tugas terdapat dua atau lebih soal, maka gabungkan jawaban ke dalam satu file notebook.

13. **Disarankan mengerjakan menggunakan Google Colab**.
    > Segala jenis problem yang muncul akibat masalah yang dialami komputer student saat Live Code karena menggunakan Jupyter Notebook seperti laptop blue screen, laptop freeze, dll, menjadi tanggung jawab student.

---

## Assignment Submission

- Simpan assignment pada sesi ini dengan nama `h8dsft_P1LC2_Set_3_<nama-students>.ipynb` misal `h8dsft_P1LC2_Set_3_raka_ardhi.ipynb`.
- Push Assigment yang telah dibuat ke akun Github masing-masing student.

---

## Problems

1. Buatlah model Machine Learning untuk mengklasifikasikan rentang harga (`price_range`). Bandingkan antara model Decision Tree dan Random Forest. **Analisa dua buah model ini dan tentukan model yang terbaik untuk data ini** ! 
   * [Dataset URL](https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification)
   * Gunakan file `train.csv` sebagat `train-set` dan `test-set`.
   * Gunakan file `test.csv` sebagain `inference-set`.

2. Lakukan EDA dengan minimal menjawab pertanyaan dibawah ini : 
   1. Buatlah visualisasi yang membandingkan jumlah mobile phone yang support 3G dan 4G !
   2. Buatlah visualisasi yang membandingkan antara support 4G dan `price_range`! Apakah 4G mempengaruhi `price_range` ?
   3. Buatlah visualisasi yang membandingkan antara RAM dan `price_range` ! Apakah RAM mempengaruhi `price_range` ?
   4. Buatlah visualisasi yang membandingkan antara jumlah core dan `price_range` ! Apakah jumlah core mempengaruhi `price_range` ?
   5. Narasikan visualisasi poin 2.1 hingga 2.4 !

---

## Assignment Rubrics

### Code Review

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Preprocessing | Mampu melakukan preprocessing dataset sebelum melakukan proses modeling (split data, normalisasi, encoding, dll) | 20 pts |
| Decision Tree | Mampu melakukan training data dengan model Decision Tree serta melakukan hyperparameter tunning dengan **maksimal 2 hyperparameter dan 2 set values masing-masing hyperparameter (4 kombinasi)** | 25 pts |
| Ensemble Learning | Mampu melakukan training data dengan model Random Forest serta melakukan hyperparameter tunning dengan **maksimal 2 hyperparameter dan 2 set values masing-masing hyperparameter (4 kombinasi)** | 25 pts |
| Model Evaluation | Mampu melakukan evaluasi model Decision Tree dan Random Forest yang telah dibuat | 20 pts each model (40 max) |
| Model Inference | Mencoba model yang telah dibuat dengan data baru | 10 pts each model (20 max) |
| Apakah Kode Berjalan Tanpa Ada Error? | Kode berjalan tanpa ada error. Seluruh kode berfungsi dan dibuat dengan benar | 10 pts |

### Readability

| Criteria | Meet Expectations | Points |
| --- |--- |--- |
| Tertata dengan Baik | Semua baris cell dan kode terdokumentasi dengan baik dengan Markdown pada tiap cell untuk penjelasan kode | 10 pts |
| Informasi dan Analisa | Terdapat penjelasan/informasi setiap EDA dan informasi setiap keputusan yang diambil pada data terutama di bagian Preprocessing dan penentuan set hyperparameter | 10 pts|

### Analysis

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Model Analysis | Menganalisa informasi dari model yang telah dibuat | 30 pts |
| EDA Analysis | Menarik informasi/kesimpulan dari eksplorasi data yang dilakukan | 40 pts |

---

```
Total Points : 230
```

---

## Notes

* **Deadline : pukul 12:15 WIB.**

* **Keterlambatan pengumpulan tugas mengakibatkan skor LC 2 menjadi 0.**
