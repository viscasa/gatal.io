<h1 align="center">WELCOME TO GATAL.IO !!!</h1>
<p align="center"> <img src="asset/img/Logo.jpg" width="150"></p>

Gatal.io adalah salah satu platform _e-commerce_ Indonesia untuk menjual barang-barang digital, termasuk _video game indie_, _asset game_, musik, dan banyak lagi.

## Tugas 2
### Proses Pembuatan Proyek Django hingga Melakukan Deployment ke PWS:
- [x] Membuat sebuah proyek Django baru.
    1. Buat repositori baru di Github dengan nama ```gatal.io```
    2. Buat direktori lokal dan hubungkan dengan repositori di Github dengan _mantra_ :
        ```bash
        git init 
        git remote add origin https://github.com/viscasa/gatal.io.git
        ```
    3. Buat _virtual environment_ dengan menjalankan _command_ berikut di direktori lokal:
        ```bash
        python -m venv env
        ```
    4. Aktifkan _virtual environment_ dengan _command_ berikut di direktori lokal:
        ```bash
        env\Scripts\activate
        ```
    5. Di direktori yang sama, tambahkan _file_ `requirements.txt` untuk membuat _dependencies_ yang berisikan:
        ```
        django
        gunicorn
        whitenoise
        psycopg2-binary
        requests
        urllib3
        ```
    6. Lakukan instalasi terhadap _dependencies_ tadi dengan _command_ berikut:
        ```bash
        pip install -r requirements.txt
        ```
    7. Buat proyek Django bernama `gatal_io` dengan _command_ berikut:
        ```bash
        django-admin startproject gatal_io .
        ```

<h5 align="center">==========================================================</h5>

- [x] Membuat aplikasi dengan nama `main` pada proyek tersebut.
    1. Mengubah `ALLOWED_HOSTS` di file `settings.py` pada direktori proyek untuk keperluan deployment dengan menambahkan:
        ```
        ...
        ALLOWED_HOSTS = ["localhost", "127.0.0.1", "alwie-attar-gatalio.pbp.cs.ui.ac.id"]
        ...
        ```
    2. Membuat aplikasi `main` dengan _command_:
        ```bash
        python manage.py startapp main
        ```

<h5 align="center">==========================================================</h5>

- [x] Melakukan _routing_ pada proyek agar dapat menjalankan aplikasi `main`.
    1. Mendaftarkan aplikasi `main` ke dalam `setting.py`:
        ```python
        INSTALLED_APPS = [
        ...,
        'main'
        ]
        ```

<h5 align="center">==========================================================</h5>

- [x] Membuat model pada aplikasi `main` dengan nama `Product` dan memiliki atribut wajib sebagai berikut.
    - `name`
    - `price`
    - `description`
    1. Isi _file_ `models.py` di direktori `main` dengan kode berikut:
        ```python
        from django.db import models

        class Product(models.Model):
            name = models.CharField(max_length=255)
            price = models.IntegerField()
            description = models.TextField()
            rating = models.FloatField()
            genre = models.TextField()
        ```
    2. Jalankan _command_ berikut untuk membuat migrasi model:
        ```bash
        python manage.py makemigrations
        ```
    3. Jalankan _command_ berikut untuk menerapkan migrasi ke dalam basis data lokal.
        ```bash
        python manage.py migrate
        ```

<h5 align="center">==========================================================</h5>

- [x] Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.

    1. Buat direktori baru bernama `templates` di dalam direktori aplikasi `main`.
    2. Di dalam direktori `templates`, buat _file_ baru bernama `main.html`. Isi _file_ `main.html` dengan kode berikut:
        ```html
        <h1 align="center">WELCOME TO GATAL.IO !!!</h1>

        <h5>Name: {{ name }}</h5>
        <h5>Class: {{ class }}</h5>
        ```
    3. Buka _file_ `views.py` yang terletak di dalam direktori `main`. Lalu ubah isinya menjadi kode berikut:
        ```python
        from django.shortcuts import render

        def show_main(request):
            context = {
                'name': 'Alwie Attar Elfandra',
                'class': 'PBP D'
            }

            return render(request, "main.html", context)
        ```

<h5 align="center">==========================================================</h5>

