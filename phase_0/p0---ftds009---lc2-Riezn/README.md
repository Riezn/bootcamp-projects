[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=7182830&assignment_repo_type=AssignmentRepo)
# Live Code 2

# Instruction

Live Code ini dikerjakan dalam format ***notebook*** isi *notebook* harus mengikuti *outline* di bawah ini:
1. Perkenalan\
   Bab pengenalan harus diisi dengan identitas
2. **Judul/Penanda Soal**\
    Sediakan *Cell* Markdown sebelum cell import pustaka yang berisi nomor soal dan judul problem yang dikerjakan di tiap soalnya. Tiap soal mengikuti format nomor 2-6.
3. *Import* pustaka yang dibutuhkan\
   *Cell* pertama pada *notebook* **harus berisi dan hanya berisi** semua *library* yang digunakan dalam *project*.
4. *Data Loading*\
   Bagian ini berisi proses *data loading* yang kemudian dilanjutkan dengan *explorasi data* secara sederhana. Jika tidak ada data yang dimuat, abaikan bagian ini.
5. *Mathematical Calculations*\
   Bagian ini berisi proses pengolahan data dengan perhitungan matematis yang diperlukan.
6. Hasil\
   Pada bab terakhir ini berisi jawaban dari pertanyaan soal.
7. **Kumpulkan file ipynb dengan nama file h8_p0lc2_NAMA.ipynb dan push ke repository ini.**

---

# Problems

## Nomor 1 
Perang sedang berkecamuk! Tentara negara kita ingin melakukan komunikasi ke sekutunya tanpa diketahui oleh negara musuh. Untuk itu, kamu diminta untuk mengubah pesan kalimat menjadi pesan transmisi.

  Pesan yang ingin dikirim adalah: "**Prepare to negotiate**".

 ### Instruksi/Clue No. 1:
  <ol type="a">
  <li> Mengubah sebuah pesan berupa kalimat ke kode/pesan transmisi yang berupa kumpulan angka disebut sebagai <i>encode</i> dan sebaliknya disebut <i>decode</i>. Cara untuk melakukan <i>encode</i> adalah dengan mengalikan matriks yang berisikan pesan kalimat dengan matriks encoder. </li>
  <li> Konversikan tiap karakter pada pesan di atas ke dalam angka dan simpan ke dalam numpy array (Boleh pakai metode/teknik apapun). Contoh: A=1, Z=26, dan spasi=0. Untuk kalimat "Siap bersedia" akan terkonversi menjadi np.array([19,9,1,16,0,2,5,18,19,5,7,9,1]). </li>
  <li> Numpy array yang masih berupa 1D-array (vektor) dapat diubah ke matriks (2-D array) dengan menggunakan method reshape (NumPy). (Ukuran matriks menyesuaikan dengan ukuran encode matriks sehingga bisa dikalikan). Matriks ini akan kita sebut sebagai <strong>matriks pesan</strong>. <strong><i>[Memenuhi Rubrik Penilaian Nomor 1a]</i></strong>. </li>
  <li> Untuk mengkonversi kalimat ke kode transmisi, buatlah <strong>matriks encoder</strong> 4x4 berikut: </li>
<center><img align='center' src="https://latex.codecogs.com/gif.latex?E=\begin{bmatrix}&space;2&space;&&space;1&space;&&space;0&space;&&space;4\\&space;3&space;&&space;4&space;&&space;2&space;&&space;1\\&space;1&space;&&space;1&space;&&space;9&space;&&space;0\\&space;0&space;&&space;7&space;&&space;8&space;&space;&&space;3\end{bmatrix}" title="E=\begin{bmatrix} 2 & 1 & 0 & 4\\ 3 & 4 & 2 & 1\\ 1 & 1 & 9 & 0\\ 0 & 7 & 8 & 3\end{bmatrix}" /></center> 
  
  <li> Kalikan <strong>matriks encoder</strong> yang telah ditentukan dengan <strong>matriks pesan</strong>. Tunjukkan bahwa pesan sudah berhasil di-encode (Perkalian dua matriks berhasil menghasilkan matriks baru yang kita namakan sebagai <strong>matriks transmisi</strong>). <strong><i>[Memenuhi Rubrik Penilaian Nomor 1b]</i></strong> </li>
  <li> Agar menyakinkan apakah perhitungan kamu sudah benar, lakukan decode pesan yang sudah di-encode dengan cara mengalikan <strong>matriks transmisi</strong> dengan <strong>inverse matriks encoder</strong>, E. Hasil perkalian matriksnya akan kita sebut sebagai <strong>matriks decoded</strong> Tunjukkan bahwa matriks hasil decode sama dengan matriks pesan sebelum di-encode. (Kamu bisa pakai bantuan <i>np.allclose</i> untuk mengecek matriks decoded dengan matriks pesan sama atau tidak). </li>
</ol>

