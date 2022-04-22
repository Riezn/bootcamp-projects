[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=7092950&assignment_repo_type=AssignmentRepo)
# Live Code 1

```{attention}
This page is still on development.
```


## Instruction

Live Code ini dikerjakan dalam format ***notebook*** isi *notebook* harus mengikuti *outline* di bawah ini:
1. Perkenalan\
   Bab pengenalan harus diisi dengan identitas
2. **Judul/Penanda Soal**\
    Sediakan *Cell* Markdown sebelum cell import pustaka yang berisi nomor soal dan judul problem yang dikerjakan di tiap soalnya. Tiap soal mengikuti format nomor 2-5.
3. *Import* pustaka yang dibutuhkan\
   *Cell* pertama pada *notebook* **harus berisi dan hanya berisi** semua *library* yang digunakan dalam *project*.
4. *Data Loading*\
   Bagian ini berisi proses *data loading* yang kemudian dilanjutkan dengan *explorasi data* secara sederhana. Jika tidak ada data, bagian ini tidak perlu.
5. *Answer*\
   Bagian ini berisi proses dalam menjawab soal.
6. Simpan file jupyter notebook dengan nama file h8_p0lc1_NAMA.ipynb dan push ke repository yang telah disediakan (P0LC1) di github organization batch.

---

## Problems

Kamu adalah salah satu tim relawan back office penanganan COVID-19 di Indonesia. Kamu diminta untuk memperoleh data baru dari dataset yang sudah disediakan. Kerjakan dan jawab pertanyaan-pertanyaan berikut. (**Dataset yang disediakan merupakan jumlah kasus kumulatif bukan harian**)
1. Menggunakan Pandas query, ambil data kasus kumulatif Covid-19 tanggal 20 Januari 2022 untuk negara-negara dengan latitude di bawah 0. Negara mana yang paling tinggi jumlah kumulatif kasus Covidnya per tanggal tersebut? Jika bukan Indonesia, bandingkan jumlah kumulatif kasus negara tersebut dengan Indonesia per tanggal yang sama!
2. Buatlah fungsi untuk menghitung jumlah kasus harian Covid-19! (Hint: Kamu bisa menggunakan .diff() untuk menghitung perbedaan tiap baris data/menghitung jumlah kasus harian dan .transpose() untuk mengubah kolom menjadi baris atau sebaliknya)
3. Pada tanggal berapa puncak tertinggi kasus harian Covid-19 di Indonesia? bandingkan dengan tanggal 20 Januari 2022, apakah mengalami penurunan atau kenaikan jumlah kasus?
4. Gunakan for loop dan conditional if untuk membuat sebuah list yang berisikan jumlah kasus harian Covid-19 dengan ketentuan hanya mengambil data Indonesia saja dan jumlah kasus di bawah 10000. Berapa jumlah hari dengan kasus di bawah 10000?


## Dataset:

Dataset dapat diakses melalui link ini: https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv



---

## Assignment Rubrics

### Code Review

|Criteria|Meet Expectations|Points|
|--- |--- |--- |
|Data Loading|Mampu memuat data dengan Pandas| 2 pts |
|Looping Implementation|Mampu menerapkan looping while dalam suatu kasus| 10 pts |
|Conditional If Implementation|Mampu menerapkan konsep conditional if dalam suatu kasus| 10 pts |
|Function Implementation|Mampu menerapkan function pada sebuah kasus| 10 pts |
|Pandas Query Implementation|Mampu mengimplementasikan pandas query dalam pengolahan data| 10 pts |

### Readability

|Criteria|Meet Expectations|Points|
|--- |--- |--- |
|Tertata Dengan Baik|Semua Cell Di Notebook Terdokumentasi Dengan Baik Dengan Markdown Pada Tiap Cell Untuk Penjelasan Kode.| 8 pts |


---

```{admonition} Total Points
**50**
```