- [x] Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
    1. Buat _file_ `urls.py` di dalam direktori `main`
    2. Isi file tersebut dengan kode:
        ```python
        from django.urls import path
        from main.views import show_main

        app_name = 'main'

        urlpatterns = [
            path('', show_main, name='show_main'),
        ]
        ```
    3. _Routing_ url pada file `urls.py` di direktori `gatal_io` sehingga isi file `urls.py` menjadi:
        ```python
        from django.contrib import admin
        from django.urls import path, include

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', include('main.urls'))
        ]
        ```

<h5 align="center">==========================================================</h5>

- [x] Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
    1. Lakukan tes pada proyek Django yang sudah kamu buat dengan menjalankan perintah `python manage.py runserver`
    2. Buka http://localhost:8000/ di incognito mode
    3. Jika proyek sudah aman, anda bisa matikan Django servernya dan melakukan deploy ke situs PWS.
    4. Pastikan Anda sudah melakukan registrasi pada situs PWS (https://pbp.cs.ui.ac.id/) dan sudah membuat proyek di PWS tersebut.
    5. Jalankan perintah yang terdapat pada informasi _Project Command_ pada halaman PWS, maka proyek anda sudah berhasil di-_deploy_ ke PWS.
    6. Apabila kedepannya ada perubahan pada proyek Django Anda yang ingin Anda push ke PWS, jalankan _command_ berikut:
        ```bash
        git push pws main:master
        ```

<h5 align="center">==========================================================
</h5>

<h3 align="center">
Bagan <i>Request User</i> ke <i>Web</i> Aplikasi berbasis Django
</h3>

<p align="center"> 
    <img src="asset/img/MVT.jpg">
</p>

Request dari user akan diproses terlebih dahulu sehingga dapat diteruskan ke View yang sesuai. kemudian View tersebut akan membaca/menulis data di Model dan menggunakan Template yang sesuai untuk menampilkan dan mengembalikan response ke user.

<h5 align="center">==========================================================
</h5>

### Fungsi git dalam pengembangan perangkat lunak
1. **Versi Kontrol:** Git memungkinkan pengembang melacak perubahan kode sumber dari waktu ke waktu. Setiap perubahan disimpan sebagai versi (_commit_), sehingga mudah untuk kembali ke versi sebelumnya jika diperlukan.

2. **Kolaborasi Tim:** Dengan Git, banyak pengembang dapat bekerja secara bersamaan di proyek yang sama tanpa saling mengganggu pekerjaan satu sama lain. _Branching_ (pembuatan cabang) mempermudah pekerjaan di fitur yang berbeda sebelum digabungkan (_merged_) ke cabang utama.

3. **Pemecahan Konflik:** Git memudahkan deteksi dan resolusi konflik kode ketika dua atau lebih pengembang mengedit file yang sama.

4. **Backup & Repositori Terdistribusi:** Git menyimpan salinan lengkap dari repositori di setiap mesin yang menggunakannya, sehingga kode aman jika server pusat tidak dapat diakses atau hilang.

5. **Branching dan Merging:** Git memungkinkan pembuatan cabang (_branch_) untuk pengembangan fitur baru atau eksperimen tanpa mempengaruhi kode utama. Setelah diuji, perubahan dari cabang ini bisa digabungkan (_merge_) ke cabang utama.

<h5 align="center">==========================================================
</h5>

### Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

1. Django menggunakan Python yang mudah dipahami, cocok untuk pemula.
2. Banyak fitur bawaan yang langsung siap digunakan tanpa konfigurasi tambahan.
3. Arsitektur Model-View-Template (MVT) membantu pemula memahami struktur kode yang baik.
4. Dokumentasi yang lengkap dan mudah diikuti memudahkan pembelajaran.
5. Komunitas besar dan aktif menyediakan banyak sumber belajar dan bantuan.

<h5 align="center">==========================================================
</h5>

### Mengapa model pada Django disebut sebagai ORM?

Model pada Django disebut sebagai **ORM** (Object-Relational Mapping) karena berfungsi sebagai penghubung antara objek Python dan tabel dalam database relasional. Dengan ORM, pengembang dapat berinteraksi dengan database menggunakan kode Python tanpa harus menulis query SQL secara langsung. Setiap model merepresentasikan tabel dalam database, di mana kolom menjadi atribut objek Python. ORM memudahkan operasi seperti insert, update, dan query data, serta memungkinkan otomatisasi manajemen skema database dan mendukung berbagai jenis database. Selain itu, ORM juga menangani relasi antar tabel dengan mudah, menjadikan pengelolaan data lebih intuitif dan aman.