### Pertanyaan yang harus dijawab:
1. Pada langkah c, berapa ukuran matriks yang pesan yang memungkinkan untuk dapat dikalikan dengan matriks encoder? dan mengapa jawabannya demikian? <strong><i>[Memenuhi Rubrik Penilaian Nomor 2a - 5 Pt]</i></strong>
2. Apakah susunan perkalian yang benar antara **matriks pesan x matriks encoder** atau **matriks encoder x matriks pesan** sama saja? jika sama, mengapa? dan jika berbeda mengapa demikian dan susunan mana yang benar?<strong><i>[Memenuhi Rubrik Penilaian Nomor 2a - 5 Pt]</i></strong>
3. Pada langkah f, untuk melakukan decoding, digunakan perkalian antara matriks transmisi dengan inverse matriks encoder dimana harapannya hasil perkaliannya menghasilkan matriks yang sama/mirip dengan matriks pesan. Mengapa mengalikan matriks transmisi dengan inverse matriks encoder dan mengapa tidak dengan matriks encoder biasa saja tanpa di-inverse?<strong><i>[Memenuhi Rubrik Penilaian Nomor 2a - 5 Pt]</i></strong>

**Jawab dengan *markdown***

## Nomor 2
Dalam training data dengan model machine learning, salah satu metrik yang dapat dijadikan referensi untuk mengevaluasi kecocokan antara model dan data adalah ROC (Receiver Operating Charateristics) curve. ROC curve dibangun dari hubungan antara False Positive Rate/FPR (sumbu X) dan True Positive Rate/TPR (sumbu Y), masing-masing bernilai dari 0-1. Selain ROC Curve, kadangkala orang mengevaluasi model menggunakan ROC AUC score yang tidak lain adalah luas area di bawah kurva ROC. Untuk menghitung ROC AUC score, gunakan konsep integral.

  Pada dataset yang tersedia, hitung nilai ROC AUC score untuk masing-masing model Random Forest Regressor dan Support Machine Regressor (SVR). Manakah yang terbaik? (Model terbaik adalah yang ROC Score nya paling besar dan mendekati 1). **SEBELUM MENYELESAIKAN PROBLEM DENGAN CODE, JAWAB PERTANYAAN DI BAWAH**.
  
 ### Pertanyaan yang harus dijawab:
 1. Jenis integral apakah untuk menghitung luas area di bawah kurva ROC? mengapa demikian? <strong><i>[Memenuhi Rubrik Penilaian Nomor 2b - 5 Pt]</i></strong>
 2. Untuk menyelesaikan persoalan menghitung ROC AUC score, metode apa yang kita pakai, simbolik atau numerik? apakah perlu pendefinisian fungsi matematis? <strong><i>[Memenuhi Rubrik Penilaian Nomor 2b - 5 Pt]</i></strong>
 
 **Jawab dengan *markdown***

**SESUDAH MENYELESAIKAN PROBLEM DENGAN CODE, JAWAB PERTANYAAN DIBAWAH:**
3. Manakan model yang terbaik berdasarkan hasil perhitungan ROC AUC score? jelaskan mengapa! <strong><i>[Memenuhi Rubrik Penilaian Nomor 2b - 5 Pt]</i></strong>

**Jawab dengan *markdown***

  ### Dataset

  Dataset dapat diunduh dari link berikut: https://raw.githubusercontent.com/fahmimnalfrzki/Dataset/main/ROC%20Curve%20SVR%20-%20Random%20Forest.csv?token=AEZDEHVS66CKQBUSHKZ534TA44EVO.

  Keterangan kolom:
  - svr_fpr = False Positive Rate model SVR
  - svr_tpr = True Positive Rate model SVR
  - rfr_fpr = False Positive Rate model Random Forest
  - rfr_tpr = True Positive Rate model Random Forest

---

## Assignment Rubrics

### 1. Code Review
**Impementasi Code Python**
|No.|Criteria|Meet Expectations|Points|
|--- |--- |--- |--- |
|a|Matrix Implementation|Dapat membuat matrix menggunakan library Numpy| 2 pts |
|b|Linear Algebra Implementation|Mampu menerapkan konsep operasi aritmetika matriks dengan library NumPy| 4 pts |
|c|Data Loading|Mampu memuat data dengan Pandas (Nomor 2) | 2 pts |
|d|Calculus Implementation|Mampu menerapkan konsep Integral dengan library Scipy| 4 pts |

### 2. Conceptual
**Menjawab Pertanyaan**
|No.|Criteria|Meet Expectations|Points|
|--- |--- |--- |--- |
|a|Linear Algebra Concept|Mampu menjawab pertanyaan secara singkat, padas, dan jelas menggunakan konsep matriks (masing-masing soal: 5 pt)| 15 pts |
|b|Calculus Concept|Mampu menjawab pertanyaan secara singkat, padas, dan jelas menggunakan konsep integral (masing-masing soal: 5 pt)| 15 pts |

### 3. Readability

|Criteria|Meet Expectations|Points|
|--- |--- |--- |
|Tertata Dengan Baik|Semua Cell Di Notebook Terdokumentasi Dengan Baik Dengan Markdown Pada Tiap Cell Untuk Penjelasan Kode.| 8 pts |

---

```{admonition} Total Points
**50**
```
