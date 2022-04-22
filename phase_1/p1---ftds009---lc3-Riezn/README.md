[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=7518594&assignment_repo_type=AssignmentRepo)
# Live Code 3

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
   > Bagian ini berisi proses penyiapan data untuk proses pelatihan model, seperti pembagian data menjadi train-set dan inference-set, transformasi data (normalisasi, encoding, dll.), dan proses-proses lain yang dibutuhkan.

7. Model Definition
   > Bagian ini berisi cell untuk mendefinisikan model. Jelaskan alasan menggunakan suatu algoritma/model, hyperparameter yang dipakai, jenis penggunaan metrics yang dipakai, dan hal lain yang terkait dengan model.

8. Model Training
   > Cell pada bagian ini hanya berisi code untuk melatih model dan output yang dihasilkan. Lakukan beberapa kali proses training dengan hyperparameter yang berbeda untuk melihat hasil yang didapatkan. Analisis dan narasikan hasil ini pada bagian Model Evaluation.

9. Model Evaluation
   > Pada bagian ini, dilakukan evaluasi model yang harus menunjukkan bagaimana performa model berdasarkan metrics yang dipilih. Hal ini harus dibuktikan dengan visualisasi tren performa dan/atau tingkat kesalahan model. **Lakukan analisis terkait dengan hasil pada model dan tuliskan hasil analisisnya**.

10. Model Inference
    > Model yang sudah dilatih akan dicoba pada data yang bukan termasuk ke dalam train-set. Data ini harus dalam format yang asli, bukan data yang sudah di-scaled.
   
11. Pengambilan Kesimpulan
    > Pada bagian terakhir ini, **harus berisi** kesimpulan yang mencerminkan hasil yang didapat dengan *objective* yang sudah ditulis di bagian pengenalan.

12. Notebook harus diupload dalam akun GitHub masing-masing siswa untuk selanjutnya dinilai. Jika dalam sebuah tugas terdapat dua atau lebih soal, maka gabungkan jawaban ke dalam satu file notebook.

13. **Disarankan mengerjakan menggunakan Google Colab**.
    > Segala jenis problem yang muncul akibat masalah yang dialami komputer student saat Live Code karena menggunakan Jupyter Notebook seperti laptop blue screen, laptop freeze, dll, menjadi tanggung jawab student.

---

## Assignment Submission

- Simpan assignment pada sesi ini dengan nama `h8dsft_P1LC3_Set_2_<nama-students>.ipynb` misal `h8dsft_P1LC3_Set_2_raka_ardhi.ipynb`.
- Push Assigment yang telah dibuat ke akun Github masing-masing student.

---

## Problems

Sebuah lembaga LSM berkomitmen untuk memerangi kemiskinan dan menyediakan fasilitas dan bantuan dasar bagi masyarakat di negara-negara kurang mampu. Baru-baru ini, mereka telah mampu mengumpulkan sekitar $ 10 juta. CEO LSM tersebut perlu memutuskan bagaimana menggunakan uang ini secara strategis dan efektif. Isu signifikan yang muncul saat membuat keputusan ini terkait dengan pemilihan negara mana yang paling membutuhkan bantuan. 

Buatlah model machine learning Unsupervised Learning dengan menggunakan KMeans untuk mengelompokkan negara-negara tersebut. Anda diwajibkan untuk menyarankan negara mana yang perlu menjadi fokus CEO. Jawab pertanyaan dibawah ini sebagai acuan analisa/cerita : 

1. Pada bagian eksplorasi data, apa insight menarik yang bisa kamu ceritakan ?

2. Berapa cluster yang berhasil kamu peroleh dari dataset tersebut ? Apakah sudah optimal ? Visualisasikan hasil clustering yang kamu peroleh dengan plot 2 dimensi dimana 2 dimensi tersebut merupakan dimensi yang diperoleh dari hasil reduksi dimensi.

3. Bagaimana karakteristik dari masing-masing cluster ? Bisakah kamu visualisasikan dan ceritakan ?

4. Apa insight menarik yang kamu peroleh dari jawaban/analisa nomor 3 ?

5. Dibandingkan dengan EDA, apakah ada kesamaan dari hasil clustering yang kamu peroleh ? Ceritakan analisamu !

[Dataset URL](https://www.kaggle.com/hellbuoy/pca-kmeans-hierarchical-clustering)

---

## Assignment Rubrics

### Code Review

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Data Loading | Mampu memuat data dengan Pandas | 5 pts  |
| Data Processing and Cleaning | Mampu melakukan pengolahan data dan data cleaning | 15 pts |
| Feature Engineering | Mampu menyeleksi dan menyesuaikan feature yang akan ditrain oleh model | 15 pts |
| Unsupervised Model Implementation | Mampu melakukan training data dengan model KMeans | 20 pts |
| Model Evaluation | Mampu melakukan evaluasi model untuk menentukan nilai `K` / jumlah grup | 15 pts |
| PCA | Mampu melakukan reduksi dimensi dengan menggunakan PCA | 15 pts |

### Readability

| Criteria | Meet Expectations | Points |
| --- | --- |--- |
| Tertata dengan Baik | Semua baris cell dan kode terdokumentasi dengan baik dengan Markdown pada tiap cell untuk penjelasan kode | 10 pts |

### Analysis

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Overall Analysis | Menarik informasi/kesimpulan dari seluruh kegiatan yang dilakukan | 40 pts |

---

```
Total Points : 135
```

---

## Notes

* **Deadline : pukul 11:00 WIB.**

* **Keterlambatan pengumpulan tugas mengakibatkan skor LC 3 menjadi 0.**
