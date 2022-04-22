[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=7372961&assignment_repo_type=AssignmentRepo)
# Live Code 1

## Instruction

Live Code ini dikerjakan dalam format ***notebook (.ipynb)*** . Isi *notebook* harus mengikuti *outline* di bawah ini:
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

---

## Assignment Submission

- Simpan assignment pada sesi ini dengan nama `h8dsft_P1LC1_Set_2_<nama-students>.ipynb` misal `h8dsft_P1LC1_Set_2_raka_ardhi.ipynb`.
- Push Assigment yang telah kalian buat ke akun Github kalian masing-masing.

---

## Problems
1. Buatlah model linear regression untuk memprediksi closing price saham Amazon ([Dataset URL](https://www.kaggle.com/dgawlik/nyse?select=prices-split-adjusted.csv)). Gunakan file `prices-split-adjusted.csv` dalam kasus ini.

2. Buatlah visualisasi yang menampilkan closing price saham `Amazon`, `Cisco`, `Apple`, dan `Netflix` berdasarkan `date` (time series). Saham apa yang memiliki closing price tertinggi dan terendah di akhir tahun 2014, 2015 dan 2016?

3. Buatlah model Logistic Regression untuk memprediksi Loan Pay Back ([Dataset URL](https://www.kaggle.com/sarahvch/predicting-who-pays-back-loans?select=loan_data.csv)). Gunakan file `loan_data.csv` dalam kasus ini.

4. Dengan dataset nomor 3, carilah jumlah `fully paid` tertinggi dan terendah berdasarkan `purpose`. 

### Code Review

| Criteria| Meet Expectations | Points |
| --- | --- | --- |
| Preprocessing | Mampu melakukan preprocessing dataset sebelum melakukan proses modeling (split data, normalisasi, encoding, dll) | 20 pts each number (40 max) |
| Linear Regression | Mengimplementasikan Linear Regression dan menentukan hyperparameter yang tepat dengan Scikit-Learn | 10 pts |
| Logistic Regression | Mengimplementasikan Logistic Regression dan menentukan hyperparameter yang tepat dengan Scikit-Learn | 10 pts |
| Model Evaluation | Mampu melakukan evaluasi terhadap model Linear Regression dan model Logistic Regression yang telah dibuat | 20 pts each (40 max) |
| Model Inference | Mencoba model yang telah dibuat dengan data baru | 10 pts each number (20 max) |
| Apakah Kode Berjalan Tanpa Ada Error? | Kode berjalan tanpa ada error. Seluruh kode berfungsi dan dibuat dengan benar | 10 pts |


### Readability

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Tertata dengan Baik| Semua baris kode terdokumentasi dengan baik dengan Markdown untuk penjelasan kode | 10 pts |

### Analysis

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Model Analysis | Menganalisa informasi dari model yang telah dibuat | 20 pts each number (40 max) |
| EDA Analysis | Menarik informasi/kesimpulan dari eksplorasi data yang dilakukan | 5 pts each number (10 max) |

---

```
Total Points : 190
```

---

## Notes

* **Deadline : pukul 12:15 WIB.**

* **Keterlambatan pengumpulan tugas mengakibatkan skor LC 1 menjadi 0.**
