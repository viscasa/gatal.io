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
<h3 align="center">=====================================</h3>

- [x] Membuat aplikasi dengan nama `main` pada proyek tersebut.

- [x] Melakukan routing pada proyek agar dapat menjalankan aplikasi main.

- [x] Membuat model pada aplikasi `main` dengan nama `Product` dan memiliki atribut wajib sebagai berikut.
    - `name`
    - `price`
    - `description`

- [x] Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
