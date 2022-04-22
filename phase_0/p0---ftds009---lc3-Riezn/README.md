[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=7243705&assignment_repo_type=AssignmentRepo)
# Live Code 3

```{attention}
This page is still on development.
```

## Instruction

Live Code ini dikerjakan dalam format ***notebook*** dan isi *notebook* harus mengikuti *outline* seperti pada file <i>Assignment Template.ipynb</i> dan push file notebook pekerjaannya ke <strong>repository soal</strong>. **Beri nama file dengan: h8_p0lc3_NAMA.ipynb**

---

## Problem

Kamu adalah seorang data scientist di salah satu perusahaan e-commerce. Saat ini, kamu terlibat dalam proyek bersama dengan tim produk dan tim UI/UX untuk merubah tampilan landing page. Menggunakan dataset dari https://raw.githubusercontent.com/fahmimnalfrzki/Dataset/main/purchase_data.txt?token=AEZDEHRU5YLQEXGDDLCL6CLA2KZTI, coba lakukan langkah di bawah:

1. Hitunglah central tendency (mean, median, modus) tanpa menggunakan pandas.DataFrame.describe()! <strong><i>[Memenuhi Rubrik Penilaian Nomor 1c]</strong></i> dan berdasarkan hasil perhitungan central tendency, data cenderung berpusat ke purchased atau non purchased? apa kesimpulanmu? <strong><i>[Memenuhi Rubrik Penilaian Nomor 2a]</strong></i>
2. Buatlah analisa menggunakan konsep A/B testing. Sebelum melakukan perhitungan di Python, definisikan H0 dan H1 dari hipotesis testingnya <strong><i>[Memenuhi Rubrik Penilaian Nomor 2b]</strong></i> dan jenis hipotesis apa yang akan kamu gunakan? <strong><i>[Memenuhi Rubrik Penilaian Nomor 2c]</strong></i>. Setelah melakukan perhitungan menggunakan Python <strong><i>[Memenuhi Rubrik Penilaian Nomor 1d]</strong></i>, Apa kesimpulanmu terhadap hasil A/B testing tsb? <strong><i>[Memenuhi Rubrik Penilaian Nomor 2d]</strong></i>

**Keterangan Dataset:**
- user_id = id pelanggan
- timestamp = Waktu ketika pelanggan mengakses laman web
- group = grup kontrol dan treatment
- landing_page = landing page yang diakses oleh pelanggan (laman lama atau laman baru)
- purchased = 0 : tidak ada pembelian, and 1: ada pembelian


---

## Assignment Rubrics

### 1. Code Review
**Impementasi Code Python**
|No.|Criteria|Meet Expectations|Points|
|--- |--- |--- |--- |
|a|Data Loading|Mampu memuat data dengan Pandas| 1 pts |
|b|Data Processing|Mampu mengolah data sampai siap dianalisa meliputi data cleaning dan missing value checking/handling | 3 pts |
|c|Central Tendency|Mampu menerapkan/menghitung mean, median, modus menggunakan Python (Bukan dengan df.describe())| 3 pts |
|d|A/B Testing Implementation|Mampu menerapkan A/B testing menggunakan scipy| 3 pts |

### 2. Conceptual
**Menjawab Pertanyaan**
|No.|Criteria|Meet Expectations|Points|
|--- |--- |--- |--- |
|a|Central Tendency Concept|Mampu menjawab pertanyaan dengan singkat, jelas, dan padat| 5 pts |
|b|Hypothesis Testing Definition|Mampu menjawab pertanyaan dengan singkat, jelas, dan padat | 5 pts |
|c|Hypothesis Testing Concept|Mampu menjawab pertanyaan dengan singkat, jelas, dan padat| 5 pts |
|d|A/B Testing Analysis|Mampu menjawab pertanyaan dengan singkat, jelas, dan padat| 5 pts |

### 3. Readability

|Criteria|Meet Expectations|Points|
|--- |--- |--- |
|Tertata Dengan Baik|Semua Cell Di Notebook Terdokumentasi Dengan Baik Dengan Markdown Pada Tiap Cell Untuk Penjelasan Kode dan **Format Notebook Sesuai dengan Template**.| 10 pts |

---

```{admonition} Total Points
**40**
```
