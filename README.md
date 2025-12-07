# fp-tegraf

Tugas Praktikum Teori Graf (B) Kelompok 14

#### Anggota Kelompok:

1. Raynald Ramadhani Fachriansyah (5025241020)
2. Derryell Josua Ekklesio Pandiangan (5025241175)

---

## Soal 1

Implementasi algoritma backtracking untuk menyelesaikan permasalahan Knight's Tour pada papan catur berukuran n x n. Program ini mencoba untuk menemukan jalur di mana kuda dapat mengunjungi setiap kotak pada papan catur tepat satu kali.

### Cara Menjalankan Program:

1. Pastikan Python terinstal di sistem komputer.
2. Buka terminal dan masuk ke direktori tempat file `knights.py` disimpan.
3. Jalankan program dengan ketik perintah berikut di terminal:
   ```
   python3 knights.py
   ```
4. Tunggu hingga program selesai mengeksekusi dan menampilkan hasilnya grafiknya.

### Input:

Variabel `n` pada kode menentukan ukuran papan catur (n x n). Anda dapat mengubah nilai `n` sesuai kebutuhan di bagian:

```main
if __name__=="__main__":
    n = 8 # Ukuran papan catur n x n
    print(f"Menghitung solusi untuk N={n}...")
```

### Output:

Program akan menampilkan grafik yang menunjukkan jalur yang diambil oleh kuda pada papan catur. Setiap kotak pada papan akan diberi nomor sesuai urutan kunjungan kuda.

## Soal 2

Implementasi algoritma untuk menemukan Largest Monotonically Increasing Subsequence (LMIS) dari sebuah urutan bilangan. Program ini juga menampilkan visualisasi pohon keputusan yang menggambarkan proses pencarian LMIS.

### Cara Menjalankan Program:

1. Pastikan Python terinstal di sistem komputer.
2. Buka terminal dan masuk ke direktori tempat file `lmis.py` disimpan
3. Jalankan program dengan ketik perintah berikut di terminal:
   ```
   python3 lmis.py
   ```
4. Tunggu hingga program selesai mengeksekusi dan menampilkan hasilnya grafiknya.

### Input:

Variabel `sequence` pada kode menentukan urutan bilangan yang akan dianalisis. Untuk mengubah urutan angka yang ingin dianalisis, user dapat mengedit langsung variabel sequence di dalam kode pada bagian:

```
sequence = [4, 1, 13, 7, 0, 2, 8, 11, 3]
```

### Output:

Program akan menampilkan urutan bilangan yang diberikan, LMIS yang ditemukan, dan grafik yang menunjukkan pohon keputusan selama proses pencarian LMIS.
